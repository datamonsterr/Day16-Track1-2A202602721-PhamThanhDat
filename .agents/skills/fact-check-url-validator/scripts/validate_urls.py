#!/usr/bin/env python3
"""
URL Validator & 404 Recovery Tool
Scans files or URLs, tests HTTP status, and automatically checks Wayback Machine
or generates search queries to recover broken (404) URLs.
"""

import sys
import os
import re
import json
import urllib.request
import urllib.parse
import urllib.error

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

def extract_urls_from_markdown(file_path: str):
    urls = []
    if not os.path.exists(file_path):
        return urls
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Match markdown [text](url) and raw https?:// URLs
    md_links = re.findall(r'\[([^\]]+)\]\((https?://[^\s\)]+)\)', content)
    for text, url in md_links:
        urls.append({"text": text, "url": url})
        
    raw_urls = re.findall(r'(?<!\()(https?://[^\s\)\>\]]+)', content)
    for url in raw_urls:
        if not any(u["url"] == url for u in urls):
            urls.append({"text": url, "url": url})
            
    return urls

def check_url_status(url: str, timeout: int = 8):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "*/*"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return {
                "url": url,
                "status": resp.status,
                "ok": 200 <= resp.status < 400,
                "final_url": resp.geturl(),
                "error": None
            }
    except urllib.error.HTTPError as e:
        return {
            "url": url,
            "status": e.code,
            "ok": False,
            "final_url": url,
            "error": f"HTTP {e.code}: {e.reason}"
        }
    except urllib.error.URLError as e:
        return {
            "url": url,
            "status": None,
            "ok": False,
            "final_url": url,
            "error": f"URL Error: {e.reason}"
        }
    except Exception as e:
        return {
            "url": url,
            "status": None,
            "ok": False,
            "final_url": url,
            "error": str(e)
        }

def query_wayback_machine(url: str):
    api_url = f"https://archive.org/wayback/available?url={urllib.parse.quote(url)}"
    req = urllib.request.Request(api_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            snapshots = data.get("archived_snapshots", {})
            closest = snapshots.get("closest", {})
            if closest and closest.get("available"):
                return {
                    "available": True,
                    "snapshot_url": closest.get("url"),
                    "timestamp": closest.get("timestamp")
                }
    except Exception as e:
        return {"available": False, "error": str(e)}
    return {"available": False}

def suggest_recovery_query(url: str, text: str = ""):
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc
    path_slug = re.sub(r'[/_\-\.]+', ' ', parsed.path).strip()
    query_parts = []
    if domain:
        query_parts.append(f"site:{domain}")
    if text and text != url:
        query_parts.append(text)
    elif path_slug:
        query_parts.append(path_slug)
    return " ".join(query_parts)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_urls.py <markdown_file_or_url>")
        sys.exit(1)

    target = sys.argv[1]
    items_to_check = []

    if target.startswith("http://") or target.startswith("https://"):
        items_to_check.append({"text": target, "url": target})
    else:
        items_to_check = extract_urls_from_markdown(target)

    print(f"🔍 Validating {len(items_to_check)} URLs...")
    results = []

    for item in items_to_check:
        url = item["url"]
        print(f"\nChecking: {url}")
        res = check_url_status(url)
        if res["ok"]:
            print(f"  ✅ OK: HTTP {res['status']}")
            if res["final_url"] != url:
                print(f"     Redirected to: {res['final_url']}")
        else:
            print(f"  ❌ FAILED: {res['error']}")
            if res.get("status") == 404 or "404" in str(res.get("error")):
                print("  🔄 Attempting 404 Recovery:")
                wb = query_wayback_machine(url)
                if wb.get("available"):
                    print(f"     🏛️ Wayback Archive found: {wb['snapshot_url']}")
                    res["archive_url"] = wb["snapshot_url"]
                else:
                    print("     ⚠️ No direct Wayback archive found.")
                
                search_query = suggest_recovery_query(url, item.get("text", ""))
                print(f"     🔎 Recommended search query: '{search_query}'")
                res["recovery_query"] = search_query
        results.append(res)

    print("\n" + "="*50)
    summary_ok = sum(1 for r in results if r["ok"])
    summary_fail = len(results) - summary_ok
    print(f"📊 Summary: Total={len(results)} | Valid={summary_ok} | Failed/404={summary_fail}")

if __name__ == "__main__":
    main()

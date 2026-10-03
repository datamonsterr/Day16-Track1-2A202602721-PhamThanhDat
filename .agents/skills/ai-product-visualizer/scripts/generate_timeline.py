#!/usr/bin/env python3
"""
AI Product Timeline & Infographic Generator
Generates standalone SVG and HTML timeline infographics with official vector logos
(Google Gemini, NotebookLM, OpenAI).
"""

import os
import sys
import json
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
ICONS_DIR = SKILL_DIR / "resources" / "icons"

def load_icon_content(icon_name: str) -> str:
    path = ICONS_DIR / icon_name
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

# Default milestones extracted from Gemini research
DEFAULT_MILESTONES = [
    {
        "date": "06/2017",
        "title": "Nền móng Transformer",
        "product": "Google Brain / Research",
        "icon": "gemini-sparkle.svg",
        "desc": "Công bố cơ chế Self-Attention thay thế RNN/CNN, khởi nguyên toàn bộ kỷ nguyên LLM.",
        "badge": "Breakthrough"
    },
    {
        "date": "10/2018",
        "title": "BERT & Core Search",
        "product": "Google Search",
        "icon": "gemini-sparkle.svg",
        "desc": "Mô hình ngữ cảnh 2 chiều tích hợp trực tiếp vào Search, củng cố hào kinh tế cốt lõi.",
        "badge": "Core Moat"
    },
    {
        "date": "12/2023",
        "title": "Gemini 1.0 & Cloud TPU v5p",
        "product": "Google DeepMind",
        "icon": "gemini-sparkle.svg",
        "desc": "Hợp nhất Brain & DeepMind, kiến trúc Native Multimodal chạy trên hạ tầng TPU tự chủ.",
        "badge": "Native Multimodal"
    },
    {
        "date": "02-05/2024",
        "title": "Cửa sổ Ngữ cảnh 1M-2M Token",
        "product": "Gemini 1.5 Pro & Flash",
        "icon": "gemini-sparkle.svg",
        "desc": "Phá vỡ giới hạn RAG với MoE và độ truy hồi >99.7% Needle-In-A-Haystack.",
        "badge": "10x Value"
    },
    {
        "date": "09/2024",
        "title": "Audio Overview Pivot",
        "product": "NotebookLM",
        "icon": "notebooklm-icon.svg",
        "desc": "Biến kho tài liệu tĩnh thành podcast thảo luận 2 chiều có kiểm chứng nguồn nghiêm ngặt.",
        "badge": "Vertical AI"
    },
    {
        "date": "12/2024",
        "title": "Native Agentic Era",
        "product": "Gemini 2.0 & Deep Research",
        "icon": "gemini-sparkle.svg",
        "desc": "Multimodal Live API thời gian thực và Deep Research tác tử tự động duyệt web đa bước.",
        "badge": "Autonomous Agent"
    },
    {
        "date": "05-08/2026",
        "title": "Flash Cadence Strategy",
        "product": "Gemini 3.5-3.8 Flash",
        "icon": "gemini-sparkle.svg",
        "desc": "4 mô hình trong 106 ngày; giảm chi phí 5x ($2.36 vs $11.84) và năng lượng 33x.",
        "badge": "Unit Economics"
    },
    {
        "date": "09/2026",
        "title": "Gemini 4 Argon & 1M Output",
        "product": "Gemini 4 Argon",
        "icon": "gemini-sparkle.svg",
        "desc": "Trần xuất 1M token; chuyển đổi 800k dòng Zircon OS sang Rust; phòng thủ an ninh mạng.",
        "badge": "Frontier Agent"
    }
]

def generate_html_timeline(milestones=None, output_path="timeline.html"):
    if milestones is None:
        milestones = DEFAULT_MILESTONES

    gemini_sparkle_svg = load_icon_content("gemini-sparkle.svg")
    notebooklm_icon_svg = load_icon_content("notebooklm-icon.svg")
    openai_logo_svg = load_icon_content("openai-logo.svg")

    items_html = []
    for idx, m in enumerate(milestones):
        icon_svg = gemini_sparkle_svg
        if "notebooklm" in m.get("icon", "").lower() or "notebook" in m.get("product", "").lower():
            icon_svg = notebooklm_icon_svg
        elif "openai" in m.get("icon", "").lower() or "openai" in m.get("product", "").lower():
            icon_svg = openai_logo_svg

        align_class = "timeline-left" if idx % 2 == 0 else "timeline-right"

        item = f"""
        <div class="timeline-item {align_class}">
          <div class="timeline-badge-icon">
            {icon_svg}
          </div>
          <div class="timeline-card">
            <div class="timeline-header">
              <span class="timeline-date">{m['date']}</span>
              <span class="timeline-tag">{m.get('badge', '')}</span>
            </div>
            <h3 class="timeline-title">{m['title']}</h3>
            <div class="timeline-product">{m.get('product', '')}</div>
            <p class="timeline-desc">{m['desc']}</p>
          </div>
        </div>
        """
        items_html.append(item)

    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gemini Ecosystem Timeline & Strategic Decisions</title>
  <style>
    :root {{
      --bg: #0B0F19;
      --card-bg: rgba(22, 27, 46, 0.85);
      --card-border: rgba(99, 130, 246, 0.25);
      --primary: #4F87ED;
      --accent-purple: #9476C5;
      --accent-coral: #D6645D;
      --text: #F1F5F9;
      --text-muted: #94A3B8;
      --font: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: radial-gradient(circle at 50% 0%, #172038 0%, var(--bg) 75%);
      color: var(--text);
      font-family: var(--font);
      min-height: 100vh;
      padding: 40px 20px;
    }}
    .timeline-container {{
      max-width: 1000px;
      margin: 0 auto;
      position: relative;
    }}
    .timeline-header-main {{
      text-align: center;
      margin-bottom: 50px;
    }}
    .timeline-header-main h1 {{
      font-size: 2.2rem;
      background: linear-gradient(135deg, #439DDF, #4F87ED, #9476C5, #D6645D);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 12px;
    }}
    .timeline-header-main p {{
      color: var(--text-muted);
      font-size: 1.05rem;
    }}
    .timeline {{
      position: relative;
      padding: 20px 0;
    }}
    .timeline::before {{
      content: '';
      position: absolute;
      left: 50%;
      top: 0;
      bottom: 0;
      width: 3px;
      background: linear-gradient(180deg, #4F87ED, #9476C5, #D6645D);
      transform: translateX(-50%);
    }}
    .timeline-item {{
      position: relative;
      width: 50%;
      margin-bottom: 40px;
    }}
    .timeline-left {{
      left: 0;
      padding-right: 45px;
    }}
    .timeline-right {{
      left: 50%;
      padding-left: 45px;
    }}
    .timeline-badge-icon {{
      position: absolute;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #111827;
      border: 2px solid var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      top: 15px;
      z-index: 2;
      box-shadow: 0 0 15px rgba(79, 135, 237, 0.4);
    }}
    .timeline-left .timeline-badge-icon {{
      right: -22px;
    }}
    .timeline-right .timeline-badge-icon {{
      left: -22px;
    }}
    .timeline-badge-icon svg {{
      width: 24px;
      height: 24px;
    }}
    .timeline-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 20px;
      backdrop-filter: blur(10px);
      box-shadow: 0 10px 25px rgba(0,0,0,0.3);
      transition: transform 0.2s ease, border-color 0.2s ease;
    }}
    .timeline-card:hover {{
      transform: translateY(-3px);
      border-color: rgba(148, 118, 197, 0.6);
    }}
    .timeline-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }}
    .timeline-date {{
      font-weight: 700;
      font-size: 0.9rem;
      color: #38BDF8;
      letter-spacing: 0.5px;
    }}
    .timeline-tag {{
      font-size: 0.75rem;
      padding: 3px 8px;
      border-radius: 9999px;
      background: rgba(79, 135, 237, 0.2);
      border: 1px solid rgba(79, 135, 237, 0.4);
      color: #93C5FD;
      font-weight: 600;
    }}
    .timeline-title {{
      font-size: 1.2rem;
      margin-bottom: 4px;
      color: #F8FAFC;
    }}
    .timeline-product {{
      font-size: 0.85rem;
      color: #A855F7;
      font-weight: 500;
      margin-bottom: 10px;
    }}
    .timeline-desc {{
      font-size: 0.92rem;
      line-height: 1.5;
      color: var(--text-muted);
    }}
    @media (max-width: 768px) {{
      .timeline::before {{ left: 24px; }}
      .timeline-item {{ width: 100%; left: 0 !important; padding-left: 60px !important; padding-right: 0 !important; }}
      .timeline-left .timeline-badge-icon, .timeline-right .timeline-badge-icon {{ left: 2px; }}
    }}
  </style>
</head>
<body>
  <div class="timeline-container">
    <div class="timeline-header-main">
      <h1>Hành Trình & Quyết Định Chiến Lược Cốt Lõi</h1>
      <p>Reverse-engineering các cột mốc tạo nên thành công của hệ sinh thái Google Gemini & Vertical AI</p>
    </div>
    <div class="timeline">
      {"".join(items_html)}
    </div>
  </div>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Generated timeline HTML: {output_path}")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "timeline.html"
    generate_html_timeline(DEFAULT_MILESTONES, out)

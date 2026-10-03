#!/usr/bin/env python3
"""
HTML Infographic Report Builder
Builds or updates index.html with interactive Chart.js charts and infographic summary cards.
"""

import os
import sys
import shutil
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = SKILL_ROOT / "resources" / "template_index.html"

def generate_report(output_file: str = "index.html"):
    output_path = Path(output_file).resolve()
    if not TEMPLATE_PATH.exists():
        print(f"❌ Error: Template not found at {TEMPLATE_PATH}")
        sys.exit(1)
        
    shutil.copy(TEMPLATE_PATH, output_path)
    print(f"✅ Generated interactive report page: {output_path}")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    generate_report(out)

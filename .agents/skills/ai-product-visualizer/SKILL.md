---
name: ai-product-visualizer
description: >-
  Tạo các hình ảnh biểu đồ, infographic timeline history và sơ đồ kiến trúc cho các sản phẩm AI
  (Google Gemini, NotebookLM, OpenAI ChatGPT/GPT-4, Claude). Đi kèm bộ icon vector SVG chuẩn xác
  của Google Gemini, NotebookLM, OpenAI để nhúng vào báo cáo web và infographic.
---

# AI Product Visualizer

Skill chuyên dụng để thiết kế, vẽ biểu đồ, infographic lịch sử (timeline history) và kiến trúc sản phẩm AI với bộ nhận diện và icon vector SVG chuẩn xác.

## Tài nguyên Icon Chính thức (`resources/icons/`)

Kèm sẵn các file SVG vector chuẩn xác:
- `gemini-sparkle.svg`: Biểu tượng 4 cánh Google Gemini với gradient chuẩn (`#439DDF` → `#4F87ED` → `#9476C5` → `#BC688E` → `#D6645D`).
- `gemini-full-logo.svg`: Logo Google Gemini hoàn chỉnh kèm biểu tượng lấp lánh và kiểu chữ chính thức.
- `notebooklm-icon.svg`: Biểu tượng vòng xoắn đồng tâm đặc trưng của Google NotebookLM.
- `notebooklm-full-logo.svg`: Logo đầy đủ của Google NotebookLM dạng vector SVG.
- `openai-logo.svg`: Logo vector hình xoắn ốc (spiral/rosette) của OpenAI (`#10A37F`).

## Cách sử dụng

### 1. Tạo Infographic Timeline Lịch sử tự động
Sử dụng script Python đi kèm để sinh file HTML hoặc SVG timeline:
```bash
python3 .agents/skills/ai-product-visualizer/scripts/generate_timeline.py [output_path.html]
```

### 2. Nhúng Icon vào Web/HTML/SVG
Để nhúng icon trực tiếp vào các component HTML hoặc biểu đồ SVG:
```html
<!-- Nhúng inline SVG từ file resources/icons/ -->
<div class="product-badge">
  <img src=".agents/skills/ai-product-visualizer/resources/icons/gemini-sparkle.svg" alt="Gemini" width="24" height="24" />
  <span>Google Gemini</span>
</div>
```

### 3. Tạo Sơ đồ So sánh & Kiến trúc
Khi cần so sánh hệ sinh thái:
- Google Gemini: Nhấn mạnh TPU stack (v5p, v6e Trillium), Native Multimodal, Cửa sổ ngữ cảnh 1M-2M, Trần xuất 1M token (Argon).
- NotebookLM: Nhấn mạnh Source-grounded synthesis, Audio Overview (podcast 2 chiều), Vertical AI.
- OpenAI: Nhấn mạnh reasoning chains (o-series), GPT-4 horizontal wrappers.

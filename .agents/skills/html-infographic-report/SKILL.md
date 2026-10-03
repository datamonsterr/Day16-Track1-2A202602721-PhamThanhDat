---
name: html-infographic-report
description: >-
  Xây dựng trang báo cáo trực quan index.html bằng HTML, JS (Chart.js), CSS hiện đại với các biểu đồ
  (radar năng lực, bar so sánh chi phí $/task, line xu hướng), các thẻ KPI infographic và sơ đồ hào kinh tế.
---

# HTML Infographic Report

Skill chuyên tạo và cập nhật trang web báo cáo `index.html` của dự án, trực quan hóa kết quả nghiên cứu và reverse engineering bằng HTML, CSS (Google AI Glassmorphism Theme) và Chart.js.

## Tính năng

1. **Biểu đồ Tương tác Đa chiều (Chart.js)**:
   - **Cost Comparison Bar Chart**: Chi phí phục vụ các tác vụ lập trình (SWE-bench / coding tasks) giữa các mô hình.
   - **Radar Matrix**: Năng lực toàn diện (Context 2M, Output 1M, Multimodal, Latency, Unit Economics, Coding).
2. **Infographic KPI Cards**:
   - Thẻ số liệu nổi bật: Context window 2M, Output token 1M, Mức giảm tiêu thụ năng lượng 33x, Chi phí $2.36/task.
3. **Sơ đồ So sánh Chiến lược**:
   - Hào kinh tế đa tầng (Silicon TPU, Dữ liệu độc quyền, Phân phối 2B+ users, Bánh đà Dogfooding) đối chiếu với AI Wrapper.

## Cách sử dụng

### 1. Tạo hoặc Khởi tạo file `index.html` cho dự án:
```bash
python3 .agents/skills/html-infographic-report/scripts/build_report.py [path_to_index.html]
```
Mặc định nếu không truyền tham số sẽ tạo ngay `index.html` tại thư mục hiện tại.

### 2. Tùy biến Nội dung & Biểu đồ:
Chỉnh sửa dữ liệu trực tiếp trong `index.html` hoặc trong template `resources/template_index.html`:
- Cập nhật mảng `data` trong các đối tượng Chart.js.
- Cập nhật các thẻ `.kpi-card` với số liệu mới từ các báo cáo chuyên sâu.

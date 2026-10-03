---
name: fact-check-url-validator
description: >-
  Tra cứu mạng xác thực thông tin (fact-check), kiểm tra tính hợp lệ của các liên kết (URL validation),
  và tự động thực hiện quy trình tìm lại URL chính xác khi liên kết trả về lỗi 404 (Wayback Machine archive,
  slug site search, domain mapping).
---

# Fact-Check & URL Validator

Skill hỗ trợ kiểm chứng tính xác thực của dữ liệu/luận điểm trong nghiên cứu và xử lý triệt để bài toán liên kết chết (broken/404 links).

## Khi nào kích hoạt

- Cần tra cứu mạng (search_web, read_url_content) để đối chiếu thông số kỹ thuật, mốc thời gian, số liệu benchmark.
- Cần rà soát toàn bộ link trong báo cáo/tài liệu (ví dụ file `GEMINI_DEEP_RESEARCH_REPORT.md` hoặc các tài liệu Markdown khác).
- Gặp link trả về 404 Not Found và cần tìm link chính thức thay thế.

## Quy trình Kiểm chứng Thông tin (Fact-Checking Workflow)

1. **Xác định Nguồn Sơ Cấp (Primary Sources)**:
   - Nghiên cứu học thuật: Luôn ưu tiên arXiv, ACM Digital Library, Google Research publications.
   - Sản phẩm công nghệ: Ưu tiên Official Blog của Google DeepMind, OpenAI, Anthropic, tài liệu kỹ thuật của Google Cloud/TPU.
   - Benchmark: Tra cứu trực tiếp bảng xếp hạng gốc (ví dụ DeepSWE, CWE-bench, Terminal-bench).

2. **Cross-Examination**:
   - Đối chiếu số liệu chi phí ($/token, MMLU score, context size) từ ít nhất 2 nguồn độc lập trước khi kết luận.

## Quy trình Khôi phục URL bị 404 (404 Recovery Protocol)

Khi một URL trả về mã lỗi 404:

```text
[URL trả về 404]
       │
       ├──> 1. Truy vấn Wayback Machine API:
       │       https://archive.org/wayback/available?url=<URL>
       │       Nếu có bản snapshot -> trích xuất nội dung hoặc link archive.
       │
       ├──> 2. Phân tách Slug & Từ khóa tiêu đề:
       │       Tách domain và path: e.g. blog.google/gemini-1-5-pro
       │       Chạy tìm kiếm với: site:<domain> "<keywords>"
       │
       ├──> 3. Kiểm tra thay đổi cấu trúc URL (URL Pattern Migration):
       │       Google DeepMind: /blog/article -> /discover/blog/article
       │       ArXiv: /abs/XXXX.XXXXX -> /pdf/XXXX.XXXXX.pdf
       │
       └──> 4. Tìm kiếm Nguồn Thay thế (Alternative Canonical Source):
               Nếu trang gốc bị gỡ vĩnh viễn, tìm bài phân tích tương đương trên
               các nền tảng lưu trữ uy tín hoặc bản tin tổng hợp chính thức.
```

## Sử dụng Script Hỗ trợ

Chạy kiểm tra tự động tất cả liên kết trong file:
```bash
python3 .agents/skills/fact-check-url-validator/scripts/validate_urls.py <path_to_file.md>
```
Hoặc kiểm tra một URL đơn lẻ:
```bash
python3 .agents/skills/fact-check-url-validator/scripts/validate_urls.py "https://example.com/some-page"
```
Script sẽ tự động:
- Kiểm tra HTTP Status (200, 301, 302, 404, 500).
- Nếu 404: Tự động truy vấn Wayback Machine Availability API.
- Tạo sẵn gợi ý query tìm kiếm cứu hộ (`site:domain ...`).

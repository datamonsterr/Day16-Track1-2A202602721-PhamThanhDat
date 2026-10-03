---
name: natural-doc-writer
description: >-
  Viết tài liệu kỹ thuật, nghiên cứu reverse-engineering và phân tích sản phẩm tự nhiên, rõ ràng,
  sâu sắc, không dùng sáo rỗng AI. Tuyệt đối tuân thủ và bảo tồn 100% template, cấu trúc mục, bảng biểu
  có sẵn mà không tự ý sửa đổi khung mẫu.
---

# Natural Doc Writer

Skill viết tài liệu kỹ thuật, tài liệu nghiên cứu ca sử dụng (use cases), và bóc tách đảo ngược (reverse-engineering) các quyết định sản phẩm AI mang tính bước ngoặt.

## Nguyên tắc Tối thượng (Non-Negotiables)

### 1. Không Sửa Template (Strict Template Preservation)
- **Bảo tồn Tuyệt đối Khung Mẫu**: Giữ nguyên 100% tất cả các tiêu đề mục, thứ tự mục, bảng biểu, cột dữ liệu, chú thích định dạng sẵn có trong template hoặc file ban đầu.
- **Không tự ý thêm/bớt/đổi tên mục lớn**: Điền nội dung chất lượng cao vào đúng các vị trí được chỉ định trong template.
- Nếu người dùng cung cấp mẫu sẵn (Markdown, JSON, Doc outline), chỉ tập trung tối ưu nội dung bên trong mỗi phần, không thay đổi cấu trúc bộ khung.

### 2. Văn phong Tự nhiên, Chuyên sâu (No AI-Fluff)
- **Loại bỏ hoàn toàn sáo rỗng AI**: Không dùng các cụm từ sáo rỗng như: *"Trong kỷ nguyên số phát triển nhanh chóng...", "Không thể phủ nhận rằng...", "Đóng vai trò then chốt trong bức tranh toàn cảnh...", "Như một minh chứng cho..."*.
- **Giọng văn Kỹ sư & Product Leader thực chiến**:
  - Viết trực diện, cô đọng, giàu mật độ thông tin (high information density).
  - Sử dụng thuật ngữ kỹ thuật chính xác: KV-Cache bottleneck, Sparse MoE, Native Multimodal, Hardware-Software Co-design, Scaled Dot-Product Attention, Marginal Cost per Token.
  - Văn phong tiếng Việt mạch lạc, chuyển tải chuẩn xác các khái niệm công nghệ cao mà không gây gượng gạo hay dịch thô.

### 3. Phương pháp Luận Reverse-Engineering Quyết định Sản phẩm
Khi phân tích sự thành bại của sản phẩm AI:
1. **Bối cảnh & Điểm nghẽn Cốt lõi**: Lúc quyết định được đưa ra, giới hạn phần cứng (GPU/TPU memory bandwidth), chi phí tính toán ($/token), hay điểm nghẽn người dùng là gì?
2. **Trade-offs (Đánh đổi)**: Đội ngũ phát triển đã chấp nhận hy sinh điều gì (ví dụ: hoãn ra mắt model Pro cỡ lớn để tập trung tối ưu dòng Flash, hy sinh điểm chuẩn benchmark lý thuyết để đạt chi phí phục vụ đại chúng)?
3. **Đòn bẩy Đột phá (10x Value vs Incremental)**: Cửa sổ ngữ cảnh 1M-2M token giải quyết triệt để rào cản chunking/vector DB như thế nào? Trần xuất 1M token giải phóng tác tử phần mềm tự động ra sao?
4. **Hào Kinh tế Bền vững (Defensive Moat)**: Phân tách rõ ràng giữa ứng dụng dạng vỏ bọc (AI Wrapper) và hệ thống tích hợp dọc tự chủ từ chip (TPU), dữ liệu độc quyền, đến kênh phân phối hàng tỷ người dùng.

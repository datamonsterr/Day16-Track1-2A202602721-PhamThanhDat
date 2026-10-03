---
name: first-principles-product-thinking
description: >-
  Áp dụng tư duy nguyên lý đầu tiên (First Principles Thinking) và Product Sense chuyên sâu để mổ xẻ
  chiến lược sản phẩm AI, bóc tách JTBD, 4 lực đẩy chuyển đổi (Four Forces), kinh tế học đơn vị bán dẫn,
  và xây dựng lập luận vững chắc cho tài liệu phân tích sản phẩm (MEMO.md).
---

# First Principles & Product Thinking Skill

Skill trang bị phương pháp tư duy từ nguyên lý đầu tiên (First Principles) và năng lực cảm thụ sản phẩm (Product Sense) cho các bài toán phân tích chiến lược, reverse-engineering sản phẩm công nghệ cao, đặc biệt tối ưu cho việc hoàn thành tài liệu [MEMO.md](file:///home/dat/dev/vinuni_aia/Day16-Track1-2A202602721-PhamThanhDat/MEMO.md).

## Phương Pháp Luận Cốt Lõi: First Principles Trong AI

Thay vì suy luận bằng cách so sánh tương tự (*Reasoning by Analogy* - "đối thủ làm chatbot thì ta làm chatbot"), skill này buộc ta phải:
1. **Truy về sự thật nền tảng không thể chối cãi**:
   - Định luật phần cứng: Suy luận LLM ngữ cảnh dài bị nghẽn ở băng thông bộ nhớ nạp KV-Cache (Memory Bandwidth Bound), không phải FLOPS.
   - Kinh tế học đơn vị: Search kiếm $0.01/truy vấn. Chi phí AI Overview bắt buộc phải < $0.001, nếu không toàn bộ biên lợi nhuận của Alphabet sẽ sụp đổ.
   - Nhận thức con người: Đọc 50 trang tài liệu tạo ma sát nhận thức lớn; nghe 2 người trao đổi (podcast) là hình thức tiếp nhận thông tin thụ động tự nhiên nhất.
2. **Nghĩ ngược lên để giải thích quyết định của Google**:
   - Tại sao làm TPU? Để xóa bỏ 75% gross margin của Nvidia.
   - Tại sao ra 4 bản Flash trong 106 ngày? Để hạ giá 5x ($2.36) và giảm điện năng 33x trước khi roll out AI Overviews toàn cầu.
   - Tại sao NotebookLM ra Audio Overview? Để biến kho dữ liệu tĩnh thành kênh phân phối tri thức định dạng âm thanh độc quyền có grounding.
   - Tại sao Gemini 4 Argon nâng trần xuất 1M token? Để luồng suy luận của tác tử phần mềm (Autonomous Agent Trajectory) không bị ngắt quãng giữa chừng.

---

## Hướng Dẫn Thực Hiện 4 Phần Của `MEMO.md`

### Step 1: §1 · Timeline Các Cập Nhật Lớn (6–8 cột mốc)
- **Yêu cầu**: Thời điểm · Cập nhật · Context lúc đó · Nguyên lý (kèm link nguồn).
- **Cách tư duy First Principle**:
  - Không liệt kê tính năng bề nổi; hãy chỉ rõ điểm nghẽn kỹ thuật lúc đó là gì (ví dụ: RNN tuần tự không thể train song song -> Transformer giải phóng Self-Attention; Vector DB phân mảnh -> 1M-2M context native MoE; Trần xuất 64k làm đứt code -> 1M output tokens).
  - Cột "Nguyên lý": Gắn với nguyên lý cụ thể: *Tạo dựng giá trị vượt trội 10x, Đồng thiết kế Phần cứng - Phần mềm (Co-design), Đơn vị kinh tế học biên (Unit Economics), Hào kinh tế tích hợp dọc*.
  - Kiểm tra link nguồn: Chạy skill `fact-check-url-validator` để đảm bảo link arXiv, Google Blog không bị lỗi 404.

### Step 2: §2 · Tệp User & JTBD (Early Adopters vs Mainstream)
- **Yêu cầu**: Phân tích đặc điểm, JTBD chính, cách làm trước đó; phân tích dịch chuyển tệp; switching cost map 4 forces.
- **Cách tư duy Product Sense**:
  - **Early Adopters**: Kỹ sư phụ trách monorepo lớn, chuyên gia an ninh mạng (SecOps), nhà nghiên cứu tài chính/học thuật cần trích dẫn chính xác tuyệt đối. JTBD: "Tái cấu trúc 800k dòng code sang Rust an toàn bộ nhớ không cần rà soát thủ công", "Tổng hợp 50 báo cáo nghiên cứu không bị ảo giác".
  - **Tệp Hiện Tại**: Hàng tỷ người dùng Search, người dùng văn phòng Workspace (Docs, Sheets, Gmail). JTBD: "Xử lý hàng trăm email và tóm tắt video cuộc họp 2 tiếng thành các hành động cần làm ngay".
  - **4 Lực Đẩy (Four Forces)**:
    - *Push*: Chi phí API đối thủ đắt đỏ, giới hạn trần xuất 64k token làm đứt mạch agent, RAG truyền thống phức tạp dễ lỗi.
    - *Pull*: Cửa sổ 2M context + trần 1M output của Argon, tích hợp tự nhiên vào Drive/Docs/Gmail, podcast NotebookLM, giá rẻ nhờ TPU.
    - *Anxiety*: Lo ngại vendor lock-in vào Google Cloud, lịch sử khai tử sản phẩm của Google, kiểm duyệt nội dung gắt gao.
    - *Inertia*: Thói quen dùng ChatGPT đã thành quán tính, pipeline vector DB đã đầu tư chưa khấu hao hết.

### Step 3: §3 · Ba Dự Đoán Hướng Đi (6–12 Tháng Tới)
- **Yêu cầu**: 3 dự đoán cụ thể, mỗi dự đoán có phân loại và lập luận dẫn ngược về §1 và §2.
- **Cách tư duy**:
  - Dự đoán 1 (*Mô hình kiếm tiền / Bán dẫn*): Google cung cấp gói subscription "Agent Infrastructure as a Service" trên Vertex AI với giá token cache rẻ hơn 95%, ép các nhà cung cấp GPU đám mây rời vào cuộc chiến tiêu hao biên lợi nhuận (dẫn từ §1 cột mốc TPU v6e & Flash unit economics).
  - Dự đoán 2 (*Mở rộng tính năng / Tác tử doanh nghiệp*): Tác tử tự hành chuyển đổi mã nguồn toàn diện (Legacy Migration Agent) của Gemini 4 Argon được đóng gói thành sản phẩm thương mại cho các ngân hàng và tập đoàn tài chính để thay thế hệ thống COBOL/C kế thừa sang Rust (dẫn từ §1 trần xuất 1M token và §2 JTBD của Enterprise Engineer).
  - Dự đoán 3 (*Trải nghiệm tri thức / Vertical AI*): NotebookLM mở rộng Audio Overview thành nền tảng đàm thoại tương tác 2 chiều thời gian thực (Real-time Interactive Voice Agent) thay vì podcast thụ động (dẫn từ §1 Multimodal Live API và §2 JTBD tiêu thụ tri thức không độ trễ).

### Step 4: §4 · AI Log
- **Yêu cầu**: Bảng khai báo: Việc gì AI làm, việc gì bạn phán đoán/kiểm chứng lại thế nào.
- **Cách thực hiện**:
  - Tận dụng log tự động từ file `.ai_log` do Antigravity hook ghi lại.
  - Khai báo minh bạch: AI trích xuất mốc thời gian, đối chiếu số liệu benchmark; người phân tích phán đoán nguyên nhân sâu xa (First Principle reasoning), đánh giá tính khả thi kinh tế của TPU và kiểm chứng tính hợp lệ của link nguồn bằng công cụ fact-check.

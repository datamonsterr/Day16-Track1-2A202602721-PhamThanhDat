# Memo Teardown — Google Gemini

**Họ tên:** Phạm Thành Đạt (2A202602721)

**Vì sao chọn sản phẩm này:** Google Gemini đại diện cho bài toán chuyển dịch sản phẩm AI phức tạp nhất lịch sử công nghệ — từ một gã khổng lồ nghiên cứu học thuật bị đe dọa trực tiếp mô hình kinh doanh cốt lõi (Search) đến việc tái cấu trúc toàn diện chuỗi giá trị tích hợp dọc (từ bán dẫn TPU, mô hình nền tảng, đến phân phối 2 tỷ người dùng). Phân tích Gemini giúp bóc tách rõ nét kinh tế học đơn vị ($/token), lợi thế hào phòng thủ và năng lực mở khóa giá trị 10x của AI biên.

**§1. Timeline các cập nhật lớn**

| Thời điểm | Cập nhật | Context lúc đó | Nguyên lý |
|---|---|---|---|
| **06/2017** | **Khởi nguyên kiến trúc Transformer** ([Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)) | NLP toàn cầu bế tắc vì mạng tuần tự LSTM/RNN; OpenAI là lab phi lợi nhuận nhỏ tập trung RL game. | **Tính toán ma trận song song & đường truyền $O(1)$:** Giải phóng giới hạn tính tuần tự, tối ưu năng lực phần cứng GPU/TPU và bảo toàn liên kết ngữ nghĩa tầm xa. |
| **10/2018** | **Mô hình BERT & Đưa vào Google Search** ([Devlin et al., 2018](https://arxiv.org/abs/1810.04805)) | OpenAI ra GPT-1 & GPT-2 (Decoder-only); tranh luận Encoder vs Decoder; Google Search cần hiểu truy vấn tự nhiên dài. | **Bảo vệ giá trị kinh tế cốt lõi:** Thay vì bán API rời, đưa BERT vào Search gia cố dòng tiền quảng cáo 175B USD; hiểu ý định truy vấn cần biểu diễn 2 chiều (Bi-directional). |
| **12/2023** | **Gemini 1.0 & Siêu máy tính Cloud TPU v5p** ([Pichai & Hassabis, 2023](https://blog.google/innovation-and-ai/technology/ai/google-gemini-ai/)) | Hậu "Code Red", ChatGPT gây sốt toàn cầu; Nvidia khan hiếm GPU H100 với biên lợi nhuận >75%; Google hợp nhất Brain + DeepMind. | **Nhận thức thế giới bản địa & Tự chủ chuỗi bán dẫn:** Huấn luyện Native Multimodal tránh nghẽn ghép nối; tự chủ chip TPU v5p tối ưu chi phí biên ($/token) không phụ thuộc Nvidia. |
| **02–05/2024** | **Cửa sổ ngữ cảnh 1M–2M token (Gemini 1.5 Pro & Flash)** ([Gemini Team, 2024](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf)) | OpenAI tung Sora và GPT-4o; Claude 3 vượt GPT-4; Google gặp khủng hoảng PR tạo ảnh; cần giảm chi phí phục vụ hàng tỷ lượt tìm kiếm. | **Giá trị đột phá 10x & Sparse MoE:** Nhảy vọt ngữ cảnh x15 lần triệt tiêu nhu cầu chunking/RAG vector phức tạp; kiến trúc MoE kết hợp HBM của TPU giữ chi phí suy luận siêu rẻ. |
| **09/2024** | **NotebookLM Audio Overview** ([Google Blog, 2024](https://blog.google/innovation-and-ai/products/notebooklm-audio-overviews/)) | Claude 3.5 Sonnet dẫn đầu coding; OpenAI ra mắt o1 (Test-time compute); người dùng mệt mỏi vì ảo giác chatbot chung chung. | **Ràng buộc miền tri thức & Giảm tải nhận thức:** Triệt tiêu ảo giác bằng giới hạn tri thức đóng (Source-grounded); chuyển văn bản dài thành hội thoại âm thanh podcast hợp tâm lý tiếp nhận. |
| **12/2024** | **Gemini 2.0 Flash & Deep Research (TPU v6e)** ([Hassabis, 2024](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/google-gemini-ai-update-december-2024/)) | Anthropic ra Claude Computer Use; OpenAI hé lộ Operator; ngành chuyển từ chatbot giao tiếp sang tác tử hành động tự chủ. | **Triệt tiêu độ trễ tích lũy & Hào dữ liệu độc quyền:** Multimodal I/O thời gian thực loại bỏ độ trễ chuỗi STT-LLM-TTS; Deep Research kết nối trực tiếp Google Search Index để vượt mặt các AI wrapper. |
| **05–08/2026** | **Chiến lược Nhịp độ Flash Liên tục (4 bản trong 106 ngày)** ([Value Add VC, 2026](https://valueaddvc.com/pulse/google-gemini-flash-cadence-no-frontier-model-2026)) | "Cú sốc DeepSeek" nén chi phí; trung tâm dữ liệu chạm trần điện lưới; Scaling Law suy giảm hiệu suất biên; phán quyết chống độc quyền DOJ. | **Kinh tế học đơn vị ($/token) quy mô lớn:** Tạm hoãn flagship 3.5 Pro; dồn lực dòng Flash hạ chi phí xuống 2,36 USD/task (giảm 33x điện năng) để bảo toàn biên lợi nhuận cho AI Overviews. |
| **09/2026** | **Trần đầu ra 1M token & Gemini 4 Argon** ([Google DeepMind, 2026](https://deepmind.google/models/gemini/)) | Tác tử đối thủ bị kẹt ở trần 64k token làm đứt gãy luồng xử lý; tấn công mạng zero-day tự động gia tăng; doanh nghiệp tắc nghẽn legacy code. | **Bảo toàn chân trời suy luận dài hạn (Reasoning Horizon):** Đầu ra 1M token giữ nguyên vẹn đồ thị logic monorepo (chuyển đổi 800k dòng C/C++ sang Rust); TPU quản lý KV Cache phân tán; dogfooding giải phóng >300 TiB bộ nhớ. |

**Vì sao chọn những mốc này:** 8 mốc thời gian trên phản ánh trọn vẹn sự dịch chuyển cấu trúc từ nền móng kiến trúc vi mô (Transformer, BERT) đến tự chủ hạ tầng bán dẫn (TPU v5p/v6e), đột phá giá trị 10x về không gian ngữ cảnh (1.5 Pro, Argon 1M Output), và chuyển hướng sống còn sang kinh tế học đơn vị ($/token). Các mốc thử nghiệm mang tính phản ứng ngắn hạn như Google Bard (03/2023), mô hình phụ trợ nhỏ (Gemini 1.5 Flash-8B), hoặc các cập nhật giao diện nhỏ được loại bỏ vì không làm thay đổi bản chất ngăn xếp công nghệ hay chiến lược cạnh tranh dài hạn của Google.

**§2. Tệp user & JTBD**

| | Early adopters | Tệp hiện tại |
|---|---|---|
| Đặc điểm | | |
| JTBD chính | | |
| Trước đó họ làm bằng cách nào | | |

**Dịch chuyển tệp:** cột mốc nào ở §1 gây ra sự dịch chuyển? Tại sao?

**Switching cost (map 4 forces):** điều gì giữ user ở lại? Lực nào đang kéo họ đi / giữ họ lại?

**§3. Ba dự đoán hướng đi (6–12 tháng tới)**

**Dự đoán 1** *(loại: mở rộng tính năng / segment / mô hình kiếm tiền / đe dọa Big Tech)*
- **Dự đoán:** …
- **Lập luận:** … *(dẫn ngược về §1–§2)*

**Dự đoán 2** *(loại: …)*
- **Dự đoán:** …
- **Lập luận:** …

**Dự đoán 3** *(loại: …)*
- **Dự đoán:** …
- **Lập luận:** …

**§4. AI Log**

| Việc | AI làm hay bạn làm? | Bạn kiểm chứng/phán đoán lại thế nào? |
|---|---|---|
| | | |
| | | |


# 🚀 NLP & Generative AI Lab Series

Chào mừng đến với kho lưu trữ các bài thực hành về Xử lý ngôn ngữ tự nhiên (NLP) và Mô hình ngôn ngữ lớn (LLM). Repository này ghi lại lộ trình xây dựng mô hình ngôn ngữ từ sơ khai (N-gram) đến hiện đại (Fine-tuning).

## 📌 Tổng quan lộ trình (Roadmap)

| Lab | Thư mục | Chủ đề chính | Kỹ thuật / Tech Stack | Trạng thái |
| :---: | :--- | :--- | :--- | :---: |
| **01** | [📂 lab1_processing](./lab1_processing) | **Python & Data Processing** | `Python`, `NumPy`, `Regex`, Text Cleaning | ✅ |
| **02** | [📂 lab2_bigram_language](./lab2_bigram_language) | **Statistical NLP** | `Bigram Model`, `Tokenization`, Probability | ✅ |
| **03** | [📂 lab3_Inference_model](./lab3_Inference_model) | **Model Inference** | `Transformers`, `HuggingFace`, Text Generation | 🚧 |
| **04** | [📂 lab4_finetune_model](./lab4_finetune_model) | **LLM Fine-tuning** | `PEFT`, `LoRA`, `Fine-tuning`, `PyTorch` | 🚧 |

---

## 📖 Chi tiết các bài Lab

### 🔹 Week 1: Python Practice & Preprocessing
* **Mục tiêu:** Ôn tập kỹ năng lập trình Python và xử lý dữ liệu văn bản thô.
* **Nội dung:**
    * Làm sạch dữ liệu (Data Cleaning).
    * Chuẩn hóa văn bản (Normalization).
    * Xây dựng bộ từ điển (Vocabulary building).

### 🔹 Week 2: Bigram Language Model
* **Mục tiêu:** Hiểu cơ chế dự đoán từ dựa trên xác suất thống kê.
* **Nội dung:**
    * Xây dựng mô hình Bigram từ đầu (from scratch).
    * Tính toán xác suất xuất hiện của chuỗi từ.
    * Sinh văn bản ngẫu nhiên dựa trên phân phối xác suất.

### 🔹 Week 3: Model Inference (Suy luận)
* **Mục tiêu:** Sử dụng các mô hình đã huấn luyện để sinh văn bản.
* **Nội dung:**
    * Load pre-trained models.
    * Thực hiện các chiến lược giải mã (Decoding strategies): Greedy, Beam Search.

### 🔹 Week 4: Finetune Model
* **Mục tiêu:** Tinh chỉnh mô hình ngôn ngữ cho tác vụ cụ thể.
* **Nội dung:**
    * Chuẩn bị dữ liệu cho Fine-tuning.
    * Huấn luyện lại (Retrain) mô hình trên tập dữ liệu mới.
    * Đánh giá hiệu suất sau khi tinh chỉnh.

---


<div align="center">
  <img src="https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1200&auto=format&fit=crop" alt="AI NLP Banner" style="border-radius: 10px; width: 100%; max-height: 300px; object-fit: cover;">
  
  <h1 style="font-size: 3em; margin-top: 20px;">🧠 NLP & Generative AI Lab Series</h1>
  
  <p style="font-size: 1.2em; color: #8b949e;">
    Hành trình xây dựng Large Language Models (LLMs): Từ N-gram cơ bản đến Fine-tuning hiện đại.
  </p>

<p>
    <img src="https://img.shields.io/badge/Language-Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Framework-PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
    <img src="https://img.shields.io/badge/Library-HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="HuggingFace" />
    <img src="https://img.shields.io/badge/Tool-Jupyter_Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter" />
    <img src="https://img.shields.io/badge/Focus-NLP_&_LLMs-4B8BBE?style=for-the-badge&logo=openai&logoColor=white" alt="NLP" />
  </p>
</div>

---

## 📌 Tổng quan lộ trình (Roadmap)

| Lab | Thư mục | Chủ đề chính | Kỹ thuật / Tech Stack | Trạng thái |
| :---: | :--- | :--- | :--- | :---: |
| **01** | [📂 lab1_processing](./lab1_processing) | **Python & Data Processing** | `Python`, `NumPy`, `Regex`, Text Cleaning | ✅ |
| **02** | [📂 lab2_bigram_language](./lab2_bigram_language) | **Statistical NLP** | `Bigram Model`, `Tokenization`, Probability | ✅ |
| **03** | [📂 lab3_Inference_model](./lab3_Inference_model) | **Model Inference** | `Transformers`, `HuggingFace`, Text Generation | ✅ |
| **04** | [📂 lab4_finetune_model](./lab4_finetune_model) | **LLM Fine-tuning** | `PEFT`, `LoRA`, `Fine-tuning`, `PyTorch` | 🚧 |

---

## 📚 Tài liệu học tập (Course Materials)

Các tài liệu lý thuyết, bài tập bổ trợ và hướng dẫn thực hành được lưu trữ trong thư mục `material`.

| Loại | Tên Tài liệu / Thư mục | Mô tả nội dung | Link truy cập |
| :---: | :--- | :--- | :---: |
| 📂 | **Language Model Theory** | Các tài liệu lý thuyết về mô hình ngôn ngữ | [Truy cập](./material/LanguageModel) |
| 📂 | **Text Classifier** | Tài liệu và code mẫu về phân loại văn bản | [Truy cập](./material/Classifier) |
| 📓 | **Stanford HF Tutorial** | Hướng dẫn sử dụng HuggingFace từ Stanford | [Xem Notebook](./material/Stanford_Hugging_Face_Tutorial.ipynb) |
| 📓 | **Chapter 6 Problems** | Bài tập thực hành chương 6 | [Xem Notebook](./material/Chapter_6_Problems.ipynb) |

---

## 📖 Chi tiết các bài Lab

### 🔹 Week 1: Python Practice & Preprocessing
* **Mục tiêu:** Ôn tập kỹ năng lập trình Python và xử lý dữ liệu văn bản thô.
* **Nhiệm vụ chính:**
    * Làm sạch dữ liệu (Data Cleaning): Loại bỏ ký tự đặc biệt, HTML tags.
    * Chuẩn hóa văn bản (Normalization) và tách từ (Tokenization).

### 🔹 Week 2: Bigram Language Model
* **Mục tiêu:** Hiểu cơ chế "dự đoán từ tiếp theo" (Next token prediction).
* **Nhiệm vụ chính:**
    * Xây dựng mô hình thống kê Bigram từ con số 0 (from scratch).
    * Tính toán ma trận xác suất và sinh văn bản ngẫu nhiên.

### 🔹 Week 3: Model Inference (Suy luận)
* **Mục tiêu:** Sử dụng các mô hình Pre-trained hiện đại để sinh văn bản.
* **Nhiệm vụ chính:**
    * Tải mô hình (Load Model & Tokenizer).
    * Thực hiện các chiến lược giải mã: Inference tasks and comparision with model in Hugging Face

### 🔹 Week 4: Finetune Model (Fine-tuning)
* **Mục tiêu:** Tùy chỉnh mô hình ngôn ngữ lớn vào một tác vụ cụ thể.
* **Nhiệm vụ chính:**
    * Chuẩn bị dữ liệu dạng Instruction (Input/Output).
    * Cấu hình tham số huấn luyện (Hyperparameters) dùng PEFT/LoRA.

---

## 🛠️ Cài đặt môi trường (Installation)

```bash
# 1. Clone repository về máy
git clone [https://github.com/USERNAME/Lab1-NLP-UIT.git](https://github.com/USERNAME/Lab1-NLP-UIT.git)

# 2. Di chuyển vào thư mục
cd Lab1-NLP-UIT

# 3. Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```


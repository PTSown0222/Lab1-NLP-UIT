import gradio as gr
# Tạo Gradio interface
demo = gr.Interface(
    fn=predict_vietnamese_text,
    inputs=gr.Textbox(lines=3, placeholder="Nhập văn bản tiếng Việt..."),
    outputs=gr.Textbox(label="Kết quả phân loại"),
    title="PhoBERT Vietnamese Text Classification",
    description="Inference model PhoBERT trên dataset UIT-VSMC",
    examples=[
        ["Sản phẩm này rất tuyệt vời!"],
        ["Chất lượng tạm được."],
        ["Tôi không hài lòng với dịch vụ."]
    ]
)

demo.launch(share=True)  # share=True để tạo public link
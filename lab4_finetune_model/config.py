# -----------------------------
# Configuration
# -----------------------------

class Config:
    # Base model
    model_name = ""

    # I/O
    dataset_path = "/content/dataset/train"
    output_dir = "./qwen_legal_lora_sft"

    # Sequence & batching
    max_seq_length = 1024          # raise if VRAM allows; 1024 if tight
    per_device_train_batch_size = 2
    gradient_accumulation_steps = 4

    # Steps / schedule
    max_steps = 70                # quick run; raise for better quality
    warmup_ratio = 0.06
    learning_rate = 2e-4
    weight_decay = 0.01
    lr_scheduler_type = "cosine"
    logging_steps = 10
    max_grad_norm = 0.3
    seed = 3407

    # Precision
    fp16 = not torch.cuda.is_bf16_supported()
    bf16 = torch.cuda.is_bf16_supported()

    # Data split
    test_size = 0.1

    # LoRA
    lora_r = 32
    lora_alpha = 16
    lora_dropout = 0.05
    target_modules = [
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj"
    ]

    # Optimizer (bitsandbytes)
    optim = "adamw_bnb_8bit"

random.seed(Config.seed)
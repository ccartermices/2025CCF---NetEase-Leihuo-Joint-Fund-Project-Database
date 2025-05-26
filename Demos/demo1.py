from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "/workspace/LLaMA-Factory/saves/Qwen3-4B-Base/lora/train_2025-05-25-03-15-17/output/Qwen3-4B-NPC-cp2000"

# 加载模型和分词器
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_path)

# 生成文本（修正后的部分）
prompt = "uuid:d4512cbd-6200-4408-882f-a7979a70c244,question:你是学生吗？"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)  # 添加return_tensors参数
outputs = model.generate(**inputs, max_new_tokens=1024)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("模型回复：", response)
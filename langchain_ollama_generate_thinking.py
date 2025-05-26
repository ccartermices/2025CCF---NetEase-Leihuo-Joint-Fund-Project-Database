from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM
import json

# 加载文档并提取所有对话内容
with open("persona_dialogues_test_100.json", "r") as f:
    all_data = json.load(f)

# 提取第一个场景的所有对话内容
first_scene = list(all_data[0].values())[0]  # 获取第一个随机ID对应的对话数组
combined_content = "\n".join(
    [f"{msg['role']}: {msg['content']}" for msg in first_scene if msg["content"]]
)

print(len(combined_content))
print("\n")

# 设置提示（保持原样）
prompt = """根据人设对话，生成一个“问题-推理过程-最终答案”，要求：
1. 问题需涉及人物关系、隐藏设定或矛盾细节
2. 格式要求，必须严格按顺序包含：[question]不超过15字的问题[/question][cot]2-3句推理过程，不要分点[/cot][answer]10字内简短答案[/answer]
3. 禁止事项:不要反问，不要用markdown，不要分点
4. 示例：[question]戒指材质与残缺手指的关系?[/question][cot]角色设定提到佩戴钛合金戒指，残缺部位是无名指，推测为掩盖伤痕[/cot][answer]掩盖手指残缺并增强近战攻击力[/answer]"""

print(f"prompt:{prompt}\n")

# 分割文本
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
docs = text_splitter.split_text(combined_content)

# 初始化模型并生成回答
llm = OllamaLLM(model="deepseek-r1:32b")
context = docs[0] if docs else ""

print(len(context))
print("\n")

response = llm.invoke(
    f"基于以下对话记录分析人设：\n{context}\n\n生成要求：{prompt}"
)
print("生成的QCA三元组：\n" + response)
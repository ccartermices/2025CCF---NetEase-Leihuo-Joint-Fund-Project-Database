import requests
import json
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM
import json

# 加载JSON数据
with open('persona_dialogues_test_100.json', 'r', encoding='utf-8') as f:
    all_data = json.load(f)

def process_query(user_input):
    # 解析用户输入
    uuid = user_input.get('uuid', '')
    question = user_input.get('question', '')
    
    # 查找对应的对话数据
    selected_conversation = None
    for item in all_data:
        if uuid in item:
            selected_conversation = item[uuid]
            break
    
    if not selected_conversation:
        return {"response": "未找到对应的对话数据"}
    
    # 提取对话内容
    dialogue_parts = []
    for entry in selected_conversation:
        if isinstance(entry, dict) and 'role' in entry and 'content' in entry:
            dialogue_parts.append(f"{entry['role']}: {entry['content']}")
    
    # 处理文本分割
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    docs = text_splitter.split_text('\n'.join(dialogue_parts))
    
    # 调用模型生成回答
    llm = OllamaLLM(model="qwq:32b")
    context = docs[0] if docs else ""
    prompt = f"基于以下对话内容：\n{context}\n你扮演对话中的user角色，最终的问答要尽可能简单，在10个字以内\n问题：{question}"
    
    return {
        "response": llm.invoke(prompt).strip()
    }

# 示例使用
if __name__ == "__main__":
    # 模拟用户输入
    user_input = {
        "uuid": "d4512cbd-6200-4408-882f-a7979a70c244",
        "question": "你是学生吗？"
    }
    
    # 处理请求
    result = process_query(user_input)
    print(json.dumps(result, ensure_ascii=False, indent=2))
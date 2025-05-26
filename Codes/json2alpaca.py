import json
import time
from typing import List, Dict

def convert_to_alpaca(input_path: str, output_path: str, external_ref: str = "external/input.json"):
    """
    将嵌套JSON转换为Alpaca格式，支持q1-q10的QA对提取
    参数：
    - input_path: 输入JSON文件路径
    - output_path: 输出JSONL文件路径
    - external_ref: 外部引用路径模板
    """
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    alpaca_entries = []
    
    # 用于显示进度
    count_item = 0

    for item in data:

        start_time_item = time.time() 

        item_id = next(iter(item.keys()))
        dialogues = item[item_id]
        
        # 提取所有包含QA对的部分
        qa_sections = [elem for elem in dialogues if any(key.startswith('q') for key in elem)]
        
        for qa in qa_sections:
            # 遍历q1到q10
            for i in range(1, 11):
                q_key = f"q{i}"
                cot_key = f"cot{i}"
                a_key = f"a{i}"
                
                # 检查字段是否存在
                if q_key in qa and cot_key in qa and a_key in qa:
                    entry = {
                        "instruction": qa[q_key],
                        "input": f"{external_ref}@{item_id}",
                        "output": f"<think>{qa[cot_key]}</think>{qa[a_key]}"
                    }
                    alpaca_entries.append(entry)

        end_time_item = time.time()
        execution_time_item = end_time_item - start_time_item
        print(f"一次循环执行时间: {execution_time_item:.4f} 秒") 
        count_item = count_item+1
        print(f"进度：{count_item}/100\n")
    
    # 写入JSONL文件
    print("-------------------------\n保存更新后的数据")
    with open(output_path, 'w', encoding='utf-8') as f:
        for entry in alpaca_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

if __name__ == "__main__":

    # 记录开始时间
    start_time = time.time()

    convert_to_alpaca(
        input_path="input.json",
        output_path="alpaca_data.jsonl",
        external_ref="external/source.json"
    )
    
    # 记录结束时间
    end_time = time.time()
    # 计算并打印运行时间（单位：秒）
    execution_time = end_time - start_time
    print(f"代码执行时间: {execution_time:.4f} 秒")
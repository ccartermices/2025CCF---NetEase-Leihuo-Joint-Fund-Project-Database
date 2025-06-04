# 2025CCF-网易雷火联合基金课题数据库（由于保密需求，具体什么课题不给出）

回收课题相关数据，请注意文件中的readme和各目录要求：

code：存放项目源代码，按功能或模块组织，需安装依赖确保运行。

demo：提供样例数据和示例结果，含演示脚本与配置，可以速览项目功能。

model：存放训练好的模型文件，使用时要确保正确加载。

readme：即当前目录，项目文档说明，如运行指南、使用手册，使用前建议详读。

## Methods

首先基于json文件中的背景资料生成对应的问题。由于需要保密，不能通过api连接大语言模型进行推理，因此通过本地部署deepseek-R1 32b或14b生成对应的数据-答案对。对于每个样本，生成了10个。之后，将每个样本的10个问题答案对附加到json文件中。之后基于json文件形成alpaca格式的微调数据集

利用llama factory微调Qwen3-4B和DeepseekR1-7B，获得相应的lora模型。其中，前者用的lora，后者用的是qlora。

## usage

### Quick Start

直接在自己的机器上的命令行输入：

```
curl -X POST http://xxxxxxxx/ask
\ -H "Content-Type: application/json"
\ -d '{ "uuid": "xxxxxxxxxxxxxxx", "question": "你是学生吗？" }'
```

其中，post地址请联系管理员获取

### Other usages

demo文件夹中有很多demo的脚本，全部都可以独立使用。其中demo_{模型名}是快速测试，demo_rag是利用langchain技术连接ollama和json文件（出于保密本仓库不给出）进行问答。先下载models文件夹中的模型，之后直接修改demo中的路径并运行代码：

`python demo_qwen3-4b-NPC.py`

即可。

或者先下载ollama，之后拉取所需的模型，这里推荐qwen3:14b和qwen2.5:14b，然后把设置json文件的路径，之后运行：

`python demo_rag.py`

## mMdels
模型下载地址如下（后续会不断更新，也可以直接用Models文件夹中的文件下载）：
| 模型名称 | 下载链接 | 类型 | 备注 |
|----------|----------|------|------|
| Qwen3-4B-NPC | [下载](https://modelscope.cn/models/ccArtermices/Qwen3-4B-NPC) | 问答模型 | 微调Qwen3-4B获得（lora） |
| DeepseekR1-7B-NPC | [下载](https://modelscope.cn/models/ccArtermices/DeepseekR1-7B-NPC) | 问答模型 | 微调DeepseekR1-7B获得（qlora） |

## Future work

- [] Webui

- [] API调用

全自动模型下载和运行程序

## 同时针对课题详细情况，提醒您​

1、预计5月底回收课题结果，请您提前准备，比赛结果实时评测，评测频率分为两个阶段，5月24日前，每周评测1-2次，5月24-5月底，每2天评测1次。

2、数据回收阶段，请各位老师提供Github账号，并将课题结果上传至github，我们将通过Github进行结果回收

3、Fork后请维护私有仓库，并邀请账号【Lac-bit】 加入仓库，后续我们将拉取最新提交的结果更新榜单成绩。

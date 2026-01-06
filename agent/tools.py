from llm import client


tools = [
    {
        "name": "get_score_by_name",
        "description": "根据名字获取评分",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "名字"
                }
            },
            "required": ["name"]
        }
    },
    {
        "name": "generating_performance_reviews",
        "description": "根据评价生成评价",
        "parameters": {
            "type": "object",
            "properties": {
                "estimation": {
                    "type": "string",
                    "description": "员工的简单评价"
                }
            },
            "required": ["estimation"]
        },
    },
]


def get_score_by_name(name):
    if name == "李华":
        return "name: 李华 绩效评分: 85.9"
    elif name == "王小明":
        return "name: 王小明 绩效评分: 90.1"
    else:
        return "未查到此人"


def generating_performance_reviews(estimation):
    completion = client.chat.completions.create(
        model="glm-4.6",
        messages=[
            {"role": "system", "content": "你是一个评分系统，你需要根据 estimation 生成评价"},
            {"role": "user", "content": estimation}
        ]
    )

    return completion.choices[0].message.content
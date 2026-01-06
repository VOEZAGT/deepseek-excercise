import json
from llm import client
from prompt import REACT_PROMPT
from tools import get_score_by_name,generating_performance_reviews,tools
import re


def send_message(message):
    res = client.chat.completions.create(
        model="glm-4.6",
        messages=message,
    )
    return res


if __name__ == "__main__":
    instruction = "你是一个员工绩效评价系统"

    query = "请比较李华和王小明的绩效谁好？并给绩效好的员工一个赞扬的绩效评价，给绩效差一点的员工一个鼓励的绩效评价"

    prompt = REACT_PROMPT.replace("{tools}", json.dumps(tools)).replace("{input}", query)
    messages = [{"role": "user", "content": prompt}]

    while True:
        response = send_message(messages)
        response_text = response.choices[0].message.content
        print("大模型的回复：")
        print(response_text)

        final_answer_match = re.search(r'Final Answer:\s*(.*)', response_text)
        if final_answer_match:
            final_answer = final_answer_match.group(1)
            print("最终答案:", final_answer)
            break
        messages.append(response.choices[0].message)

        action_match = re.search(r'Action:\s*(\w+)', response_text)
        action_input_match = re.search(r'Action Input:\s*({.*?}|".*?")', response_text, re.DOTALL)

        if action_match and action_input_match:
            tool_name = action_match.group(1)
            params = json.loads(action_input_match.group(1))

            observation = ""
            if tool_name == "get_score_by_name":
                observation = get_score_by_name(params["name"])
                print("人类的回复：Observation:", observation)
            elif tool_name == "generating_performance_reviews":
                observation = generating_performance_reviews(params["estimation"])
                print("人类的回复：Observation:", observation)
            messages.append({"role": "tool", "content": observation})


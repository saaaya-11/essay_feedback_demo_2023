import openai
from .mySet import setVal
GPT_KEY=setVal.GPT_KEY

def reviewEssay(prompts):
    if setVal.IS_EXPERIMENT:
        output=["日本語力のフィードバック","論理性のフィードバック","内容のフィードバック"]
        return output
    msg=[]
    for prompt in prompts:
        chat=[{"role":"system", "content":setVal.REVIEW_SYSTEM}]
        chat.append({"role":"user", "content":prompt})
        openai.api_key=GPT_KEY
        response=openai.ChatCompletion.create(
                model=setVal.GPT_MODEL, messages=chat
            )
        msg.append(response["choices"][0]["message"]["content"].lstrip().replace('\n','<br>'))
    return msg
def createPrompt(input_text,essay_theme):
    #prompt_system=setVal.GPT_SYSTEM
    prompt_essay=[]
    for vp in setVal.VIEWPOINTS:
        prompt_essay.append(
            f"""
            #小論文テーマ:{essay_theme}
            #入力小論文:{input_text}
            #評価観点:{vp}
            #フィードバック:
            """
        )
    return prompt_essay
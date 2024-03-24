import openai
from .mySet import setVal
GPT_KEY=setVal.GPT_KEY
def get_reply(chatlog,essay,theme,feedback):
    chatlist=chat2list(chatlog,essay,theme,feedback)
    openai.api_key=GPT_KEY
    response=openai.ChatCompletion.create(
            model=setVal.GPT_MODEL, messages=chatlist
        )
    msg=response["choices"][0]["message"]["content"].lstrip().replace('\n','<br>')
    return msg

def chat2list(chatlog,essay,theme,feedback):
    system_prompt=setVal.CHAT_SYSTEM+"\n#小論文テーマ"+theme+"\n#小論文:"+essay+"\n#フィードバック:"+feedback
    chatlist=[{"role":"system", "content":system_prompt}]
    for sp,msg in chatlog:
        if sp=="gpt":
            chatlist.append({"role":"assistant", "content":msg})
        elif sp=="user":
            chatlist.append({"role":"user", "content":msg})
    return chatlist
def chat2html(chatlog):
    htmltext=""
    for sp,msg in chatlog:
        if sp=="gpt":
            htmltext+=f'<div class="msg_incoming"><div class="msg_image"><img src="/static/img/loading_bot.gif" alt="sunil"></div><div class="msg_received"><div class="msg_received_withd"><p>{msg}</p></div></div></div>\n'
        elif sp=="user":
            htmltext+=f'<div class="msg_outgoing"><div class="msg_sent"><p>{msg}</p></div></div>\n'
    return htmltext
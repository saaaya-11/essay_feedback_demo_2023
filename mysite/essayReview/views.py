from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .form import essayForm
from .reviewAI import reviewEssay, createPrompt
from .chat import chat2html,get_reply
import csv

class EssayReviewView(View):
    def get(self, request):
        return render(request, "essayReview/essay_review.html")
    def post(self, request):
        if "input_text" in request.POST:
            print("review")
            essay_theme=request.POST["essay_theme"]
            input_text=request.POST["input_text"]
            if input_text:
                prompt_essay=createPrompt(input_text=input_text,essay_theme=essay_theme)
                responses=reviewEssay(prompt_essay)
                response_html=f"<h3> 日本語力 </h3><p> {responses[0]} </p><h3> 論理性・一貫性 </h3><p> {responses[1]} </p><h3> 内容 </h3><p> {responses[2]} </p>"
                log_init=["gpt", "小論文についてなんでも聞いてください！"]
                with open("essayReview/chat_log.csv", 'w') as f:
                    writer=csv.writer(f)
                    writer.writerow(log_init)
                with open("essayReview/essay_info.csv", 'w') as f:
                    writer=csv.writer(f)
                    writer.writerow([str(input_text).replace('\n',''),essay_theme,response_html])
                    """
                    f.write(input_text.replace('\n',''))
                    f.write("\n")
                    f.write(essay_theme.replace('\n',''))
                    f.write("\n")
                    f.writelines(response_html.replace('\n',''))
                    f.write("\n")
                    """
                context={'input_text':input_text, 'essay_theme':essay_theme, 'response':response_html, 'chat_history':chat2html([log_init])}
                return render(request, "essayReview/essay_review.html", context)
            else:
                return render(request, "essayReview/essay_review.html")
        elif "btn_message" in request.POST:
            message=request.POST["input_msg"]
            if message:
                
                with open("essayReview/chat_log.csv", 'r') as f:
                    reader=csv.reader(f)
                    chat_log=[row for row in reader]
                chat_log.append(["user",message])
                with open("essayReview/essay_info.csv", 'r') as f:
                    reader=csv.reader(f)
                    input_text,essay_theme, response=[row for row in reader][0]
                    #input_text,essay_theme, response=f.readlines()
                chat_reply=get_reply(chat_log,input_text,essay_theme,response)
                chat_log.append(["gpt",chat_reply])
                with open("essayReview/chat_log.csv", 'a') as f:
                    writer=csv.writer(f)
                    writer.writerow(["user",message])
                    writer.writerow(["gpt", chat_reply])
                context={'input_text':input_text, 'essay_theme':essay_theme, 'response':response, 'chat_history':chat2html(chat_log)}
                return render(request, "essayReview/essay_review.html", context)
            else:
                return render(request, "essayReview/essay_review.html")
        else:
            return render(request, "essayReview/essay_review.html")

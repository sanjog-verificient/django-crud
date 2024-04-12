from django.shortcuts import render
from django.http import HttpResponse
import random

words = [
    "python",
    "django",
    "ruby",
    "english",
    "Response",
    "template",
]
msg = ""  
def rword():
      global jword
      global word
      word = random.choice(words)
      jum = random.sample(word, len(word))
      jword = "".join(jum)



def homepage(request):
    rword()
    global jword, word
    return render(request,'index.html',{'jum_word': jword})


def checkans(request):
     global word,jword,msg
     user_answer = request.GET['answer']
     if user_answer == word:
          msg = "That was correct"
          homepage(request)
     else:
          msg = "Try again"
     return render(request,'index.html',{'jum_word': jword,'msg':msg})
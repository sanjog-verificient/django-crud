from django.http import HttpResponse



def home(request):
    link_html = "<a href='https://www.youtube.com/watch?v=-qUoCBExAvY&list=PL-51WBLyFTg1pUMaTJ4WSgnyvWfLGmwDm'>Watch the video</a>"
    return HttpResponse("this is a link :"+link_html)
from django.shortcuts import render
from news.models import News


def home(request):
    context = {"news_list": News.objects.all()}
    return render(request, "home.html", context)

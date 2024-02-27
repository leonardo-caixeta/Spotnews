from django.shortcuts import get_object_or_404, render
from news.models import News


def home(request):
    context = {"news_list": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    categories = news.categories.all()
    return render(
        request, "news_details.html", {"news": news, "categories": categories}
    )

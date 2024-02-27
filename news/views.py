from django.shortcuts import get_object_or_404, redirect, render
from news.forms import CreateCategoryForm
from news.models import Category, News


def home(request):
    context = {"news_list": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    categories = news.categories.all()
    return render(
        request, "news_details.html", {"news": news, "categories": categories}
    )


def categories(request):
    if request.method == "POST":
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            Category.objects.create(name=name)
            return redirect('home-page')
    else:
        form = CreateCategoryForm()
        return render(request, "categories_form.html", {"form": form})

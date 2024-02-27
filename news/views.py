from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from news.forms import CreateCategoryForm, CreateNewsForm
from news.models import Category, News, User


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
            return redirect("home-page")
    else:
        form = CreateCategoryForm()
        return render(request, "categories_form.html", {"form": form})


def news_form(request):
    if request.method == 'POST':
        form = CreateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            news = News.objects.create(
                title=cleaned_data['title'],
                content=cleaned_data['content'],
                author=cleaned_data['author'],
                created_at=cleaned_data['created_at'],
                image=cleaned_data['image']
            )
            for category in cleaned_data['categories']:
                news.categories.add(category)
            return redirect('home-page')
        else:
            return HttpResponse("O formulário inválido", status=400)
    else:
        form = CreateNewsForm()
        users = User.objects.all()
        categories = Category.objects.all()
        return render(request, 'news_form.html', {
            'form': form,
            'users': users,
            'categories': categories
        })

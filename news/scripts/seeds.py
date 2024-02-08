try:
    from news.models import Category
except ModuleNotFoundError:
    Category = None

try:
    from news.models import User
except ModuleNotFoundError:
    User = None

try:
    from news.models import News
except ModuleNotFoundError:
    News = None
from news.scripts.data import authors, categories, news


def create_users(user_model):
    for author in authors:
        user_model.objects.create(
            name=author["name"],
            email=author["email"],
            password=author["password"],
            role=author["role"],
        )


def create_categories(category_model):
    for category in categories:
        category_model.objects.create(name=category["name"])


def create_news(news_model, category_model, user_model):
    for new in news:
        n = news_model.objects.create(
            title=new["title"],
            content=new["content"],
            author=user_model.objects.get(name=new["author"]),
            created_at=new["created_at"],
            image=new["image"],
        )
        category = category_model.objects.get(name=new["category"])
        n.categories.add(category)


def run():
    if Category is not None and not Category.objects.all():
        create_categories(Category)
        print("Categories created successfully!")

    if User is not None and not User.objects.all():
        create_users(User)
        print("Users created successfully!")

    if (
        (User is not None and User.objects.all())
        and (Category is not None and Category.objects.all())
        and (News is not None and not News.objects.all())
    ):
        create_news(News, Category, User)
        print("News created successfully!")

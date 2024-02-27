from django.urls import path
from .views import categories, home, news_details, news_form

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name='news-details-page'),
    path("categories", categories, name="categories-form"),
    path("news", news_form, name="news-form")
]

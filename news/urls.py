from django.urls import path
from .views import categories, home, news_details

urlpatterns = [
    path("", home, name="home-page"),
    path('news/<int:id>', news_details, name='news-details-page'),
    path("categories", categories, name="categories-form")
]

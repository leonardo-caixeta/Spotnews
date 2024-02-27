from django.urls import path
from .views import home, news_details

urlpatterns = [
    path("", home, name="home-page"),
    path('news/<int:id>', news_details, name='news-details-page'),
]

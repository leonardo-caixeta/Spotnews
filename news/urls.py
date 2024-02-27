from django.urls import include, path
from .views import categories, home, news_details, news_form
from .views import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name='news-details-page'),
    path("categories", categories, name="categories-form"),
    path("news", news_form, name="news-form"),
    path("api/", include(router.urls)),
]

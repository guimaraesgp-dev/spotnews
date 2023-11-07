from django.urls import path
from news.views import home, news_details


urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:new_id>", news_details, name="news-details-page"),
]

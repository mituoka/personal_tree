from django.urls import path
from .views import home,github,qiita,youtube,twitter,hobby,portfolio

urlpatterns = [
    path('', home.main_func, name="home"),
    path('github', github.main_func, name="github"),
    path('qiita', qiita.main_func, name="qiita"),
    path('youtube', youtube.main_func, name="youtube"),
    path('twitter', twitter.main_func, name="twitter"),
    path('hobby', hobby.main_func, name="hobby"),
    path('portfolio', portfolio.main_func, name="portfolio"),    
]
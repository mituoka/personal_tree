from django.urls import path
from .views import home,github,qiita,design,portfolio

urlpatterns = [
    path('', home.main_func, name="home"),
    path('github', github.main_func, name="github"),
    path('qiita', qiita.main_func, name="qiita"),
    path('design', design.main_func, name="design"),
    path('portfolio', portfolio.main_func, name="portfolio"),    
]
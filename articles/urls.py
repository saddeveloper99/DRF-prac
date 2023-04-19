from django.urls import path, include
from articles import views

urlpatterns = [
    path('', views.aritcleAPI, name='index'),
    path('<int:article_id>/', views.articleDetailAPI, name='article_view'),
]

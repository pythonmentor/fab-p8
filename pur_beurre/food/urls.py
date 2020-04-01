from django.urls import path
from food import views

urlpatterns = [
    path('home', views.home),
    path('article/<id_article>', views.view_article),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.BooksVeiw.as_view()),
]
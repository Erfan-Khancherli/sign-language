from django.urls import path
from word.views import WordsListView , CategoryList , WordsCreate , CategoryCreate


urlpatterns = [
    path('' , WordsListView.as_view()),
    path('create/', WordsCreate.as_view()),
    path('categories/' , CategoryList.as_view()),
    path('categories/create/' ,CategoryCreate.as_view()),
]

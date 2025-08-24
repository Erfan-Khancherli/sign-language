from django.urls import path
from word.views import WordsListView , CategoryList , WordsCreate
# from word.views import CategoryList
urlpatterns = [
    path('' , WordsListView.as_view()),
    path('create/', WordsCreate.as_view()),
    path('categories/' , CategoryList.as_view()),
    # path('words/' , get_1_alphabet.as_view())
]

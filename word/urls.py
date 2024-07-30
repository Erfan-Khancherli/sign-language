from django.urls import path
from word.views import AlphabetListView , AlphabetCreate , CategoryList , get_1_alphabet
urlpatterns = [
    path('' , AlphabetListView.as_view()),
    path('create/', AlphabetCreate.as_view()),
    path('categories/' , CategoryList.as_view()),
    path('alphabets/' , get_1_alphabet.as_view())
]

from django.urls import path
from .views import FavoriteCreate ,FavoriteListView
urlpatterns = [
    path('create/<int:word_id>/' , FavoriteCreate.as_view()),
    path('list/' , FavoriteListView.as_view())
]
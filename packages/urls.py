from django.urls import path
from packages.views import PackageAPIView  ,UserPackageAPIView

urlpatterns = [
    path('update/' , PackageAPIView.as_view()),
    path('create/', PackageAPIView.as_view()),
    path('list/' , PackageAPIView.as_view()),
    path("user-packages/", UserPackageAPIView.as_view()),
]

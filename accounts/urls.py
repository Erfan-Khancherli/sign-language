from django.urls import path
from accounts import views
from .views import RegisterUser , LogoutView , UpdatePassword
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register1/',RegisterUser.as_view()), #for class base view Register
    path('register/',views.createAccount ),    #for function base view Register
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #login enpoint
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # refresh token endpoint
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('change_password/', UpdatePassword.as_view(), name='change_password'),
]
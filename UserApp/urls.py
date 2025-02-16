from .views import AllUsersAPI, UserIdAPI, RegisterAPI, LoginAPI, UpdateUserPasswordAPI
from django.urls import path



urlpatterns = [
    path('all_users/', AllUsersAPI.as_view(), name='all_users'),
    path('user/<int:id>/', UserIdAPI.as_view(), name='user_id'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(),name='login'),
    path('update_password/', UpdateUserPasswordAPI.as_view(),name='UpdatePassword'),
]
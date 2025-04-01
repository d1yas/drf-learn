from .views import AllUsersAPI, UserIdAPI, RegisterAPI, LoginAPI, UpdateUserPasswordAPI,ListUsersAPI, DeleteUserAPI
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/all_users/', AllUsersAPI.as_view(), name='all_users'),
    path('api/user/<int:id>/', UserIdAPI.as_view(), name='user_id'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(),name='login'),
    path('api/update_password/', UpdateUserPasswordAPI.as_view(),name='UpdatePassword'),
    path('api/list_users/', ListUsersAPI.as_view(), name='list_users'),
    path('api/delete/<int:id>', DeleteUserAPI.as_view(), name='delete user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]
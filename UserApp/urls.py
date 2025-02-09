from .views import AllUsersAPI, UserIdAPI
from django.urls import path



urlpatterns = [
    path('all_users/', AllUsersAPI.as_view(), name='all_users'),
    path('user/<int:id>/', UserIdAPI.as_view(), name='user_id'),
]
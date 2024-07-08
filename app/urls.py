from django.urls import path
from .views import UserList, UserDelete, UserUpdate, UserCreate, UserDetail

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('users/create/', UserCreate.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdate.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),
]

from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('', index, name='index'),
    path('', ChatList.as_view(), name = 'chat_list'),
    path('chat/<str:room_name>/', chat, name='room'),
    path('accounts/login/register/',RegisterView.as_view(), name="register"),
    path('new-chat/', ChatCreate.as_view(), name="new-chat")
]

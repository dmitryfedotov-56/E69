from .models import Chat
from .forms import ChatForm
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User


def index(request):
    return render(request, 'chat_app/index.html')


class ChatList(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'chat_list.html'
    context_object_name = 'chats'
    ordering = ['-id']


class ChatCreate(LoginRequiredMixin, CreateView ):
    template_name = 'chat_app/create_chat.html'
    form_class = ChatForm
    success_url = '/'


def chat(request, room_name):
    print(request.user)
    return render(request, 'chat_app/chat.html', {
        'room_name': room_name,
        'user_name': str(request.user),
     })


class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)



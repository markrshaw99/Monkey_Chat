from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *



@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name="public-chat")
    chat_messages = chat_group.chat_messages.all()[:30]  # Get the last 30 messages
    form = ChatMessageCreateForm()
    return render(request, 'a_rtchat/chat.html', {'chat_messages': chat_messages, 'form': form})

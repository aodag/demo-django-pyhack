from django.shortcuts import render
from .models import PyhackEvent
# Create your views here.


def hello(request):
    context = {
        "message": "Hello, world!",
    }
    return render(request, "pyhackregister/hello.html", context)

# イベント一覧
def list_event(request):
    events = PyhackEvent.objects.all()
    context = {
        "events": events,
    }
    return render(request, "pyhackregister/events.html", context)

# イベント詳細
def event_detail(request, id):
    event = PyhackEvent.objects.get(pk=id)
    context = {
        "event": event,
    }
    return render(request, "pyhackregister/event.html", context)
# 登録

from django.urls import path

from .views import hello, list_event, event_detail


urlpatterns = [
    path("hello/", hello),
    path("events/", list_event),
    path("events/<int:id>", event_detail),
]

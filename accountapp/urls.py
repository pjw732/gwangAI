from django.urls import path

from accountapp.views import Hello_world

urlpatterns = [
    path('Hello_world/', Hello_world, name="Hello_world"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.hello, name="simple_hello" ),
    path("brain", views.brain, name="brain"),
    path("baha", views.baha, name="baha"),
    # path("<str:name>", views.greet, name="greet"),
    path("", views.index, name="hello"),
    path("<str:name>", views.greet, name="greet")
]

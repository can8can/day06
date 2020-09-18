from django.urls import path

from api import views

urlpatterns = [
    # path("demo/", views.Demo.as_view()),
    path("demo2/", views.Demo2.as_view()),
]
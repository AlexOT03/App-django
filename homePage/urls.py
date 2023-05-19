from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('home/', views.MyView.as_view(), name="my-view"),
]
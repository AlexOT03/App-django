from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', views.admin.as_view(), name="admin"),
    path('admin/places', views.adminPlaces.as_view(), name="places"),
    path('admin/orders', views.adminOrders.as_view(), name="orders"),
    path('admin/messages', views.adminMessages.as_view(), name="messages"),
]
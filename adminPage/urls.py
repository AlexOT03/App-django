from django.urls import path
from .views import Admin, AdminPlaces, AdminPlacesEdit, AdminOrders, AdminMessages

urlpatterns = [
    path('admin/', Admin.as_view(), name="admin"),

    path('admin/places/', AdminPlaces.as_view(), name="places"),
    path('admin/places/info/<id>/', AdminPlaces.show, name="placeInfo"),
    path('admin/places/delete/<id>/', AdminPlaces.delete, name="placeDelete"),
    path('admin/places/edit/<id>/', AdminPlacesEdit.as_view(), name="placeEdit"),

    path('admin/orders/', AdminOrders.as_view(), name="orders"),

    path('admin/messages/', AdminMessages.as_view(), name="messages"),
    path('admin/messages/info/<id>/', AdminMessages.show, name="messageInfo"),
    path('admin/messages/delete/<id>/', AdminMessages.show, name="messageDelete"),
]
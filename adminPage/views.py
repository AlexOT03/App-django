from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.
class admin(View):
    def get(self, request):
        return render(request, 'indexAdmin.html')

class adminPlaces(View):
    def get(self, request):
        return render(request, 'placesAdmin.html')
    
    def post(self, request, id):
        return redirect('places')

class adminOrders(View):
    def get(self, request):
        return render(request, 'ordersAdmin.html')
    
class adminMessages(View):
    def get(self, request):
        return render(request, 'messagesAdmin.html')
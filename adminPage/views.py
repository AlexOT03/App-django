from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Places, Orders, Message
from .form import PlaceForm, OrderForm, MessageForm

# Create your views here.
class admin(View):
    def get(self, request):
        return render(request, 'indexAdmin.html')

class adminPlaces(View):
    def get(self, request):
        lugares = Places.objects.values()
        form = PlaceForm()
        return render(request, 'placesAdmin.html', {
            'form': form,
            'lugares': lugares
        })

    def post(self, request):
        form = PlaceForm(request.POST)
        if form.is_valid():
            fm = Places()
            fm.name = form.cleaned_data['name']
            fm.location = form.cleaned_data['location']
            fm.owner = form.cleaned_data['owner']
            fm.capacity = form.cleaned_data['capacity']
            fm.price = form.cleaned_data['price']
            fm.description = form.cleaned_data['description']
            fm.save()
        else:
            print("Error")
        return redirect('places')

    def delete(self, request, id):
        place = Places.objects.get(id=id)
        place.delete()
        return redirect('places')

class adminOrders(View):
    def get(self, request):
        return render(request, 'ordersAdmin.html')
    
class adminMessages(View):
    def get(self, request):
        return render(request, 'messagesAdmin.html')
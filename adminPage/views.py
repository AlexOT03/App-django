from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Places, Orders, Message
from .form import PlaceForm, OrderForm, MessageForm

# Create your views here.
class Admin(View):
    def get(self, request):
        place = Places.objects.values().count()
        order = Orders.objects.values().count()
        message = Message.objects.values().count()
        return render(request, 'indexAdmin.html', {
            'num_places': place,
            'num_orders': order,
            'num_messages': message
        })

class AdminPlaces(View):
    def get(self, request):
        lugares = Places.objects.values().order_by('id')
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
    
    def show(request, id):
         place = Places.objects.values().get(id=id)
         return render(request, 'placesInfoAdmin.html', {
             'place': place,
         })
         
    def delete(request, id):
        place = Places.objects.get(id=id)
        place.delete()
        return redirect('places')

class AdminPlacesEdit(View):
    def get(self, request, id):
        place = Places.objects.get(id=id)
        form = PlaceForm(initial={'name':place.name, 'location':place.location, 'owner':place.owner, 'capacity':place.capacity, 'price':place.price, 'description':place.description})
        return render(request, 'placesEditAdmin.html', {
            'form': form,
            'place': place,
        })
    
    def post(self, request, id):
        place = Places.objects.get(id=id)
        form = PlaceForm(request.POST)
        if form.is_valid():
            place.name = request.POST.get('name')
            place.location = request.POST.get('location')
            place.owner = request.POST.get('owner')
            place.capacity = request.POST.get('capacity')
            place.price = request.POST.get('price')
            place.description = request.POST.get('description')
            place.save()
        return redirect('places')

class AdminPlaceDelete(View):
    def get(self, request, id):
        place = Places.objects.get(id=id)
        place.delete()
        return redirect('places')

class AdminOrders(View):
    def get(self, request):
        return render(request, 'ordersAdmin.html')

class AdminMessages(View):
    def get(self, request):
        return render(request, 'messagesAdmin.html')
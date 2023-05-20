from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!, Iam a Client!!!!")
    
def home(request, *args, **kwargs):
    return HttpResponse("Welcome, type in the url '/admin if you want to access a CRUD', or type '/home to access to another string view'")
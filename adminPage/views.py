from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!, Iam Admin!!!!!!!!!!")
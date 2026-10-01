from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


#function based
# def home(request):
#     if(request.method == 'GET'):
#         return HttpResponse("Hello, world. You're the only method available.")
#
# #define index view returns msg "index page"
#
# def Index(request):
#     if(request.method == 'GET'):
#         return HttpResponse("Index Page")

class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to Django")

class Index(View):
    def get(self, request):
        return HttpResponse("Index page")
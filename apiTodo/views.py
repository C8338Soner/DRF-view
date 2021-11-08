from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):
 return HttpResponse('<center><h1 style = "background-color:powderblue; font-size: 5rem; font-weight: bold"> Welcome To The ApiTodo</h1></center>')
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random


def index(request):
    variable = "ram"
    return render(request,'home.html',{'variable' :"shyam"})
def about(request):
    return HttpResponse("Hello, world. You're at the polls about.")
def result(request):
    text = request.POST['text1']


    return render(request,'home.html',{'rand':text} )
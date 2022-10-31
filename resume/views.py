from django.shortcuts import render
from .models import Destination

# Create your views here.
from django.http import HttpResponse
import random


def profile(request):
    dests= Destination.objects.all()



    return render(request,'profile.html',{'dests':dests})
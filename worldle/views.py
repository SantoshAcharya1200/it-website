from django.shortcuts import render, redirect
from .models import Worldle
from django.contrib import messages


# Create your views here.
from django.http import HttpResponse
import random


def worldle(request):
    value= str(request.POST.get('text'))
    values = value.lower()
    world= Worldle.objects.all()
    rand=random.choice(world)
    bcd= rand.title.lower()
    result = ''

    if values == bcd:
        messages.info(request, 'Correct')
        result = 'correct'
    else:
        result='Wrong'


    return render(request,'worldle.html',{'rand':rand,'values':values,'rst':result})
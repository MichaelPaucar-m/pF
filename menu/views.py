from django.shortcuts import render
from .models import Menu

# Create your views here.
def menu (request): 
    menu=Menu.objects.all()#listamos los servicios 
    return render (request, "menu/menu.html", {'menu':menu}) 
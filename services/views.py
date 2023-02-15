from django.shortcuts import render, get_object_or_404
from django.shortcuts import render 
from .models import Services, Category



# Create your views here. 


def services (request): 
    #consultas 
    services= Services.objects.all()
    return render (request, "services/services.html",{'services': services})

#obtener el id y direccion url
def category(request, category_id):
   # pass#hace que no se caiga el programa si esta imcompleto 
   category=get_object_or_404(Category, id=category_id)
   #tomar los blogs que le pertencen a esta categoria 
   services=Services.objects.filter(categories=category)
   return render (request, "services/category.html", {'services': services})
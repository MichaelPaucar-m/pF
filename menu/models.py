from django.db import models

# Create your models here.
class Menu(models.Model): #heredando de la clase modelo que brinda Django
     title= models.CharField(max_length=200, verbose_name="Titulo")
     description=models.TextField(verbose_name="Descripcion")
     image=models.ImageField(verbose_name="Imagen", upload_to="project")
     price=models.CharField(null=True, max_length=200, verbose_name="Precio")
     created=models.DateTimeField(
         auto_now_add=True, verbose_name="Fecha de creacion")
     update=models.DateTimeField(
         auto_now=True, verbose_name="Fecha de actualizacion")

     class Meta:   #Modificaciones extendidas del modelo
         verbose_name = "Menu"
         verbose_name_plural = "Menus"

         ordering = ["-created"]

     def __str__(self):       #retornar en forma de string la informacion del objeto
             return self.title
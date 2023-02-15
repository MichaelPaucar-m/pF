from django.contrib import admin
from .models import Category, Services

# Register your models here. 
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') 

class ServicesAdmin(admin.ModelAdmin):#configuracion extendida
    readonly_fields = ('created','updated') 
    list_display = ('title','author','published')
    ordering = ('author','published')
    search_fields =('title',)
    date_hierarchy ='published'
    list_filter = ('author__username','categories__name') 


admin.site.register(Category, CategoryAdmin)  
admin.site.register(Services, ServicesAdmin) 
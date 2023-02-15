from .models import Link

def ctx_dict(request): 
    ctx={}
    #cargar lalista de redes sociales 
    link=Link.objects.all()
    #agregamos dentro del diccionarion
    for links in link:
        ctx[links.key]= links.url #llenamos el diccionario
    return ctx 
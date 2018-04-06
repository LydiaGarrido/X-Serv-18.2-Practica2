from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

from acorta.models import Urls


FORMULARIO = """
    <form method = 'POST'>
    <b>Introduce URL: </b><br>
    <input type='text' name='url'><br>
    <input type='submit' value='Acortar'></form>
    """


@csrf_exempt
def barra(request):
    lista_urls = Urls.objects.all()
    if request.method == 'GET':
        respuesta = FORMULARIO
        if len(lista_urls) != 0:
            respuesta += "Lista de urls acortadas:"
            for url in lista_urls:
                respuesta += ("<br><b> ·<u>Url larga: </u></b>" + url.url_larga +
                             "<b> /<u> Url acortada: </u></b>" +
                             "<a href=" + "http://localhost:8000/" + str(url.id) +
                             ">" + "http://localhost:8000/" + str(url.id) + "</a>")
        else:
            respuesta += "La lista de urls acortadas está vacía"

    elif request.method == 'POST':
        url_larga = request.POST['url']
        if (url_larga[0:8] != "https://" and url_larga[0:7] != "http://"):
            url_larga = "http://" + url_larga
        try:
            url_acortada = Urls.objects.get(url_larga=url_larga)
        except Urls.DoesNotExist:
            url = Urls(url_larga=url_larga)
            url.save()
            url_acortada = Urls.objects.get(url_larga=url_larga)
        respuesta = ("<a href=" + "http://localhost:8000/" + str(url_acortada.id) +
                     ">" + "http://localhost:8000/" + str(url_acortada.id) + "</a>")
    else:
        respuesta = "Método no permitido"
    return HttpResponse(respuesta)


def redirect(request, url_acortada):
    try:
        url_larga = Urls.objects.get(id=url_acortada).url_larga
        return HttpResponseRedirect(url_larga)
    except Urls.DoesNotExist:
        volver = '<a href="http://localhost:8000">Ir al acortador de urls</a>'
        return HttpResponse("El recurso no está disponible <br>" + volver)


def error(request):
    volver = '<a href="http://localhost:8000">Ir al acortador de urls</a>'
    return HttpResponse("Error producido: url incorrecta <br>" + volver)

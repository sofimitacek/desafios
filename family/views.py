from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from family.models import Familia


def list_familia(self):
    mihtml= open("C:\Users\chofy\OneDrive\Documentos\proyectosAA\familiares\familiares\family\templates\family_list.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

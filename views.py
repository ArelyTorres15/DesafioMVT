from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def mom(request):
    mom=Madre(nombre="Araceli", edad=61, fecha_nac="1961-10-11")
    mom.save()
    texto=f"Madre se llama: nombre: {mom.nombre} edad: {mom.edad} fecha_nac: {mom.fecha_nac}"
    return HttpResponse(texto)

def dad(request):
    dad=Padre(nombre="Alonso", edad=71, fecha_nac="1951-10-2")
    dad.save()
    texto=f"Padre se llama: nombre: {dad.nombre} edad: {dad.edad} fecha_nac: {dad.fecha_nac}"
    return HttpResponse(texto)

def bro(request):
    bro=Hermano(nombre="Orlando", edad=33, fecha_nac="1988-09-25")
    bro.save()
    texto=f"Hermano se llama: nombre: {bro.nombre} edad: {bro.edad} fecha_nac: {bro.fecha_nac}"
    return HttpResponse(texto)

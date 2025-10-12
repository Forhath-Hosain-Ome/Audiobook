from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def HomeView(request : HttpRequest) -> HttpResponse:
    return HttpResponse('Hello')
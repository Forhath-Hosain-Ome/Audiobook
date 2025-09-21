from django.shortcuts import render

def AddView(request):
    return render (request,'pages/index.html')
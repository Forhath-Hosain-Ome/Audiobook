from django.urls import path
from .views import document_detail, home

urlpatterns = [
    path('/details/<pk>', document_detail, name='detail'),
    path('', home, name = 'home')
]

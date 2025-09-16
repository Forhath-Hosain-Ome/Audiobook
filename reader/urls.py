from django.urls import path
from .views import document_detail

urlpatterns = [
    path('', document_detail, name='home'),
]

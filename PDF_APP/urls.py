from django.urls import path
from .views import DocumentListCreate, DocumentDetail

urlpatterns = [
    path('documents/', DocumentListCreate.as_view(), name='document_list_create'),
    path('documents/<int:pk>/', DocumentDetail.as_view(), name='document_detail'),
]
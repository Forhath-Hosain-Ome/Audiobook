from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='document')

urlpatterns = [
    path('', home, name = 'home'),
    path('documents/', document, name='documents'),
    path('document_detail/<pk>', view_document, name='document_detail'),
    path('upload-pdf', upload_document, name='upload_document'),
    path('api/', include(router.urls)),
]
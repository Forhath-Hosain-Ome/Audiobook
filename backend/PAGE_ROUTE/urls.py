from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


# router = DefaultRouter()
# router.register(r'documents', DocumentViewSet, basename='document')

urlpatterns = [
    path('', HomeView, name = 'home'),
    path('view-pdf/', ViewPdf, name='pdf_view'),
    path('view/pk', ViewPdf, name='single_pdf_view'),
    path('upload-pdf', AddPdf, name='upload_pdf'),
    path('edit/', EditPdf, name='edit_pdf'),
    path('delete/', DeletePdf, name='delete_pdf'),
    # path('api/', include(router.urls)),
]
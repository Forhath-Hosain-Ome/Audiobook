from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import HomeView, ViewPdf, AddPdf, EditPdf, DeletePdf


# router = DefaultRouter()
# router.register(r'documents', DocumentViewSet, basename='document')

urlpatterns = [
    path('', HomeView, name = 'home'),
]
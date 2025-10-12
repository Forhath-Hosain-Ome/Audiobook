from django.urls import path
from PAGE_ROUTE.views import HomeView
from . import views

urlpatterns = [
    path('', HomeView, name = 'home'),
    path('protected/', views.protected_view, name='protected'),
    path('public/', views.public_view, name='public'),
    path('encrypt/', views.encrypt_data, name='encrypt'),
    path('decrypt/', views.decrypt_data, name='decrypt'), 
]
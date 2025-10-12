from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from PAGE_ROUTE.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name = 'home'),
    # path('', include('PAGE_ROUTE.urls')),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
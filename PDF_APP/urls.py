from django.urls import path
from .views import DocumentListCreate, DocumentDetails
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("api/pdf/", DocumentListCreate.as_view(), name="book-list"),
    path("api/pdf/<int:pk>/", DocumentDetails.as_view(), name="book-detail"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
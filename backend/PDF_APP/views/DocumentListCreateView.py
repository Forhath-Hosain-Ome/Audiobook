from PDF_APP.models import PdfModel
from rest_framework import generics, permissions
from PDF_APP.serializer import DocumentSerializer

class DocumentListCreate(generics.ListCreateAPIView):
    queryset = PdfModel.objects.all()
    serializer_class = DocumentSerializer
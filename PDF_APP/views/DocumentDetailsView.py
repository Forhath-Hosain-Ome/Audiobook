from PDF_APP.models import PdfModel
from rest_framework import generics, permissions
from PDF_APP.serializer import DocumentSerializer


class DocumentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PdfModel.objects.all()
    serializer_class = DocumentSerializer
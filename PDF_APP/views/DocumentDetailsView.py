from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from reader.models import Document
from reader.serializer import DocumentSerializer


class DocumentDetails(APIView):
    def get(self, request, pk):
        doc = get_object_or_404(Document, pk=pk)
        serializer = DocumentSerializer(doc)
        return Response(serializer.data)

    def put(self, request, pk):  # full update
        doc = get_object_or_404(Document, pk=pk)
        serializer = DocumentSerializer(doc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):  # partial update
        doc = get_object_or_404(Document, pk=pk)
        serializer = DocumentSerializer(doc, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

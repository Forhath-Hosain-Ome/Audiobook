from django.shortcuts import render, get_object_or_404
from reader.models import Document


def document_detail(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    return render(request, "reader/detail.html", {"doc": doc})

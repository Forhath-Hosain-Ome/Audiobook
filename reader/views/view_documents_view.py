from django.shortcuts import render, get_object_or_404
from reader.models import Document


def view_document(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    return render(request, "reader/detail.html", {"doc": doc})

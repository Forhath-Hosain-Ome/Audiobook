from django.shortcuts import render, get_object_or_404
from reader.models import Document


def document(request):
    doc = Document.objects.all()
    context = {
        'documents': doc
    }
    return render(request, "reader/detail.html", context)

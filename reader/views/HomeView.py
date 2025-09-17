from django.shortcuts import render, redirect
from reader.forms import DocumentForm
from reader.utils import extract_text_from_pdf, generate_tts_gtts
from django.conf import settings
import os
from django.core.files import File


def home(request):
    return render (request,'pages/index.html')
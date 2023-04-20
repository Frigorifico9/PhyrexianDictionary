from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import * 
from .forms import SearchForm

def index(request):
    return render(request, "words/index.html",)

def word_entry(request, phyrexian_word_str):
    context = {
        "phyrexian_word":PhyrexianWord.objects.get(phyrexian=phyrexian_word_str)
    }
    return render(request, "words/word_entry.html", context) 

def about(request):
    return render(request, "words/about.html")
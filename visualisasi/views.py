from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.middleware.csrf import get_token
import pandas as pd
from nilai import *

# Create your views here.
def index(request):
    token = get_token(request)
    get_all_data()
    context = {
        'csrf_token': token,
    }
    return render(request, 'index.html', context)

def showNilai(request):
    npm = request.POST['npm']
    
    nilai = get_data(npm)
    
    mutu = (nilai['final'])

    context = {
        'nilai': nilai,
        'npm': npm,
        'mutu': huruf_mutu(float(mutu))
    }

    # return HttpResponse(mutu)
    
    return render(request, 'nilai.html', context)
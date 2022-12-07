from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.middleware.csrf import get_token
import pandas as pd

# Create your views here.
def index(request):
    token = get_token(request)
    template = loader.get_template('index.html')
    context = {
        'csrf_token': token,
    }
    return HttpResponse(template.render(context, request))

def showNilai(request):
    npm = request.POST['npm']
    data = pd.read_csv('https://raw.githubusercontent.com/adivii/visualisasi_nilai_files/main/Daftar%20Nilai%20-%20csv-for-web.csv')
    nilai = data[data['npm'] == int(npm)]
    context = {
        'nilai': nilai.reset_index(),
        'npm': npm,
    }

    template = loader.get_template('nilai.html')
    return HttpResponse(template.render(context, request))
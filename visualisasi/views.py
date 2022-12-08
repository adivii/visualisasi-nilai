from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.middleware.csrf import get_token
import pandas as pd

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

    request.session['status'] = 1

    if nilai.empty:
        request.session['status'] = 0
        return redirect('/')
    
    mutu = (nilai['final'])
    context = {
        'nilai': nilai,
        'npm': npm,
        'mutu': huruf_mutu(float(mutu))
    }

    # return HttpResponse(mutu)
    
    return render(request, 'nilai.html', context)

def huruf_mutu(nilai):
    if nilai >= 76:
        return 'A'
    elif 71 <= nilai < 76:
        return 'B+'
    elif 66 <= nilai < 71:
        return 'B'
    elif 61 <= nilai < 66:
        return 'C+'
    elif 56 <= nilai < 61:
        return 'C'
    elif 50 <= nilai < 56:
        return 'D'
    else:
        return 'E'

def get_all_data():
    return pd.read_csv('https://raw.githubusercontent.com/adivii/visualisasi_nilai_files/main/Daftar%20Nilai%20-%20csv-for-web.csv')

def get_data(npm):
    data = pd.read_csv('https://raw.githubusercontent.com/adivii/visualisasi_nilai_files/main/Daftar%20Nilai%20-%20csv-for-web.csv')
    # if int(npm) in data['npm']:
    # else:
    #     return 'error'    
    return data[data['npm'] == int(npm)].reset_index()
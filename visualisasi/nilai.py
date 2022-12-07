import pandas as pd

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
    return data[data['npm'] == int(npm)].reset_index()
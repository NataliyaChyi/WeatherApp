from django.shortcuts import render
import requests

def index(request):
    appid = '8b4995461704791e59ced235a0081d95'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+appid
    city = "Minsk"
    res = requests.get(url.format(city)).json()
    print(res)
    return render(request, 'weather/index.html')

from django.shortcuts import render

# Create your views here.
import urllib.request
import json


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        start_url = 'http://api.weatherapi.com/v1/current.json?key=01911872b9b747c4ba4161947232703&q=' + city + '&lang=es'
        url = start_url.replace(" ","%20")
        source = urllib.request.urlopen(url).read()
        list_data = json.loads(source)

        data = {
            'ciudad': str(list_data['location']['name']),
            'pais': str(list_data['location']['country']),
            'localtime': str(list_data['location']['localtime']),
            'condicion': str(list_data['current']['condition']['text']),
            'temp': str(list_data['current']['temp_c']),
            'humedad': str(list_data['current']['humidity']),
            'viento': str(list_data['current']['wind_kph']),
        }
        print(data)
    else:
        data = {}

    return render(request, 'main/index.html', data)
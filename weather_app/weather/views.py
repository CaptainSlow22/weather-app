from django.shortcuts import render
import json 
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b6b74c0de8a93c133461548c3cc8978a').read()
        json_data = json.loads(res)
        data = {
            "city" : str(json_data['name']),
            "country_code" : str(json_data['sys']['country']),
            "conditions" : str(json_data['weather'][0]['main']),
            "icon" : str(json_data['weather'][0]['icon']),
            "temp" : str(int(json_data['main']['temp'] - 273.15)) + ' ℃',
            "wind_speed" : str(int(json_data['wind']['speed'] * 1.6)) + ' km/h',
            "pressure" : str(json_data['main']['pressure']) + ' mb',
            "humidity" : str(json_data['main']['humidity']) + '%',
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
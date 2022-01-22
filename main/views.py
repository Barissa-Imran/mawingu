from django.shortcuts import render
import requests
from django.contrib import messages

# Index page view


def index(request):
    if request.method == "POST":
        city = request.POST.get('city')

        try:
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=fb25ed3367841cdd09348e1eedc1236c"

            # print(city)

            r = requests.get(url.format(city)).json()

            city_weather = {
                'city': city,
                'country': r['sys']['country'],
                'temperature': r['main']['temp'],
                'weather': r['weather'][0]['description'],
                'icon': r['weather'][0]["icon"],
                'feels_like': r['main']['feels_like'],
                'temp_min': r['main']['temp_min'],
                'temp_max': r['main']['temp_max'],
                'wind': r['wind']['speed'],
                'pressure': r['main']['pressure'],

            }

            context = {
                'city_weather': city_weather,
            }

            return render(request, "main/index.html", context)
        except:
            messages.error(request, "Please try entering a valid city!")
    else:
        pass

    # default weather to be shown on homepage before search
    city = 'Nairobi'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=fb25ed3367841cdd09348e1eedc1236c"

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'country': r['sys']['country'],
        'temperature': r['main']['temp'],
        'weather': r['weather'][0]['description'],
        'icon': r['weather'][0]["icon"],
        'feels_like': r['main']['feels_like'],
        'temp_min': r['main']['temp_min'],
        'temp_max': r['main']['temp_max'],
        'wind': r['wind']['speed'],
        'pressure': r['main']['pressure'],
    }

    context = {
        'city_weather': city_weather,
    }

    return render(request, 'main/index.html', context)


# docs page view
def docs(request):
    return render(request, "main/docs.html")

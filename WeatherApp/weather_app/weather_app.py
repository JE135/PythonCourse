from flask import Flask, render_template
import requests
import datetime as dt

app = Flask(__name__)

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "6016b98473e3474cf49f1d7e7f118070"
CITY = "Helsinki"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

@app.route("/")
def weather():
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']

    timezone_offset = response["timezone"]
    tz = dt.timezone(dt.timedelta(seconds=timezone_offset))

    sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'], tz)
    sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'], tz)

    weather_data = {
        "city": CITY,
        "temp_c": f"{temp_celsius:.2f}",
        "temp_f": f"{temp_fahrenheit:.2f}",
        "feels_c": f"{feels_like_celsius:.2f}",
        "feels_f": f"{feels_like_fahrenheit:.2f}",
        "humidity": humidity,
        "wind": wind_speed,
        "description": description.capitalize(),
        "sunrise": sunrise_time.strftime("%H:%M:%S"),
        "sunset": sunset_time.strftime("%H:%M:%S"),
    }

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)



#http://127.0.0.1:5000 link to browser app
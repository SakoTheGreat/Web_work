from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    weather_city = weather_by_city("Warsaw, Poland")
    title = "Прогноз погоды"
    if weather_city:
        weather_text =  f"Температура {weather_city['temp_C']} градусов, ощущается как {weather_city['FeelsLikeC']}"
    else:
        weather_text =  "Сервис погоды временно не доступен"
    return render_template('index.html', page_title=title, weather=weather_text)

if __name__ == "__main__":
    app.run(debug=True)
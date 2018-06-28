import os
import requests
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'

@app.route('/slack/weather', methods=['POST'])
def weather():
    location = request.form["text"]
    weather = get_weather(location)
    message = 'Its gonna be {weather} in {location}'.format(location=location, weather=weather)
    return jsonify({
        'response_type': 'in_channel',
        'text': message 
    })

def get_weather(location):
    payload = {'q': location, 'APPID': os.environ.get('OPEN_WEATHER_MAP_ACCESS_TOKEN', '0')}
    r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
    return r.json().get('weather')[0].get('main')

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020)))
import os
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'

@app.route('/slack/weather', methods=['POST'])
def weather():
    location = request.args["text"]
    message = 'Its gon rain in {location}'.format(location=location)
    return jsonify({
        'response_type': 'in_channel',
        'text': message 
    })

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020)))
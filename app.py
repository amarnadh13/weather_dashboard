from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        api_key = 'cfe16d47f4c55faea6081c78f2304d06'  # Replace with your API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.ok:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found!'}
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)


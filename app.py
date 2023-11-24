from flask import Flask, render_template, request
from weather import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    
    data = weather(city)
    return render_template('main.html',data=data,action="/get_weather")

if __name__ == '__main__':
    app.run(debug=True)

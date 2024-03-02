# Weather App using WeatherAPI.com API

## Overview
This is a simple Flask application that utilizes the WeatherAPI.com API to fetch current weather information for a given city. The application allows users to input a city name and receive details such as location, temperature (in Fahrenheit and Celsius), and current weather condition.

## Prerequisites
Make sure you have the following installed:

- Python 3
- Flask
- Requests library

You can install the required libraries using the following command:

```bash
pip install flask requests
```

## Usage
1. Clone the repository:

```bash
git clone https://github.com/your-username/weather-app.git
```

2. Navigate to the project directory:

```bash
cd weather-app
```

3. Run the Flask application:

```bash
python app.py
```

4. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

5. Enter the desired city in the input field and click the "Get Weather" button.

## Code Structure

### `app.py`
This file contains the Flask application. It defines two routes: `/` for rendering the main page and `/get_weather` for handling the form submission and displaying weather information.

### `weather.py`
The `weather` function in this file makes a request to the WeatherAPI.com API using the provided API key and the city input. It extracts relevant information such as location, temperature, and weather condition, converts the temperature to Celsius, and returns a list containing this information.

## API Key
Replace the placeholder API key (`4da0e8341db549c0b6c163519231608`) in the `weather.py` file with your WeatherAPI.com API key. You can sign up for a free account on [WeatherAPI.com](https://www.weatherapi.com/) to obtain your API key.

## Acknowledgments
- This application utilizes the WeatherAPI.com API for weather data.

Feel free to customize and extend the application based on your needs. If you have any questions or issues, please [open an issue](https://github.com/your-username/weather-app/issues) on the GitHub repository.

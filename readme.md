# Weather App using weatherapi.com API

This is a simple weather application built with Flask that fetches weather data using the weatherapi.com API. Users can input a city, and the app will display the current weather conditions for that city.

## Getting Started

### Prerequisites

- Python 3
- Flask
- Requests

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/weather-app.git
```

2. Install the required packages:

```bash
pip install flask requests
```

### Running the App

1. Navigate to the project directory:

```bash
cd weather-app
```

2. Run the Flask app:

```bash
python app.py
```

The app will be accessible at `http://localhost:5000/` in your web browser.

## How to Use

1. Access the home page at `http://localhost:5000/`.

2. Enter the desired city in the provided input box.

3. Click the "Get Weather" button to retrieve the current weather conditions for the specified city.

## Live Demo

This weather app is hosted on Render, and you can access it at the following URL:

[https://weatherapp-ijuk.onrender.com/](https://weatherapp-ijuk.onrender.com/)

## Code Structure

The code is organized as follows:

- `app.py`: Flask application containing the routes.
- `weather.py`: Module for fetching weather data from the weatherapi.com API.

## API Used

The app uses the [weatherapi.com](http://www.weatherapi.com/) API to get current weather data.

## Acknowledgments

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- weatherapi.com: [http://www.weatherapi.com/](http://www.weatherapi.com/)

Feel free to explore and modify the code according to your needs.

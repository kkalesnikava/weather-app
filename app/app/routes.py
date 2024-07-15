import os
import requests

from app import app
from flask import jsonify, render_template_string
from urllib.parse import urlencode, urlunparse

API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')
LATITUDE = os.getenv('LATITUDE')
LONGITUDE = os.getenv('LONGITUDE')


# Check for required environment variables
required_env_vars = ['API_URL', 'API_KEY', 'LATITUDE', 'LONGITUDE']

missing_vars = [var for var in required_env_vars if os.getenv(var) is None]
if missing_vars:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(missing_vars)}")


def fetch_remote_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content, response.status_code
    except requests.RequestException as e:
        return jsonify({"error_message": str(e)}), 500


# Routes
@app.route('/')
def index():
    query_params = {
        'lat': LATITUDE,
        'lon': LONGITUDE,
        'appid': API_KEY,
        'mode': 'html'
    }
    url = urlunparse(('', '', API_URL, '', urlencode(query_params), ''))
    remote_data, status_code = fetch_remote_data(url)
    return remote_data, status_code


@app.route('/ping')
def ping():
    return render_template_string('<html><body><h1>Pong</h1></body></html>'), 200


@app.route('/health')
def health():
    response = {
        "message": "HEALTHY"
    }
    return jsonify(response), 200

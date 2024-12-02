import os
from flask import Flask, redirect, request, render_template, jsonify
from requests_oauthlib import OAuth2Session
import pymongo
import plotly
import json
import numpy as np
from dotenv import load_dotenv

from Activity_pstructure.src.main import generate_plots

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Fitbit OAuth 2.0 credentials from the details you provided
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

# Fitbit OAuth 2.0 endpoints
AUTHORIZATION_URL = os.getenv('AUTHORIZATION_URL')
TOKEN_URL = os.getenv('TOKEN_URL')

# Define the required scopes for the OAuth flow
SCOPES = ['activity']

# Create an OAuth2 session
oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPES)

@app.route('/')
def index():
    """Homepage route."""
    return render_template('index.html')  

@app.route('/login')
def login():
    """Redirect user to Fitbit's authorization URL."""
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_URL)
    return redirect(authorization_url)

@app.route('/signin-fitbit')
def signin_fitbit():
    """Handle the redirect from Fitbit after user grants access."""
    # Fetch the access and refresh tokens using the authorization code sent by Fitbit
    token = oauth.fetch_token(TOKEN_URL, authorization_response=request.url,
                              client_secret=CLIENT_SECRET)
    
    # Extract the access and refresh tokens
    access_token = token['access_token']
    refresh_token = token['refresh_token']

    # For security, you can store the tokens in a session or database
    return f"Access token: {access_token}<br>Refresh token: {refresh_token}"

@app.route('/test', methods=['GET'])
def test():
    # Generate plots
    activity_plot_html, diet_plot_html, sleep_plot_html = generate_plots()

    # Render the HTML template with the generated plots
    return render_template('test.html', 
                           activity_plot=activity_plot_html,
                           diet_plot=diet_plot_html,
                           sleep_plot=sleep_plot_html)
if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)


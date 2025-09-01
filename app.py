from flask import Flask
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


import requests
import pandas as pd

def extract_data():
    
    url = "https://zenquotes.io/api/random"

    response = requests.get(url)

    data = response.json()

    quote_author= f'{data[0]["q"]} - {data[0]["a"]}'

    print(quote_author)

extract_data()

    
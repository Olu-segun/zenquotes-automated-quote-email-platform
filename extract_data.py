import requests
from datetime import datetime

def extract_data():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    data = response.json()
    quote = f'{data[0]["q"]} - {data[0]["a"]}'
    return quote

def save_quote():
    quote = extract_data()
    
    filename = f'quote_{datetime.now().strftime("%Y-%m-%d")}.txt'

    with open(filename, "w", encoding="utf-8") as file:
        file.write(quote)
    
    print(f"✅ Quote saved successfully to {filename}")

save_quote()

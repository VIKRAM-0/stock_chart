import os 
import requests
from dotenv import load_dotenv

load_dotenv()

def price (symbol:str,time_series:str):
    '''Input : 
        Symbol : Name of the stock in symbol (EX:IBM,) => string 
        Time series : Duration to get the Data (EX:INTRADAY) => string
    Output:
        Data = Time series data of the stock => csv or json'''
    
    api_key = os.getenv("ALPHAVANTAGE_API_KEY")
    
    try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{time_series}&symbol={symbol}&interval=5min&apikey=demo'
        r = requests.get(url)
        data = r.json()
    except requests.exceptions.RequestException as e:
        print(f"Error While Getting Data : \n{e}")
        return None
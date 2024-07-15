from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_stock_price():
    url = 'https://www.google.com/finance/quote/RELIANCE:NSE?hl=en'
    response = requests.get(url)
    
    if response.status_code != 200:
        return None, f"Failed to load page {url}"
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    price_span = soup.find('div', class_='YMlKec fxKbKc')
    
    if not price_span:
        return None, "Could not find the stock price element on the page"
    
    stock_price = price_span.text
    
    # Remove the ₹ symbol from the stock price
    stock_price = stock_price.replace('\u20b9', '').strip()
    
    return stock_price, None

@app.route('/stock-price', methods=['GET'])
def stock_price():
    price, error = get_stock_price()
    
    if error:
        return jsonify({'error': error}), 500
    
    # Return the stock price as a JSON response
    return jsonify({'stock_price': price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
    # app.run(debug=True)

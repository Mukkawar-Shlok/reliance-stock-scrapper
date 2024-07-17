from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import yfinance as yf
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


@app.route('/reliance_stock_history/<period>/<interval>', methods=['GET'])
def get_reliance_stock_history(period, interval):
    try:
        # Define the stock ticker symbol for Reliance Industries
        ticker_symbol = 'RELIANCE.NS'
        
        # Fetch the stock data using yfinance
        reliance_stock = yf.Ticker(ticker_symbol)
        
        # Get historical market data
        historical_data = reliance_stock.history(period=period, interval=interval)
        
        # Reset the index to make the date a column
        historical_data.reset_index(inplace=True)
        
        # Convert the DataFrame to JSON format
        historical_data_json = historical_data.to_json(orient='records', date_format='iso')
        
        # Return the JSON data with a success message
        return jsonify({"message": "Load successful.", "data": historical_data_json})
    except Exception as e:
        # Return an error message
        return jsonify({"message": str(e)}), 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)
    # app.run(debug=True)

# Valid period values:
# 1d, 5d
# 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y

# Valid interval values:
# 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h
# 1d, 5d
# 1wk, 1mo, 3mo
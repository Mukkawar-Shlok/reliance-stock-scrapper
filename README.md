# Stock Data Flask Application

This Flask application provides endpoints to retrieve historical stock data and real-time stock prices for Reliance Industries using Yahoo Finance and web scraping with BeautifulSoup.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

## Install dependencies:
```bash
pip install Flask requests beautifulsoup4 yfinance
```
or
```bash
pip install -r requirements.txt
```
## Run Flask Application 
```bash
python app.py
```
The application will start running on http://localhost:5000.

## Endpoints
```bash
GET /stock-price
```
Description:
Returns the real-time stock price of Reliance Industries fetched from Google Finance.

```bash
GET /reliance_stock_history/<interval>/<from_date>/<to_date>   
```
Date should be in format %Y-%m-%d.

Description:
Returns historical stock data for Reliance Industries based on the specified period and interval.


## Valid Interval Values:
1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h
1d, 5d
1wk, 1mo, 3mo

# Author
Shlok M Mukkawar

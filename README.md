# Stock Manager

## Overview
This application serves as a basic stock manager. It allows users to manage their balance, buy and sell stocks, and view the current price of stocks.

## Libraries Used
- Flask: A micro web framework written in Python.
- Flask-CORS: A Flask extension for handling Cross-Origin Resource Sharing (CORS).
- Bootstrap: A popular front-end framework for web development.
- Alpha Vantage: Used to fetch real-time stock prices.

## Setup

### 1. Obtain an API Key
To get real-time stock prices, we use the Alpha Vantage API. You need to obtain a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key). 

### 2. Set up the Backend
1. Ensure you have Python installed.
2. Install the necessary libraries using pip:
```bash
pip install Flask Flask-CORS requests
```
3. Clone this repository and navigate to its directory.
4. Update the `ALPHA_VANTAGE_API_KEY` variable in the backend Python script with your API key.
5. Run the Flask application with:

```bash
export FLASK_APP=your_flask_app_name.py
flask run
```
### 3. Access the Frontend
Open the `frontend_with_localstorage.html` file in a web browser. Ensure your Flask backend is running to interact with the stock functionalities.

## Usage
1. Manage your balance using the "Manage Balance" section. Add or remove money to/from your balance.
2. In the "Stock Operations" section, you can buy or sell stocks. Enter the stock symbol (e.g., AAPL for Apple Inc.) and the quantity you want to buy or sell.
3. View your current holdings in the table below, which displays your stock symbols, quantities, current prices, and the total value of each stock.

## Future Improvements
1. Implementing a proper database for more persistent storage.
2. Enhancing error handling and user feedback.
3. Adding more features such as viewing historical stock data or integrating more stock-related functionalities.

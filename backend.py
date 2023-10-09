from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

ALPHA_VANTAGE_API_KEY = "INSERT API KEY"
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
app = Flask(__name__)

# Sample in-memory data storage (just for the sake of this demo)
user_data = {
    "cash_balance": 1000.00,  # default cash balance
    "stocks": {}  # dictionary to hold stock symbols and quantities
}


@app.route('/')
def index():
    return "Stock Manager App is running!"


@app.route('/balance', methods=['GET', 'POST'])
def balance():
    if request.method == 'POST':
        amount = request.json.get('amount')
        action = request.json.get('action')  # can be 'add' or 'remove'
        
        if action == 'add':
            user_data["cash_balance"] += amount
        elif action == 'remove':
            user_data["cash_balance"] -= amount
        
        return jsonify({"message": "Balance updated successfully.", "balance": user_data["cash_balance"]})
    
    return jsonify({"balance": user_data["cash_balance"]})

@app.route('/stock_price/<symbol>', methods=['GET'])
def get_stock_price_endpoint(symbol):
    price = get_stock_price(symbol)
    return jsonify({"price": price})



def get_stock_price(stock_symbol):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": stock_symbol,
        "interval": "1min",
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    
    response = requests.get(ALPHA_VANTAGE_ENDPOINT, params=params)
    data = response.json()

    # Extract the latest stock price. This might need adjustment based on the actual response structure.
    latest_time = list(data["Time Series (1min)"].keys())[0]
    stock_price = float(data["Time Series (1min)"][latest_time]["1. open"])

    return stock_price


@app.route('/stock', methods=['POST'])
def manage_stock():
    stock_symbol = request.json.get('symbol')
    quantity = request.json.get('quantity')
    action = request.json.get('action')  # can be 'buy' or 'sell'
    
    stock_price = get_stock_price(stock_symbol)
    total_cost = stock_price * quantity
    
    if action == 'buy':
        if user_data["cash_balance"] < total_cost:
            return jsonify({"message": "Insufficient funds."}), 400
        
        user_data["cash_balance"] -= total_cost
        user_data["stocks"][stock_symbol] = user_data["stocks"].get(stock_symbol, 0) + quantity
    
    elif action == 'sell':
        if stock_symbol not in user_data["stocks"] or user_data["stocks"][stock_symbol] < quantity:
            return jsonify({"message": "Insufficient stock quantity."}), 400
        
        user_data["cash_balance"] += total_cost
        user_data["stocks"][stock_symbol] -= quantity
        
        if user_data["stocks"][stock_symbol] == 0:
            del user_data["stocks"][stock_symbol]
    
    return jsonify({"message": f"{action.capitalize()} successful.", "balance": user_data["cash_balance"], "stocks": user_data["stocks"]})


# Test the application (for this interactive environment, we're not actually starting the Flask server)
"Flask setup complete."

CORS(app)
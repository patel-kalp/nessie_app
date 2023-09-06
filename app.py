from flask import Flask, make_response, render_template, request
from decouple import config

# Read the API key from the .env file
API_KEY = config('API_KEY')

app = Flask(__name__)

@app.route('/')
def name():
    currentCustomer = request.args.get('customer_name')
    return render_template('home.html', current_tab='Home', currentCustomer=currentCustomer)

@app.route('/atms')
def atms():
    currentCustomer = request.args.get('customer_name')
    return render_template('atms.html', current_tab='ATMs', currentCustomer=currentCustomer, api_key=API_KEY)

@app.route('/customers')
def customers():
    currentCustomer = request.args.get('customer_name')
    return render_template('customers.html', current_tab='Customers', currentCustomer=currentCustomer, api_key=API_KEY)

@app.route('/deposi')
def accounts():
    currentCustomer = request.args.get('customer_name')
    return render_template('accounts.html', current_tab='Accounts', currentCustomer=currentCustomer)

@app.route('/purchases')
def purchases():
    currentCustomer = request.args.get('customer_name')
    return render_template('purchases.html', current_tab='Purchases', currentCustomer=currentCustomer)

@app.route('/deposits')
def deposit():
    currentCustomer = request.args.get('customer_name')
    return render_template('deposits.html', current_tab='Deposits', currentCustomer=currentCustomer)

@app.route('/enterprise')
def enterprise():
    return render_template('enterprise.html', current_tab='Enterprise')

if __name__ == '__main__':
    app.run(debug=True)

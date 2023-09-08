from flask import Flask, render_template, request
from flask_cors import CORS
from decouple import config

# Read the API key from the .env file
API_KEY = config('API_KEY')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def name():
    return render_template('home.html', current_tab='Home', api_key=API_KEY)

@app.route('/atms')
def atms():
    return render_template('atms.html', current_tab='ATMs', api_key=API_KEY)

@app.route('/customers')
def customers():
    return render_template('customers.html', current_tab='Customers', api_key=API_KEY)

@app.route('/accounts')
def accounts():
    return render_template('accounts.html', current_tab='Accounts', api_key=API_KEY)

@app.route('/activity')
def purchases():
    return render_template('activity.html', current_tab='Actiity', api_key=API_KEY)

@app.route('/enterprise')
def enterprise():
    return render_template('enterprise.html', current_tab='Enterprise', api_key=API_KEY)

@app.route('/delete')
def delete():
    return render_template('delete.html', current_tab='Delete', api_key=API_KEY)

if __name__ == '__main__':
    app.run(debug=True)

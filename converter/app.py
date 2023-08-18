from flask import Flask, render_template, request
import requests
app = Flask(__name__)

url = 'https://api.exchangerate.host/convert'

def is_valid_currency(currency_code):
    # Implement your logic to check if currency code is valid
    # For simplicity, let's assume any 3-letter code is valid
    return len(currency_code) == 3

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']

        if not is_valid_currency(from_currency) or not is_valid_currency(to_currency):
            error_message = "Invalid currency code. Please enter a valid 3-letter currency code."
            return render_template('form.html', error=error_message)

        try:
            amount = float(amount)
        except ValueError:
            error_message = "Invalid amount. Please enter a valid number."
            return render_template('form.html', error=error_message)

        params = {
            'from': from_currency,
            'to': to_currency,
            'amount': amount
        }

        response = requests.get(url, params=params)
        data = response.json()

        if 'error' in data:
            error_message = data['error']['info']
            return render_template('form.html', error=error_message)

        converted_amount = data['result']

        return render_template('form.html', result=converted_amount)

    return render_template('form.html')
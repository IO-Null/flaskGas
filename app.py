from flask import Flask, render_template, redirect, request, url_for
from forms import GasCalculator
import os
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', "POST"])
def home():  # put application's code here
    if request.method == "POST":
        price = float(request.form.get('price'))
        mpg = int(request.form.get('mpg'))
        distance_roundtrip = int(request.form.get('distance_roundtrip'))
        hourly_wage = float(request.form.get('hourly_wage'))
        hours_worked = int(request.form.get('hours_worked'))
        # days_worked = 5
        gallons_used = distance_roundtrip / mpg
        cost = price * gallons_used
        wages = hours_worked * hourly_wage
        actual_hourly = (wages - cost) / hours_worked
        return render_template('result.html', actual_hourly=actual_hourly)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

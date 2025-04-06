from flask import Flask, render_template, request
from datetime import datetime, date

app = Flask(__name__)

def calculate_age_and_days(dob):
    today = date.today()
    dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
    age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

    next_birthday = dob_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    
    days_remaining = (next_birthday - today).days
    return age, days_remaining

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        dob = request.form['dob']
        age, days_remaining = calculate_age_and_days(dob)

        if gender == 'Male':
            message = f"Hey {name}, The Handsome Hunk you are {age} years old & you have {days_remaining} days remaining for your next birthday, Yay!"
        else:
            message = f"Hey {name}, Miss Beautiful you are {age} years old & you have {days_remaining} days remaining for your next birthday, Yay!"
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

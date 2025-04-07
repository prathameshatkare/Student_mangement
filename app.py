from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

CSV_FILE = 'results.csv'

# Create CSV file with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Roll', 'Subject 1', 'Subject 2', 'Subject 3', 'Total', 'Percentage', 'Grade'])

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'D'

@app.route('/')
def home():
    return render_template('index.html', message=None)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        roll = request.form['roll']
        s1 = int(request.form['s1'])
        s2 = int(request.form['s2'])
        s3 = int(request.form['s3'])

        total = s1 + s2 + s3
        percentage = round(total / 3, 2)
        grade = calculate_grade(percentage)

        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, roll, s1, s2, s3, total, percentage, grade])

        return render_template('index.html', message="✅ Result submitted successfully!", status="success")

    except Exception as e:
        return render_template('index.html', message=f"❌ Error: {str(e)}", status="error")

@app.route('/all')
def all_results():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        results = list(reader)
    return render_template('all.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

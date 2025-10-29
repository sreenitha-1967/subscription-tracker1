from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get user inputs from form
    name = request.form.get('name')
    monthly_cost = float(request.form.get('monthly_cost'))
    duration = request.form.get('duration')

    # Calculate total based on duration
    if duration == 'monthly':
        total = monthly_cost
    else:
        total = monthly_cost * 12

    return render_template('summary.html', name=name, monthly_cost=monthly_cost, total=total, duration=duration)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

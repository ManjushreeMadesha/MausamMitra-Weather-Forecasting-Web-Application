from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('today.html')

@app.route('/hourly')
def hour():
    return render_template('hourly.html')

@app.route('/daily')
def daily():
    return render_template('daily.html')

@app.route('/radar')
def radar():
    return render_template('radar.html')

@app.route('/minute')
def min():
    return render_template('minute.html')

@app.route('/monthly')
def month():
    return render_template('monthly.html')

@app.route('/air')
def air():
    return render_template('air.html')

if __name__ == "__main__":
    app.run(debug=True)



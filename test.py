from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    #name = "Matt"
    #return render_template('index.html', username=name)
    return render_template('index.html', username='_______')


@app.route("/submit/", methods=['POST'])
def submit_spending():
    # name = request.form['username']
    # processed_text = name.upper()
    # return render_template('index.html', username=processed_text);
    amount = request.form['spending']
    total_savings = calc_total_savings(amount)

    return render_template('index.html', total_savings=total_savings)

def calc_total_savings(amount):
    total_savings = 0

    return total_savings


if __name__ == '__main__':
    app.run()

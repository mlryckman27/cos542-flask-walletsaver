from flask import Flask
from flask import render_template
from flask import request
from redis import Redis
import random


app = Flask(__name__)
redis = Redis(host='redis', port=6379)


challenge_list = ['challenge 1',
                  'challenge 2',
                  'challenge 3',
                  'challenge 4',
                  'challenge 5',
                  'challenge 6',
                  'challenge 7']

redis.delete('total_savings')
redis.delete('challenge')
for elem in challenge_list:
    redis.lpush('challenge', elem)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', username="User")


@app.route("/", methods=['POST'])
def submit_spending():
    amount = float(request.form['spending'])
    item = str(request.form['item'])
    temp = redis.get('total_savings')
    if temp is None:
        total_savings = 0.0
    else:
        total_savings = float(temp)

    total_savings += amount
    redis.set('total_savings', total_savings)

    rand_challenge = random.randint(0, redis.llen('challenge'))
    random_challenge = redis.lindex('challenge', rand_challenge)

    return render_template('index.html', total_savings=total_savings, amount=amount, item=item, random_challenge=random_challenge)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


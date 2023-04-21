from flask import Flask
from flask import render_template
from flask import request
from redis import Redis
import random

# Create instances of Flask and Redis
app = Flask(__name__)
redis = Redis(host='redis', port=6379)

# Healthy activities to be stored in the redis database
challenge_list = ['Activity 1: Take a 30-minute walk.',
                  'Activity 2: Do 20 sit-ups.',
                  'Activity 3: Read one chapter of a book you haven\'t yet read.',
                  'Activity 4: Write a one-page short story.',
                  'Activity 5: Do 20 pushups.',
                  'Activity 6: Pick one room that needs to be cleaned the most, spend 45 minutes cleaning it.',
                  'Activity 7: Create 10-minute video blog about one of your favorite hobbies or interests.']

# Since this is a test application,
# delete keys and start fresh every
# time the application executes,
# then push the activities list into the database
redis.delete('total_savings')
redis.delete('challenge')
for elem in challenge_list:
    redis.lpush('challenge', elem)


# Render the template that serves as the main page
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


# Take in user data regarding item and value
# Update the total savings and get a new
# alternative healthy activity for the user
# from the database and render it to the main page
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
    app.run()


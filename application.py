import json
from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
@application.route('/index')
def home():
    return render_template('index.html',
                            title='home')

@application.route('/portfolio')
def portfolio():
    with open('data/projects.json', 'r') as f:
        projects = json.load(f)
    return render_template('portfolio.html',
                            title='portfolio',
                            projects=projects)

if __name__ == '__main__':
    application.run(debug=True)

import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    with open('data/projects.json', 'r') as f:
        projects = json.load(f)
    return render_template('portfolio.html',
                            title="portfolio",
                            projects=projects)

if __name__ == '__main__':
    app.run(debug=True)

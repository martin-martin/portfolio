from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    projects = [
        {
            'name': 'xyayz',
            'image': 'static/xyayz.png',
            'description': 'this is my fun website.',
            'live_link': 'http://www.xyayz.com',
            'code_link': 'http://github.com/xyayz',
            'info_link': 'http://medium.com'
        },
        {
            'name': 'blossomizer',
            'image': 'static/blossomizer.png',
            'description': 'make crash blossoms.',
            'live_link': 'https://d8z079h7ghotx.cloudfront.net/',
            'code_link': 'https://github.com/martin-martin/blossomizer',
            'info_link': 'https://medium.com/@martin.breuss/2-blossombuilder-e8304843a7f9'
        },
        {
            'name': 'draft',
            'image': '',
            'description': 'in the works',
            'code_link': 'https://github.com/martin-martin/blossomizer'
        }
    ]
    return render_template('portfolio.html',
                            title="portfolio",
                            projects=projects)

if __name__ == '__main__':
    app.run(debug=True)

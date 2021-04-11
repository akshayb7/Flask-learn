from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'AB',
        'title': 'Blog 1',
        'content': 'content 1',
        'date_posted': 'April 11, 2021'
    },
    {
        'author': 'ABs',
        'title': 'Blog 2',
        'content': 'content 2',
        'date_posted': 'April 1, 2021'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if(__name__)=='__main__':
	app.run(debug=True)

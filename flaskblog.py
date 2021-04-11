from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'aa68ae0e3ac8061d0263cd9dfa9bd6a9'

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if(__name__)=='__main__':
	app.run(debug=True)

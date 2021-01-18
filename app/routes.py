from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Thai'}
    posts = [
        {
            'author': {'username': 'Duy'},
            'body': 'Flask de hoc qua phai khong?'
        },
        {
            'author': {'username': 'Long'},
            'body': 'Lap trinh Web that thu vi!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        lash('Yeu cau dang nhap tu user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

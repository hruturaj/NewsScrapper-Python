from project import app, db
from flask import jsonify, render_template, redirect, url_for, request, flash, abort
from flask_login import login_user, logout_user, login_required
from project.models import User
from project.forms import RegistrationForm, LoginForm, WorldForm

@app.route('/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and user.checkPassword(form.password.data) and user is not None:
            login_user(user)
            flash("Logged in successfully!")
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('index')
            return redirect(next)
    return render_template('login.html', form = form)

@app.route('/index')
@login_required
def index():
    from newsapi_key import apiKey
    top = apiKey.get_top_headlines(sources='google-news-in')
    news = top['articles']
    return render_template('index.html', news = news)

@app.route('/world', methods=['GET', 'POST'])
@login_required
def world():
    news = ""
    form = WorldForm()
    if form.validate_on_submit():
        from newsapi_key import apiKey
        top = apiKey.get_top_headlines(country= str(form.country.data))
        news = top['articles']
        return render_template('world.html', form=form, news=news)
    return render_template('world.html', form = form, news=news)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for('login'))

@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, 
                    username = form.username.data, 
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for the registration!")
        return redirect(url_for('login'))
    return render_template('registration.html', form = form)

if __name__ == "__main__":
    app.run(debug= True)








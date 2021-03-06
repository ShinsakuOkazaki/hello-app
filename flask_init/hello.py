import os

from flask import Flask, request, render_template, redirect, url_for, flash, make_response
app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password'] ):
            flash('Successfully logged in')
            response = make_response(redirect(url_for('welcome')))
            response.set_cookie('username', request.form.get('username')) 
            return response
        else:
            error = 'Incorrect username and password'
    return render_template('login.html', error = error)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires = 0)
    return response

@app.route('/')
def welcome():
    username = request.cookies.get('username')
    if username:
        return render_template('welcome.html', username = username)
    else:
        return redirect(url_for('login'))
def valid_login(username, password):
    if username == password:
        return True
    else:
        return False

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.secret_key = 'SuperSecretKey'
    app.run(host = host, port = port)
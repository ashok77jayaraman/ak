from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

# Set a secure secret key for the session
app.secret_key = os.urandom(16)

# Dummy user credentials (replace with your authentication logic)
valid_user = {'username': 'admin', 'password': 'admin'}

@app.route('/')
def home():
    return render_template('login.html', error=None)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == valid_user['username'] and password == valid_user['password']:
        session['logged_in'] = True
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', error='Invalid credentials')

@app.route('/dashboard')
def dashboard():
    if session.get('logged_in'):
        # Add the image file names you want to display
        image_files = ['image1.jpg', 'image2.png', 'image3.gif']

        # Pass the image files to the template
        return render_template('dashboard.html', image_files=image_files)
    else:
        return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

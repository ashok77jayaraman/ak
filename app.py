from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # 16 bytes for a secure secret key

# Configuration to serve static files (images)
app.config['STATIC_FOLDER'] = 'static'

# Define a user (for simplicity, you can replace this with a database)
users = {'admin': 'password123'}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            # Successful login
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            # Incorrect credentials, show error
            error = 'Invalid username or password'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if 'username' in session:
        return f'Welcome, {session["username"]}! This is your dashboard.'
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    # Clear the session to log out the user
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


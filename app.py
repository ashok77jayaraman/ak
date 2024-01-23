from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock user data (replace this with a proper user authentication system)
users = {'admin': 'admin123', 'user': 'user123'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        # In a real application, you would typically set up a session here.
        return redirect(url_for('success'))
    else:
        return render_template('login.html', error='Invalid credentials')

@app.route('/success')
def success():
    return 'Login successful!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


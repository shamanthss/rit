from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used to sign session cookies

# Updated user credentials
users = {
    'admin': 'password', 
    'john': 'securepassword'
}

@app.route('/')
def home():
    # If the user is already logged in, redirect to the welcome page
    if 'username' in session:
        return redirect(url_for('welcome'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Store the username in the session
        session['username'] = username
        return redirect(url_for('welcome'))
    else:
        flash('Invalid credentials. Please try again.', 'error')
        return redirect(url_for('home'))

@app.route('/welcome')
def welcome():
    # If the user is not logged in, redirect them to the login page
    if 'username' not in session:
        return redirect(url_for('home'))

    # After login, show the page with the GIF and message
    return render_template('welcome.html', username=session['username'])

@app.route('/logout')
def logout():
    # Clear the session (log the user out)
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


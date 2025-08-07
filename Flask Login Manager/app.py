from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Mock User class (replace with your actual User model)
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# Mock User database (replace with your actual database)
users = {'1': User('1'), '2': User('2')}

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Login view
@app.route('/login/<user_id>')
def login(user_id):
    user = users.get(user_id)
    if user:
        login_user(user)
    return redirect(url_for('index'))

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Protected route
@app.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)

if __name__ == '__main__':
    app.run(debug=True)

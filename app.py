from flask import Flask, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Use a generic database URI format
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'  # Replace with your database URI
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/profile')
def profile():
    user = {
        'name': 'John Doe',
        'bio': 'Travel enthusiast and adventurer.',
        'location': 'New York',
        'age': 28,
    }
    return render_template('profile.html', user=user)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)
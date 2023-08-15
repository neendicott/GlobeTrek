from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

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

if __name__ == '__main__':
    app.run(debug=True)

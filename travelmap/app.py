from flask import Flask, render_template

app = Flask(__name__)
#Defined a route for the root URL using the decorator. This function below is called when someone visits the root URL
@app.route('/')
def index(): 
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
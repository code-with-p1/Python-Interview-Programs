from flask import Flask

app = Flask(__name__)

# Define a single function that will be mapped to multiple URLs
@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return 'Welcome to the home page!'

# Define another function for a different route
@app.route('/about')
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    app.run(debug=True)

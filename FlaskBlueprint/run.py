from flask import Flask
from app.views import my_blueprint

# Calling create_app method
app = Flask(__name__)
app.register_blueprint(my_blueprint)

@app.route('/')
def index():
    return "<h1> Flask - Blueprint Example - Index Page </h1>"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

'''
Normal API
http://127.0.0.1:5000/

From Blueprint
http://127.0.0.1:5000/blueprint/hello
http://127.0.0.1:5000/blueprint/test

'''
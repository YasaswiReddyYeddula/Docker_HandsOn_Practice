from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask app running in docker!"

@app.route('/about')
def about():
    return "This is a simple Flask application running inside a docker container."

@app.route('/contact')
def contact():
    return "Contact us at: abc"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
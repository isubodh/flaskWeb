from flask import Flask

app = Flask(__name__)

# Default route
@app.route('/')
def home():
    return "Hello Subodh"

@app.route('/about')
def about():
    return "<HR>I am about"

if __name__ == "__main__":
    app.run(debug=True)
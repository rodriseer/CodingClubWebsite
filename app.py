# importing flask to run my backend website
from flask import Flask, render_template\
# initializer
app = Flask(__name__)

"""
@app.route('/'): this defines the URL route for the homepage, When you visit http://127.0.0.1:5000/, it will serve the index.html file
render_template('index.html'): this tells Flask to render your index.html file from the /templates folder.

"""
@app.route('/')
def index():
    return render_template('index.html')

# main runner for the flask
if __name__ == '__main__':
    app.run(debug=True)
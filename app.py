from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! EDUC platform coming soon.'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/trujilloj') #unused directory, will remove later
def trujilloj():
    return redirect("https://github.com/trujillo-j/URL-Shortner")
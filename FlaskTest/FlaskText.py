from flask import Flask
from werkzeug import security

app = Flask(__name__)


@app.route('/')
def home():
    return security.generate_password_hash("Pass")


if __name__ == '__main__':
    app.run()
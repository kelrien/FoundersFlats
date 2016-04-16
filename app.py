from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login_user():
    return render_template("test.html")


@app.route('/privacy')
def privacy():
    return render_template("privacy.html")


if __name__ == '__main__':
    app.run(debug="True", host="0.0.0.0", port=80)

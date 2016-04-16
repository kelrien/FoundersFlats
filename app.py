from flask import Flask
from flask import render_template
from flask import request
from data import dataaccess

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/login', methods=["GET"])
def login_user():
    return render_template("test.html")

@app.route('/login', methods=["POST"])
def transmit_credentials():
    id = request.json['id']
    print "USER ID:", id
    user = dataaccess.get_user(id)
    if user:
        print "User exists"
    else:
        print "User does not exist, creating..."
    return "ok"

@app.route('/privacy')
def privacy():
    return render_template("privacy.html")


if __name__ == '__main__':
    print "================= RESTART ================="
    app.run(debug="True", host="0.0.0.0", port=80)

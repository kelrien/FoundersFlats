from flask import Flask
from flask import render_template
from flask import request
from flask import current_app
from flask import redirect
from data import dataaccess

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/login', methods=["GET"])
def login_user():
    return render_template("_test.html")

@app.route('/login', methods=["POST"])
def transmit_credentials():
    id = request.json['id']
    print "USER ID:", id
    user = dataaccess.get_user(id)
    if user:
        print "User exists"
    else:
        print "User does not exist, creating..."
    response = current_app.make_response(redirect('/'))
    response.set_cookie("id", value=id)
    return response

@app.route('/offers')
def offers():
    return render_template("offers.html")

@app.route('/create', methods=["GET"])
def create_offer():
    return render_template("create.html")

@app.route('/create', methods=["POST"])
def create_offer_api():
    print request.form
    return render_template("create.html")



@app.route('/privacy')
def privacy():
    return render_template("_privacy.html")


if __name__ == '__main__':
    print "================= RESTART ================="
    app.run(debug="True", host="0.0.0.0", port=80)

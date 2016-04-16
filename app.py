from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/login', methods=["GET"])
def login_user():
    return render_template("test.html")

@app.route('/login', methods=["POST"])
def transmit_credentials():
    print request.json
    return True


@app.route('/privacy')
def privacy():
    return render_template("privacy.html")


if __name__ == '__main__':
    app.run(debug="True", host="0.0.0.0", port=80)

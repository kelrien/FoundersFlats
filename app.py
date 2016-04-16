from flask import Flask
from flask import render_template
from flask import request
from flask import current_app
from flask import redirect
from flask import jsonify
from flask import abort
from data import dataaccess
import json

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    print request.cookies
    return render_template("index.html")

@app.route('/login', methods=["GET"])
def login_user():
    return render_template("_test.html")

@app.route('/login', methods=["POST"])
def transmit_credentials():
    id = request.json['id']
    profile = request.json['permalink']
    name = request.json['display_name']
    user = dataaccess.get_user(id)
    if user:
        print "User exists"
        print user
    else:
        params = (id, "", name, profile)
        print "User does not exist, creating...", params
        dataaccess.create_user(params)
    response = current_app.make_response(redirect('/'))
    response.set_cookie("id", value=id)
    return response

@app.route('/offers')
def offers():
    result = dataaccess.get_offers()
    xid = request.cookies.get("id")
    user = dataaccess.get_user(xid)
    print user
    print result
    return render_template("offers.html", offers=result)

@app.route('/offers/<int:id>')
def offer_detail(id):
    print id
    result = None
    if id:
        result = dataaccess.get_offer(id)
    if result:
        user = dataaccess.get_user(result["creator_id"])
        merge = user.copy()
        result.update(merge)
        print "TEST!!!!!", test
        return render_template("offer-detail.html", offer=result)
    else:
        abort(404)

@app.route('/createoffer', methods=["GET"])
def create_offer():
    xid = request.cookies.get("id")
    return render_template("createoffer.html")

@app.route('/createoffer', methods=["POST"])
def create_offer_api():
    xid = request.cookies.get("id")
    print "XID:", xid
    address = request.form["address"]
    monthly = request.form["monthly_cost"]
    once = request.form["single_cost"]
    size = request.form["size"]
    title = request.form["title"]
    description = request.form["description"]
    start = request.form["from"]
    end = request.form["to"]
    we_offer = {"1": request.form["offer_it"],
    "2": request.form["offer_design"],
    "3": request.form["offer_law"],
    "4": request.form["offer_mgmt"],
    "5": request.form["offer_other"]
    }
    we_need = {"1": request.form["search_it"],
    "2": request.form["search_design"],
    "3": request.form["search_law"],
    "4": request.form["search_law"],
    "5": request.form["search_other"]
    }
    album = 0
    params = (xid, address, monthly, once, size, title, description, start, end, json.dumps(we_offer), json.dumps(we_need), album)
    print params
    id = dataaccess.create_offer(params)
    if id:
        return render_template("success.html")
    return render_template("createofer.html")

@app.route('/profile')
def get_profile():
    return render_template("profile.html")


@app.route('/privacy')
def privacy():
    return render_template("_privacy.html")


if __name__ == '__main__':
    print "================= RESTART ================="
    app.run(debug="True", host="0.0.0.0", port=80)

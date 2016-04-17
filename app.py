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
    xid = request.cookies.get("id")
    return render_template("index.html", loggedin=(xid is not None))

@app.route('/login', methods=["GET"])
def login_user():
    return render_template("login.html")

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
        new_dict = json.dumps({"1": "0", "2": "0", "3": "0", "4": "0", "5":"0"})
        params = (id, new_dict, name, profile)
        print "User does not exist, creating...", params
        dataaccess.create_user(params)
    response = current_app.make_response(redirect('/'))
    response.set_cookie("id", value=id)
    return response

@app.route('/profile', methods=["GET"])
def show_profile():
    xid = request.cookies.get("id")
    if not xid:
        return render_template("profile.html", loggedin=(xid is not None))
    user = dataaccess.get_user(xid)
    user["categories"] = json.loads(user["categories"])
    print user
    return render_template("profile.html", profile=user, loggedin=(xid is not None))

@app.route('/profile', methods=["POST"])
def update_profile():
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print ""
    print request.form
    xid = request.cookies.get("id")
    if not xid:
        return render_template("404.html", loggedin=(xid is not None))
    dict = {"1": request.form["search_it"],"2": request.form["search_design"],"3": request.form["search_law"],"4": request.form["search_mgmt"]}
    params = (json.dumps(dict) ,xid)
    user = dataaccess.update_user(params)
    return current_app.make_response(redirect('/profile'))

@app.route('/offers', methods=["GET"])
def offers():
    result = dataaccess.get_offers()
    xid = request.cookies.get("id")
    user = dataaccess.get_user(xid)
    print user
    print result
    return render_template("offers.html", offers=result, loggedin=(xid is not None))



def intTryParse(value):
    try:
        return int(value)
    except ValueError:
        return None



@app.route('/offers', methods=["POST"])
def filter_offers():
    print request.form
    xid = request.cookies.get("id")
    price = intTryParse(request.form["monthly_cost"])
    size = intTryParse(request.form["size"])
    # ImmutableMultiDict([('monthly_cost', u''), ('search_law', u'0'), ('search_law', u'0'), ('search_mgmt', u'0'), ('search_mgmt', u'0'), ('search_design', u'0'), ('search_design', u'0'), ('search_it', u'1'), ('search_it', u'0'), ('size', u'')])
    i_offer = {"1": request.form["offer_it"],"2": request.form["offer_design"], "3": request.form["offer_law"], "4": request.form["offer_mgmt"]}
    i_want = {"1": request.form["search_it"],"2": request.form["search_design"], "3": request.form["search_law"], "4": request.form["search_mgmt"]}
    if i_offer == {"1": "0", "2": "0", "3": "0", "4":"0"}:
        i_offer = None
    if i_want == {"1": "0", "2": "0", "3": "0", "4":"0"}:
        i_want = None
    values = dataaccess.filter_offers(price = price, size = size, offered = i_offer, wanted = i_want)
    result = {}
    for i, value in enumerate(values):
        result[str(i)] = value
    return render_template("offers.html", offers =result, formdata=request.form,  loggedin=(xid is not None))


@app.route('/offers/<int:id>')
def offer_detail(id):
    print id
    result = None
    if id:
        result = dataaccess.get_offer(id)
    if result:
        user = dataaccess.get_user(result["creator_id"])
        merge = user.copy()
        result.update(merge )
        xid = request.cookies.get("id")
        return render_template("offer-detail.html", offer=result, loggedin=(xid is not None))
    else:
        abort(404)

@app.route('/createoffer', methods=["GET"])
def create_offer():
    xid = request.cookies.get("id")
    if not xid:
        return render_template("profile.html", loggedin=(xid is not None))
    user = dataaccess.get_user(xid)
    user["categories"] = json.loads(user["categories"])
    print user
    return render_template("createoffer.html", profile=user, loggedin=(xid is not None))

@app.route('/createoffer', methods=["POST"])
def create_offer_api():
    xid = request.cookies.get("id")
    print "XID:", xid
    if not xid:
        return render_template("404.html", loggedin=(xid is not None))
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
    if not xid:
        return render_template("profile.html", loggedin=(xid is not None))
    user = dataaccess.get_user(xid)
    user["categories"] = json.loads(user["categories"])
    print user
    id = dataaccess.create_offer(params)
    if id:
        return render_template("success.html", loggedin=(xid is not None))
    return render_template("createoffer.html", profile=user, loggedin=(xid is not None))

@app.route('/profile')
def get_profile():
    xid = request.cookies.get("id")
    return render_template("profile.html", loggedin=(xid is not None))


@app.route('/privacy')
def privacy():
    return render_template("_privacy.html")

@app.route('/requests')
def requests():
    return render_template("requests.html")

@app.route('/createrequest')
def create_request():
    return render_template("createrequest.html")


@app.route('/logout')
def logout_user():
    response = current_app.make_response(redirect('/'))
    response.set_cookie('id', '', expires=0)
    return response



if __name__ == '__main__':
    print "================= RESTART ================="
    app.run(debug="True", host="0.0.0.0", port=80)

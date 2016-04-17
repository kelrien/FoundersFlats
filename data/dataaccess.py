import sqlite3
import json
import datetime

DB_FILE_NAME = "ff.db"

def _execute_sql(statement, parameters=(), commit = True):
    with sqlite3.connect(DB_FILE_NAME) as conn:
        cursor = conn.cursor()
        result = cursor.execute(statement, parameters).fetchall()
        if commit:
            conn.commit()
        last_row_id = cursor.lastrowid
        return (result, last_row_id)

def create_user(params):
    result = _execute_sql("INSERT INTO user VALUES (?,?,?,?)", params)
    return result

def get_user(xid):
    parameters = (xid, )
    result = _execute_sql("SELECT rowid,* FROM user WHERE xid=?", parameters)
    if len(result[0]) == 0:
        return None
    else:
        user = {'id': result[0][0][1], "categories": result[0][0][2], "profile": result[0][0][4], "name": result[0][0][3] }
        return user

def update_user(params):
    result = _execute_sql("UPDATE user SET categories=? WHERE xid=?",params)
    return result

def filter_offers(price = None, size = None, offered = None, wanted = None):
    offers = get_offers().values()
    print "BEFORE", len(offers)
    if price:
        for i, offer in enumerate(offers):
            single_price = int(offer["price_monthly"])
            if single_price > price:
                offers.pop(i)
    if size:
        for i, offer in enumerate(offers):
            single_size = int(offer["size"])
            if single_size < size:
                offers.pop(i)
    if offered:
        rmv = []
        for i, offer in enumerate(offers):
            they_want = offer["we_need"]
            match = False
            for index in ["1","2", "3", "4"]:
                if they_want[index] == "1" and offered[index] == "1":
                    print "match!"
                    match = True
                    break
            if not match:
                rmv.append(offer)
        for obj in rmv:
            offers.remove(obj)
    if wanted:
        rmv = []
        for i, offer in enumerate(offers):
            they_offer = offer["we_offer"]
            match = False
            for index in ["1","2", "3", "4"]:
                if they_offer[index] != "0" and wanted[index] == "1":
                    print "match!"
                    match = True
                    break
            if not match:
                rmv.append(offer)
        for obj in rmv:
            offers.remove(obj)
    print "AFTER", len(offers)
    return offers

def create_request(params):
    pass

def get_request(id):
    pass

def create_offer(params):
    result = _execute_sql("INSERT INTO offer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
    id = result[1]
    return id

def get_offer(id):
    result = _execute_sql("SELECT rowid,* from offer where rowid=?",(id, ))
    entry = result[0][0]
    if entry != None:
        offer = parse_offer(result[0][0])
    else:
        offer = None
    return offer

def get_offers():
    result = _execute_sql("SELECT rowid,* FROM offer")
    offers = {}
    if len(result[0]) > 0:
        for entry in result[0]:
            offers[entry[0]] = parse_offer(entry)
    return offers

def parse_offer(entry):
    result = {
        "offer_id": entry[0],
        "creator_id": entry[1],
        "address": entry[2],
        "price_monthly": entry[3],
        "price_once": entry[4],
        "size": entry[5],
        "title": entry[6],
        "description": entry[7],
        "from": entry[8],
        "to": entry[9],
        "we_offer": json.loads(entry[10]),
        "we_need": json.loads(entry[11]),
        "album_id": entry[12]
    }
    return result

if __name__ == '__main__':
    DB_FILE_NAME ="../ff.db"
    # print "Fetching test data:", get_user("16505383_e5736b")
    # update_user((json.dumps({"1":0, "2":0, "3": 1, "4": 0, "5":1}),"16505383_e5736b"))
    # print "ADDING NEW OFFER:", create_offer(("TEST_USER", "A5, 1 Mannheim", 450, 50, 43.5, "DEVELOPER LOFT", "FANCY LOFT IN DEN MANNHEIM QUADRATEN", "1.1.2017", "2.4.2017", "{}", "{}", 0))
    # print "Fechting offers: "
    # print get_offers()
    filter_offers(price=None, size=None, wanted = None, offered={"1":"0","2":"0","3":"1","4":"0","5":"0"})

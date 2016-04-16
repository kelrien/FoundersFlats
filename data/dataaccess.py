import sqlite3
import json

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
    print "Creating User", params
    result = _execute_sql("INSERT INTO user VALUES (?,?,?,?)", params)
    return result

def get_user(xid):
    parameters = (xid, )
    result = _execute_sql("SELECT rowid,* FROM user WHERE xid=?", parameters)
    print result[0]
    if len(result[0]) == 0:
        return None
    else:
        user = {'id': result[0][0][1], "categories": result[0][0][2], "profile": result[0][0][4], "name": result[0][0][3] }
        print "GET_USER_FUNCTION", user
        return user

def create_request(params):
    pass

def get_request(id):
    pass

def del_request(params):
    pass

def create_offer(params):
    # (1 XID, 2 ADDRESS, 3 PRICE_MONTHLY, 4 PRICE_ONCE, 5 SIZE, 5 TITLE, 6 DESCRIPTION, 7 START, 8 END, 9 WE_OFFER, 10 WE_WANT, 11 ALBUM_ID)
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
    # (5, u'16505383_e5736b', u'MANNHEIM KWADRATE', 1000.0, 50.0, 10.0, u'DEVELOPER FLAT', u'KRASSER SCHEISS', u'27.03.2016', u'30.04.2016', u"{1: u'1', 2: u'2', 3: u'3', 4: u'4'}", u"{1: u'on', 2: u'on', 3: u'on', 4: u'on'}", 0)
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
    print result
    return result

def del_offer(params):
    pass

if __name__ == '__main__':
    DB_FILE_NAME ="../ff.db"
    print "Fetching test data:", get_user("16505383_e5736b")
    # print "ADDING NEW OFFER:", create_offer(("TEST_USER", "A5, 1 Mannheim", 450, 50, 43.5, "DEVELOPER LOFT", "FANCY LOFT IN DEN MANNHEIM QUADRATEN", "1.1.2017", "2.4.2017", "{}", "{}", 0))
    print "Fechting offers: "
    print get_offers()

import sqlite3

DB_FILE_NAME = "ff.db"

def _execute_sql(statement, parameters=(), commit = False):
    with sqlite3.connect(DB_FILE_NAME) as conn:
        cursor = conn.cursor()
        result = cursor.execute(statement, parameters).fetchall()
        if commit:
            conn.commit()
        last_row_id = cursor.lastrowid
        return (result, last_row_id)

def create_user(params):
    print "Creating User", params
    result = _execute_sql("INSERT INTO user VALUES (?,?)", params)
    return result

def get_user(xid):
    parameters = (xid, )
    result = _execute_sql("SELECT rowid,* FROM user WHERE xid=?", parameters)
    if len(result[0]) == 0:
        return None
    else:
        user = {'id': result[0][0][1], "categories": result[0][0][2] }
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
    pass

def del_offer(params):
    pass

if __name__ == '__main__':
    DB_FILE_NAME ="../ff.db"
    print "Fetching test data:", get_user("TEST_USER")
    print "ADDING NEW OFFER:", create_offer(("TEST_USER", "A5, 1 Mannheim", 450, 50, 43.5, "DEVELOPER LOFT", "FANCY LOFT IN DEN MANNHEIM QUADRATEN", "1.1.2017", "2.4.2017", "{}", "{}", 0))

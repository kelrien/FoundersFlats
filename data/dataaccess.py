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

def add_request(params):
    pass

def get_request(params):
    pass

def del_request(params):
    pass

def add_offer(params):
    pass

def del_offer(params):
    pass

if __name__ == '__main__':
    print "Fetching test data: ", get_user("TEST_USER")

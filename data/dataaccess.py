import sqlite3

def __init__(self, file_name):
    self.file_name = file_name

def _execute_sql(statement, parameters=(), commit = False):
    with sqlite3.connect(self.file_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(statement, parameters).fetchall()
        if commit:
            conn.commit()
        last_row_id = cursor.lastrowid
        return (result, last_row_id)

def create_user(credentials):
    print "Creating User", credentials
    _execute_sql("INSERT INTO USER VALUES (?,?)")
    pass

def get_user(xid):
    pass

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

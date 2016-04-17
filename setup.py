import sqlite3

DB_FILE_NAME = "ff.db"

CREATE_OFFER_TABLE = '''CREATE TABLE IF NOT EXISTS "offer" (
	`xid`	TEXT NOT NULL,
	`address`	TEXT NOT NULL,
	`price_monthly`	REAL NOT NULL,
	`price_once`	REAL NOT NULL,
	`size`	REAL NOT NULL,
	`title`	TEXT NOT NULL,
	`description`	TEXT NOT NULL,
	`start`	TEXT,
	`end`	TEXT,
	`we_offer`	TEXT,
	`we_want`	TEXT,
	`album_id`	INTEGER
)'''

CREATE_USER_TABLE = '''CREATE TABLE IF NOT EXISTS "user" (
	`xid`	TEXT,
	`categories`	TEXT,
	`name`	TEXT,
	`profile`	TEXT
)
'''

CREATE_REQUEST_TABLE = '''CREATE TABLE IF NOT EXISTS `request` (
	`xid`	TEXT NOT NULL,
	`start`	INTEGER,
	`end`	INTEGER
)
'''

with sqlite3.connect(DB_FILE_NAME) as conn:
    conn.execute(CREATE_OFFER_TABLE)
    conn.execute(CREATE_USER_TABLE)
    conn.execute(CREATE_REQUEST_TABLE)
    conn.commit()

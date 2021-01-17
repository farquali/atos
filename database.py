import sqlite3
import time
import SQLcommands as sql

def setupdb():

	#Connect to database and store connection object
	conn = db_connect()

	create_tables(conn)

	conn.close()

#Connect to database and returns connection object
def db_connect():

	try:
		conn = sqlite3.connect(sql.db_NAME)

	except(sqlite.Error) as e:
		print(f">>>ERROR: Could not connect to database: {e}")
		sys.exit()

	return conn

#Execute CREATE table queries
def create_tables(conn):

	executeSQL(conn, sql.SQL_CREATE_TABLE_bike_issue)
	executeSQL(conn, sql.SQL_CREATE_bike)
	executeSQL(conn, sql.SQL_CREATE_issue)
	executeSQL(conn, sql.SQL_CREATE_station)
	executeSQL(conn, sql.SQL_CREATE_TABLE_journey)

#After data inserts to journey and bike tables, populate remaining tables
def post_dataload_inserts():

	conn = db_connect()

	#executeSQL(conn, sql.SQL_INSERT_INTO_bike, ">>>INSERTING data to bike table")
	executeSQL(conn, sql.SQL_INSERT_INTO_bike_from_journey, ">>>INSERTING data to bike table")
	executeSQL(conn, sql.SQL_INSERT_INTO_bike_from_bike_issue)
	executeSQL(conn, sql.SQL_INSERT_INTO_issue, ">>>INSERTING data to issue table")
	executeSQL(conn, sql.SQL_INSERT_INTO_station, ">>>INSERTING data to station table")

	conn.close()

def executeSQL(conn, query, txt=""):

	if txt != "":
		print(txt)

	try:
		with conn:

			conn.execute(query)

	except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
		print(f">>>ERROR: Could not complete INSERT operation: {e}")

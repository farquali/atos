#!/Users/alice/opt/miniconda3/bin/python
import SQLcommands2 as sql
import sqlite3

def main():

	conn = db_connect()

	ask(conn, sql.SQL_qu1, "Qu 1: How many bike stations are in the cycle network?")


def db_connect():

	try:
		conn = sqlite3.connect(sql.db_NAME)

	except(sqlite.Error) as e:
		print(f">>>ERROR: Could not connect to database: {e}")
		sys.exit()

	return conn

def ask(conn, query, qutxt = ""):

	if qutxt != "":
		print(f"\n{qutxt}")

	print(query)

	with conn:

		try:
			for row in conn.execute(query):
				print(row)

		except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
			print(f"Could not complete query: {e}")

	input("\nContinue...\n")









main()

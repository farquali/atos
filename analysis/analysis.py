#!/Users/alice/opt/miniconda3/bin/python
import SQLcommands2 as sql
import sqlite3

def main():

	conn = db_connect()

	ask(conn, sql.SQL_qu1, "Qu 1: How many bike stations are in the cycle network?")
	ask(conn, sql.SQL_qu2, "Qu 2: How many bikes operate within the cycle network?")
	ask(conn, sql.SQL_qu3a_MIN, "Qu 3a: What is the minimum journey time, for the entire year?")
	ask(conn, sql.SQL_qu3a_MAX, "Qu 3a: What is the maximum journey time, for the entire year?")
	ask(conn, sql.SQL_qu3a_AVG, "Qu 3a: What is the average journey time, for the entire year?")
	ask(conn, sql.SQL_qu3b_MIN, "Qu 3b: What is the minimum journey time per month?")
	ask(conn, sql.SQL_qu3b_MAX, "Qu 3b: What is the maximum journey time per month?")
	ask(conn, sql.SQL_qu3b_AVG, "Qu 3b: What is the average journey time per month?")
	ask(conn, sql.SQL_qu4, "Qu 4: Which bike stations are visited the least?")
	ask(conn, sql.SQL_qu5, "Qu 5: What types of problems occur with bikes and how often?")
	ask(conn, sql.SQL_qu6, "Qu 6: Which bikes have unresolved problems?")
	ask(conn, sql.SQL_qu7, "Qu 7: How long does it typically take to resolve a problem with a bike?")
	ask(conn, sql.SQL_qu9, "Qu 9: How many journeys weren't finished?")
	ask(conn, sql.SQL_qu10, "Qu 10: Which months see the most issues raised?")
	ask(conn, sql.SQL_qu11, "Qu 11: From which stations do people do the longest journeys on average?")

	conn.close()


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

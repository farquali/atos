import pandas as pd
import glob
import os.path
import sqlite3
import SQLcommands as sql
import time

csv_dir = "csvs/issues/"

#dataframe column names
bike_id_col = "bike_id"
issue_col = "issue_id"
raised_col = "raise_time"
resolved_col = "resolve_time"

file_count = 0

csv_i_dframe = pd.DataFrame()


def load_issue_csvs():

	#create an iterator for all bike_issue.csvs
	issue_files = glob.iglob(os.path.join(csv_dir, "*.csv"))

	#read each file and load into database
	for file in issue_files:

		global file_count
		file_count += 1

		print(f">>>Processing file {file_count}: {file}")
		tic = time.perf_counter()

		#Read CSV then insert to db
		load_issue_csv(file)
		insert_to_db()

		toc = time.perf_counter()
		print(f"\tCompleted file {file_count} in {toc-tic:0.2f} s\n")

#Read CSV file into a dataframe using Panda
def load_issue_csv(file):

	#remove the 'BIKE-ID-' prefix from values
	remove_prefix = lambda x: int(x[8:])

	#Read 1 csv file into a dataframe, setting column headers, formatting dates and cleaning bike_id
	global csv_i_dframe
	csv_i_dframe = pd.read_csv(
							  file,
							  header = 0,
							  usecols = [0,1,2,3],
							  names = [bike_id_col, issue_col, raised_col, resolved_col],
							  converters = {bike_id_col:remove_prefix},
							  parse_dates = [raised_col, resolved_col],
							  dayfirst = True
							  )

#Insert dataframe to database table bike_issue
def insert_to_db():

		try:
			conn = sqlite3.connect(sql.db_NAME)

			with conn:
			#Insert into bike_issue table

				csv_i_dframe.to_sql('bike_issue', con=conn, if_exists='append', index=False)
				print(f"\tFile {file_count} INSERT to bike_issue table complete")

		except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
			print("\tERROR: Could not complete INSERT into bike_issue table:", e)

		conn.close()

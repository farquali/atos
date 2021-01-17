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
		#prepare_data()
		insert_to_db()

		toc = time.perf_counter()
		print(f"\tCompleted file {file_count} in {toc-tic:0.2f} s\n")

def load_issue_csv(file):
	pass

def insert_to_db():
	pass
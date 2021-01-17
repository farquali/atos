import pandas as pd
import glob
import os.path
import sqlite3
import SQLcommands as sql
import time

csv_dir = "csvs/journeys/"
csv_j_dframe = pd.DataFrame()
file_count = 0

#dataframe column names
journey_id_col = "id"
duration_col = "duration"
bike_id_col = "bike_id"
end_time_col = "end_time"
end_station_id_col = "end_station_id"
end_station_col = "end_station_name"
start_time_col = "start_time"
start_station_id_col = "start_station_id"
start_station_col = "start_station_name"

cols = [journey_id_col, duration_col, bike_id_col, end_time_col, end_station_id_col, end_station_col, start_time_col, start_station_id_col, start_station_col]

#For each csv, read and insert into journey table in database
def load_journey_csvs():

	#locate all journey csvs in directory
	journey_files = glob.iglob(os.path.join(csv_dir, "*.csv"))

	#read each file and load into database
	for file in journey_files:

		global file_count
		file_count += 1

		print(f">>>Processing file {file_count}: {file}")
		tic = time.perf_counter()

		#read csv then insert to db
		load_journey_csv(file)
		insert_to_db()

		toc = time.perf_counter()
		print(f"\tCompleted file {file_count} in {toc-tic:0.2f} s\n")

#Read csv into a Panda dataframe
def load_journey_csv(file):

	global csv_j_dframe
	csv_j_dframe = pd.read_csv(
							  file,
							  usecols=[0,1,2,3,4,5,6,7,8],
							  header = 0,
							  names = cols,
							  parse_dates = [end_time_col, start_time_col],
							  dayfirst = True
							  )

def insert_to_db():

	try:
		conn = sqlite3.connect(sql.db_NAME)

		with conn:
			#Insert into journey table
			csv_j_dframe.to_sql('journey', con=conn, if_exists='append', index=False, chunksize=10000)

			print(f"\tFile {file_count} INSERT to journey table complete")

	except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
		print(f"\tERROR: Could not complete INSERT into journey table: {e}")













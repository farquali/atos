#!/Users/alice/opt/miniconda3/bin/python
import load_issues as loadi
import load_journeys as loadj
import database as db
import time

def main():
	tic = time.perf_counter()
	print(f">>>Start Timer: {tic:0.2f} s")

	#Create database tables
	db.setupdb()

	#Read csvs and load data into database
	loadi.load_issue_csvs()
	loadj.load_journey_csvs()

	#Populate remaining tables: bike, issue, station
	db.post_dataload_inserts()

	toc = time.perf_counter()
	print(f">>>Total processing time: {(toc-tic)/60.00:0.2f} mins")


main()
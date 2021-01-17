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

	toc = time.perf_counter()
	print(f">>>Total processing time: {(toc-tic)/60.00:0.2f} mins")


main()
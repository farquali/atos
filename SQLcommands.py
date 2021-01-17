db_NAME = "db/tfl.db"

SQL_CREATE_TABLE_bike_issue = """CREATE TABLE IF NOT EXISTS bike_issue (
									bike_id integer NOT NULL,
									issue_id integer NOT NULL,
									raise_time text NOT NULL,
									resolve_time text,
									PRIMARY KEY (bike_id, issue_id, raise_time),
									FOREIGN KEY (bike_id) REFERENCES bike (id)
										ON DELETE CASCADE,
									FOREIGN KEY (issue_id) REFERENCES issue(id)
										ON DELETE CASCADE
																	)
								"""

SQL_CREATE_TABLE_journey = """CREATE TABLE IF NOT EXISTS journey (
									id integer PRIMARY KEY,
									duration integer,
									bike_id integer NOT NULL,
									end_time text,
									end_station_id integer,
									end_station_name text,
									start_time text NOT NULL,
									start_station_id integer NOT NULL,
									start_station_name NOT NULL,
									FOREIGN KEY (bike_id) REFERENCES bike (id)
										ON DELETE CASCADE,
									FOREIGN KEY (start_station_id, start_station_name) REFERENCES station(id, name)
										ON DELETE CASCADE,
									FOREIGN KEY (end_station_id, end_station_name) REFERENCES station(id, name)
										ON DELETE CASCADE
									)
							"""

SQL_CREATE_bike = """CREATE TABLE IF NOT EXISTS bike (
            				id integer PRIMARY KEY
            										)
        				"""

SQL_CREATE_issue = """CREATE TABLE IF NOT EXISTS issue (
								id text PRIMARY KEY
														)
							"""

#Primary key is both id and name because of a few stations that have the same id but different names e.g. 780, 781, 782
SQL_CREATE_station = """CREATE TABLE IF NOT EXISTS station (
									id integer NOT NULL,
									name text NOT NULL,
									PRIMARY KEY(id, name)
															)
							"""

#Not used - this doesn't remove duplicates (so split into 2 queries below)
SQL_INSERT_INTO_bike = """INSERT INTO bike (id)
						SELECT DISTINCT bike_id FROM bike_issue
						UNION
						SELECT DISTINCT bike_id FROM journey
						"""

SQL_INSERT_INTO_bike_from_journey = """INSERT INTO bike (id)
SELECT DISTINCT bike_id FROM journey
WHERE NOT EXISTS (SELECT 1 FROM bike b WHERE bike_id = b.id)
"""

SQL_INSERT_INTO_bike_from_bike_issue = """INSERT INTO bike (id)
SELECT DISTINCT bike_id FROM bike_issue
WHERE NOT EXISTS (SELECT 1 FROM bike b WHERE bike_id = b.id)
"""

SQL_INSERT_INTO_issue = """INSERT INTO issue (id)
SELECT DISTINCT issue_id FROM bike_issue
WHERE NOT EXISTS (SELECT 1 FROM issue i WHERE issue_id = i.id)
"""

SQL_INSERT_INTO_station = """INSERT INTO station (id, name) SELECT end_station_id, end_station_name FROM(
SELECT DISTINCT end_station_id, end_station_name FROM journey
WHERE end_station_id IS NOT NULL
UNION
SELECT start_station_id, start_station_name FROM journey)
WHERE NOT EXISTS (SELECT 1 FROM station s WHERE end_station_id = s.id)
"""
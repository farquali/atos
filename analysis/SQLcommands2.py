db_NAME = "../db/tfl.db"

SQL_qu1 = """SELECT COUNT(DISTINCT id) FROM station"""

SQL_qu2 = """SELECT COUNT(DISTINCT id) FROM bike"""

SQL_qu3a_MAX = """SELECT id, MAX(duration) as seconds, ROUND((duration/86400.00),0) as days FROM
(SELECT id, duration, start_time, start_station_name, end_time, end_station_name,
strftime('%Y', start_time) as year
FROM journey
WHERE year = '2016')
"""

SQL_qu3a_MIN ="""SELECT id, MIN(duration) as seconds, ROUND((duration/86400.00),0) as days FROM
(SELECT id, duration, strftime('%Y', start_time) as year FROM journey
WHERE year = '2016')
"""

SQL_qu3a_AVG ="""SELECT ROUND((AVG(duration)/60.00),1) as minutes FROM
(SELECT id, duration, strftime('%Y', start_time) as year
FROM journey
WHERE year = '2016')
"""

SQL_qu3b_MAX ="""SELECT id, MAX(duration) as max_duration, ROUND( MAX(duration)/3600, 2)  as hours, month FROM
(SELECT id, duration, strftime('%m', start_time) as month
FROM journey)
group by month
"""

SQL_qu3b_MIN ="""SELECT id, MIN(duration) as min_duration, month FROM
(SELECT id, duration, start_time, end_time, strftime('%m', start_time) as month
FROM journey)
group by month order by month
"""

SQL_qu3b_AVG ="""SELECT ROUND(AVG(duration),0) as avg_dur_in_secs,
ROUND((AVG(duration)/60.00),1) as avg_dur_in_mins, month FROM
(SELECT id, duration, start_time, end_time, strftime('%m', start_time) as month
FROM journey)
group by month
"""

SQL_qu4 = """SELECT id,  name, SUM(c) AS nvisits FROM
(SELECT end_station_id as id, end_station_name as name, count(end_station_id) as c
FROM journey WHERE end_station_id IS NOT NULL
GROUP BY end_station_id
UNION
SELECT start_station_id, start_station_name, count(start_station_id) as c
FROM journey
GROUP BY start_station_id)
GROUP BY id ORDER BY nvisits LIMIT 10
"""

SQL_qu5 = """SELECT issue_id, count(issue_id) as c FROM bike_issue GROUP BY issue_id ORDER BY c"""

SQL_qu6 = """SELECT bike_id, resolve_time FROM bike_issue WHERE resolve_time IS NULL"""

SQL_qu6b = """SELECT count(*) FROM
(SELECT bike_id, resolve_time FROM bike_issue
WHERE resolve_time IS NULL)
"""

SQL_qu7 = """SELECT issue_id, ROUND(AVG(days),0) as total_days FROM
(SELECT bike_id, issue_id, (julianday(resolve_time) - julianday(raise_time)) as days
FROM bike_issue
WHERE resolve_time IS NOT NULL
ORDER BY days)
GROUP BY issue_id
"""

SQL_qu9 = """SELECT COUNT(*) FROM journey WHERE end_time IS NULL"""

SQL_qu10 = """SELECT month, count(month) as nissues FROM
(SELECT issue_id, strftime('%m', raise_time) as month
FROM bike_issue) GROUP BY month ORDER BY nissues DESC"""

SQL_qu11 = """SELECT start_station_id, start_station_name, ROUND(AVG(duration)/60,2) as avg_in_mins
FROM journey
GROUP BY start_station_name ORDER BY avg_in_mins DESC LIMIT 10"""






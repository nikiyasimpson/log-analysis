# Log Analysis

Using data from Udacity Full Stack program, will analysis SQL data set of news articles and log files from HTTP requests to populate a report

##Views

create view LOG_STATUS_SUMMARY_VIEW as select date(time), SUM(case when  status = '404 NOT FOUND' then 1 ELSE 0  END) as ERROR_COUNT, SUM(case when status = '200 OK' then 1 ELSE 0 END) as OK_COUNT,  COUNT(1) as TOTAL_REQUESTS  from log  group by date(time);

##How to Run
python3 newsdb.py > log_analysis.txt

## Summary Includes
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
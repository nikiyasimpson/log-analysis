# Log Analysis

Using news article data from Udacity Full Stack program, the log analysis code will analysis SQL data set of news articles and log files from HTTP requests to populate a summary report

Python 3 is used to run the code for this project

## Data

### Table Information
The following data shows the 3 tables that populate the summary report
**Table "public.articles"**

 Column |           Type           |                       Modifiers                       
--------+--------------------------+-------------------------------------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     | 
 body   | text                     | 
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('articles_id_seq'::regclass)

Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)

 
**Table "public.authors"**

 Column |  Type   |                      Modifiers                       
--------+---------+------------------------------------------------------
 name   | text    | not null
 bio    | text    | 
 id     | integer | not null default nextval('authors_id_seq'::regclass)

Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)
 
**Table "public.log"**

 Column |           Type           |                    Modifiers                     
--------+--------------------------+--------------------------------------------------
 path   | text                     | 
 ip     | inet                     | 
 method | text                     | 
 status | text                     | 
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('log_id_seq'::regclass)

Indexes:
    "log_pkey" PRIMARY KEY, btree (id)

### Views
One view was created for the log errors called LOG_STATS_SUMMARY. The following is the code to create the view:
`create view LOG_STATUS_SUMMARY_VIEW as select date(time), SUM(case when  status = '404 NOT FOUND' then 1 ELSE 0  END) as ERROR_COUNT, SUM(case when status = '200 OK' then 1 ELSE 0 END) as OK_COUNT,  COUNT(1) as TOTAL_REQUESTS  from log  group by date(time);`

## How to Run
Make sure the PostgreSQL (psycopg2) package is installed

To install: `pip install psycopg2-binary`
For  more information on PostgreSQL install visit the [documentation](http://initd.org/psycopg/docs/install.html)

#### To run code
To run summary report: `python3 newsdb.py > log_analysis.txt`

## Summary Includes
1. What are the most popular three articles of all time? Which articles have been accessed the most? Data is presented as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? Data is presented as a sorted list with the days with the highest percentages of errors listed first.

## Author
Nikiya M. Simpson, Student
Udacity, Full Stack Web Development Nanodegree Program
2019
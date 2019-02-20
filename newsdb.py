import psycopg2

def get_top_articles():

  conn = psycopg2.connect("dbname=news")
  c = conn.cursor()
  c.execute("select title, count(log.id) as num_log from articles left join log on '/article/'||articles.slug = log.path group by title order by num_log desc")
  results = c.fetchall()
  print(results)

def get_top_authors():

  conn = psycopg2.connect("dbname=news")
  c = conn.cursor()
  c.execute("select name, count(log.id) as num_log from articles join authors on articles.author = authors.id left join log on '/article/'||articles.slug = log.path group by name order by num_log desc")
  results = c.fetchall()
  print(results)

def get_error_percents():

  conn = psycopg2.connect("dbname=news")
  c = conn.cursor()
  c.execute("select date(time), count(*) as errors  from log where status = '404 NOT FOUND' group by date(time) order by errors desc ")
  results = c.fetchall()
  print(results)



get_top_articles()
get_top_authors()
get_error_percents()
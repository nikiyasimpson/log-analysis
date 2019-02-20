import psycopg2

def get_articles():

  conn = psycopg2.connect("dbname=news")
  c = conn.cursor()
  c.execute("select title, count(log.id) as num_log from articles left join log on '/article/'||articles.slug = log.path group by title order by num_log desc")
  result = c.fetchall()
  print(result)
  return result

#!/usr/bin/env python3
import psycopg2


def run_query(query):
    """ This function connects to the database
    and returns the results from query """

    conn = psycopg2.connect("dbname=news")
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except psycopg2.Error as e:
        pass
    print(e.pgerror)


def get_top_articles():
    """ Print the top performing article views """

    query = """select title, count(log.id) as views from articles
             left join log on '/article/'||articles.slug
             = log.path group by title order by views desc limit 3 """

    results = run_query(query)
    print_table("Top Articles", results, "views")


def get_top_authors():
    """ Print the top authors with the most views """

    query = """select name, count(log.id) as views from articles
             join authors on articles.author = authors.id
             left join log on '/article/'||articles.slug =
             log.path group by name order by views desc"""

    results = run_query(query)
    print_table("Top Authors", results, "views")


def get_error_percents():
    """ Print dates with more than 1% of request errors
    and the percent error rate """

    query = """select TO_CHAR(date,'fmMonth DD, YYYY'),
             round((error_count::decimal/total_requests)*100,2)::text
             ||'%'  as error_percent  from LOG_STATUS_SUMMARY_VIEW where
             (error_count::decimal/total_requests) > 0.01
             order by error_percent desc"""

    results = run_query(query)
    print_table("Days with More than 1% Errors", results, "errors")


def print_table(title, table, descriptor):
    """ This function prints a summary table for query results """

    print(title + "\n")
    for description, value in table:
        print('\t{} - {} {}'.format(description, value, descriptor))
    print("\n")


def main():
    """ Main Function that prints summary output to screen """
    print("Log Analysis Summary" + "\n")
    get_top_articles()
    get_top_authors()
    get_error_percents()
    print("End of Report")


main()

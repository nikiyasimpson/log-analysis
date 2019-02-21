import psycopg2


# This function connects to the database and returns the results from query
def run_query(query):
    conn = psycopg2.connect("dbname=news")
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()


# Print the top performing article views
def get_top_articles():

    query = "select title, count(log.id) as num_log from articles " \
            "left join log on '/article/'||articles.slug " \
            "= log.path group by title order by num_log desc"

    results = run_query(query)
    print_table("Top Articles", results, "views")


# Print the top authors with the most views
def get_top_authors():

    query = "select name, count(log.id) as num_log from articles " \
            "join authors on articles.author = authors.id " \
            "left join log on '/article/'||articles.slug = "\
            "log.path group by name order by num_log desc"

    results = run_query(query)
    print_table("Top Authors", results, "views")


# Print dates with more than 1% of request errors and the percent error rate
def get_error_percents():

    query = "select TO_CHAR(date,'fmMonth DD, YYYY'), " \
            "round((error_count::decimal/total_requests)*100,2)::text" \
            " ||'%'  as error_percent  from LOG_STATUS_SUMMARY_VIEW where  "\
            "(error_count::decimal/total_requests) > 0.01 " \
            "order by error_percent desc"

    results = run_query(query)
    print_table("Days with More than 1% Errors", results, "errors")


# This function prints a summary table for query results
def print_table(title, table, descriptor):

    print(title + "\n")
    for row in table:
        description, value = row
        print('\t{} - {} {}'.format(description, value, descriptor))
    print("\n")


# Main Function that prints summary output to screen
def main():
    print("Log Analysis Summary" + "\n")
    get_top_articles()
    get_top_authors()
    get_error_percents()
    print("End of Report")


main()

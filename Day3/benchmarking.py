import time
import sqlite3

def query1():
    con = sqlite3.connect('news_db.sqlite')
    c = con.cursor()
    c.execute(
        "SELECT distinct covid.source_id, india.source_id FROM top_headlines_covid19 covid INNER JOIN top_headlines_india india on india.source_id = covid.source_id")
    rows = c.fetchall()
    # for row in rows:
    #     print(row)
    c.close()

def query2():
    con = sqlite3.connect('news_db.sqlite')
    c = con.cursor()
    c.execute(
        "SELECT sources.source_id FROM publication_reference sources LEFT JOIN top_headlines_covid19 covid USING(source_id) WHERE covid.source_id IS NULL")
    rows = c.fetchall()
    # for row in rows:
    #     print(row)
    c.close()

def query3():
    con = sqlite3.connect('news_db.sqlite')
    c = con.cursor()
    c.execute(
        "SELECT distinct covid.description, india.description FROM top_headlines_covid19 covid INNER JOIN top_headlines_india india on india.description = covid.description")
    rows = c.fetchall()
    # for row in rows:
    #     print(row)
    c.close()

# indexed_news_db

def indexed_query1():
    con = sqlite3.connect('indexed_news_db.sqlite')
    c = con.cursor()
    c.execute(
        "SELECT distinct covid.source_id, india.source_id FROM top_headlines_covid19 covid INNER JOIN top_headlines_india india on india.source_id = covid.source_id")
    rows = c.fetchall()
    # for row in rows:
    #     print(row)
    c.close()


def indexed_query2():
    con = sqlite3.connect('indexed_news_db.sqlite')
    c = con.cursor()
    c.execute(
        "SELECT sources.source_id FROM publication_reference sources LEFT JOIN top_headlines_covid19 covid USING(source_id) WHERE covid.source_id IS NULL")
    rows = c.fetchall()
    # for row in rows:
    #     print(row)
    c.close()


def indexed_query3():
    con = sqlite3.connect('indexed_news_db.sqlite')
    c = con.cursor()
    c.execute(
        "SELECT distinct covid.description, india.description FROM top_headlines_covid19 covid INNER JOIN top_headlines_india india on india.description = covid.description")
    rows = c.fetchall()
    # for row in rows:
    #     print(row)
    c.close()


def timed(fun, n=1000):
    start = time.time()
    for i in range(n):
        fun()
    end = time.time()

    print("Function=%s, Time=%s" % (fun.__name__, end - start))

q1_time = timed(query1)
in_q1_time = timed(indexed_query1)

print("Query time without index: ", q1_time, "and with index: ", in_q1_time, "seconds")

q2_time = timed(query2)
in_q2_time = timed(indexed_query2)

print("Query time without index: ", q2_time, "and with index: ", in_q2_time, "seconds")

q3_time = timed(query3)
in_q3_time = timed(indexed_query3)

print("Query time without index: ", q3_time, "and with index: ", in_q3_time, "seconds")


# using only Python standard modules

import sqlite3
import csv

# SETUP TABLE

con = sqlite3.connect('indexed_news_db.sqlite')
c = con.cursor()

c.execute(open('create_top_headlines_india.sql', 'r').read())
c.execute('CREATE INDEX india_source_id ON top_headlines_india(source_id)')

c.execute(open('create_top_headlines_berlin.sql', 'r').read())
c.execute('CREATE INDEX berlin_source_id ON top_headlines_berlin(source_id)')

c.execute(open('create_top_headlines_covid19.sql', 'r').read())
c.execute('CREATE INDEX covid19_source_id ON top_headlines_covid19(source_id)')

c.execute(open('create_publication_reference.sql', 'r').read())
c.execute('CREATE INDEX reference_source_id ON publication_reference(source_id)')

con.commit()
c.close()

# LOAD DATA IN THE TABLES

con = sqlite3.connect('indexed_news_db.sqlite')
cur = con.cursor()

with open('top_headlines_india.csv','rt', encoding='utf-8') as f: # default is that first line are the headers
    dr = csv.DictReader(f, delimiter=',') # comma is default delimiter
    to_db = [(i['source_id'], i['source_name'], i['author'], i['title'], \
    	i['description'], i['url'], i['urlToImage'], i['publishedAt'], i['content']) for i in dr]

cur.executemany("INSERT INTO top_headlines_india (source_id, source_name, author, title, description, url, \
	urlToImage, publishedAt, content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

with open('top_headlines_berlin.csv','rt', encoding='utf-8') as f: # default is that first line are the headers
    dr = csv.DictReader(f, delimiter=',') # comma is default delimiter
    to_db = [(i['source_id'], i['source_name'], i['author'], i['title'], \
    	i['description'], i['url'], i['urlToImage'], i['publishedAt'], i['content']) for i in dr]

cur.executemany("INSERT INTO top_headlines_berlin (source_id, source_name, author, title, description, url, \
	urlToImage, publishedAt, content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

with open('top_headlines_covid19.csv','rt', encoding='utf-8') as f: # default is that first line are the headers
    dr = csv.DictReader(f, delimiter=',') # comma is default delimiter
    to_db = [(i['source_id'], i['source_name'], i['author'], i['title'], \
    	i['description'], i['url'], i['urlToImage'], i['publishedAt'], i['content']) for i in dr]

cur.executemany("INSERT INTO top_headlines_covid19 (source_id, source_name, author, title, description, url, \
	urlToImage, publishedAt, content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

with open('publication_reference.csv','rt', encoding='utf-8') as f: # default is that first line are the headers
    dr = csv.DictReader(f, delimiter=',') # comma is default delimiter
    to_db = [(i['source_id'], i['source_name'], i['description'], \
    	i['url'], i['category'], i['language'], i['country']) for i in dr]

cur.executemany("INSERT INTO publication_reference (source_id, source_name, description, url, \
	category, language, country) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)

con.commit()
con.close()



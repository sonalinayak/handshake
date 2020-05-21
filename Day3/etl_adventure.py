from newsapi import NewsApiClient
import yaml
import csv
from datetime import datetime
import os

dir = os.path.dirname(__file__)

config = yaml.safe_load(open(os.path.join(dir, "config.yaml")))
news_api_key = config['news_api_key']

newsapi = NewsApiClient(api_key=news_api_key)
sysdate = datetime.today().strftime('%Y-%m-%d')
# Get a data feed for your country's top headline.

def parse_json_to_csv(jsondata, file_name_to_save):
    with open(file_name_to_save, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(
            ['source_id', 'source_name', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt',
             'content'])

        for article in jsondata['articles']:
            writer.writerow([
                article['source']['id'] if article['source']['id'] else '',
                article['source']['name'] if article['source']['name'] else '',
                article['author'] if article['author'] else '',
                article['title'] if article['title'] else '',
                article['description'] if article['description'] else '',
                article['url'] if article['url'] else '',
                article['urlToImage'] if article['urlToImage'] else '',
                article['publishedAt'] if article['publishedAt'] else '',
                article['content'] if article['content'] else ''
            ])

top_headlines_india = newsapi.get_top_headlines(language='en',
                                                country='in',
                                                page_size=100)

# with open('top_headlines_india.json', 'w') as outfile:
#     json.dump(top_headlines_india, outfile)

parse_json_to_csv(top_headlines_india, "_".join((sysdate, 'top_headlines_india.csv')))


# Get a data feed for berlin's top headline.

top_headlines_berlin = newsapi.get_top_headlines(q='Berlin',
                                                 language='de',
                                                 country='de',
                                                 page_size=100)

parse_json_to_csv(top_headlines_berlin, "_".join((sysdate, 'top_headlines_berlin.csv')))

# One for 'covid' or something specifically not 'covid' maybe?

top_headlines_covid19 = newsapi.get_top_headlines(q='covid',
                                                 page_size=100)
parse_json_to_csv(top_headlines_covid19, "_".join((sysdate, 'top_headlines_covid19.csv')))

# Get the publication reference table.
publication_reference = newsapi.get_sources()
publication_reference_filename = "_".join((sysdate, 'publication_reference.csv'))

with open(publication_reference_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(
        ['source_id', 'source_name', 'description', 'url', 'category', 'language', 'country'])

    for source in publication_reference['sources']:
        writer.writerow([
            source['id'] if source['id'] else '',
            source['name'] if source['name'] else '',
            source['description'] if source['description'] else '',
            source['url'] if source['url'] else '',
            source['category'] if source['category'] else '',
            source['language'] if source['language'] else '',
            source['country'] if source['country'] else ''
        ])


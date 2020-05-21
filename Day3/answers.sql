/* Answer1 (What are the common publications in India and covid news?)

Execute a query and read the data */

SELECT distinct covid.source_id, india.source_id
FROM top_headlines_covid19 covid
INNER JOIN top_headlines_india india on india.source_id = covid.source_id;

/* Answer2 (Which sources do not publish information about covid?)

Execute a query and read the data */

SELECT sources.source_id
FROM publication_reference sources
LEFT JOIN top_headlines_covid19 covid USING(source_id)
WHERE covid.source_id IS NULL;

/* Answer3 (Are there any common headlines in Indian and Covid news?)

Execute a query and read the data */

SELECT distinct covid.description, india.description
FROM top_headlines_covid19 covid
INNER JOIN top_headlines_india india on india.description = covid.description;
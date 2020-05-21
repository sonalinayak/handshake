# PDEA Day3

### For this task I decided to use the newsapi data from https://newsapi.org/

Requires Python and sqlite. To use, clone this repository and run commands below.

## Run

### To get data from the newsapi and save it in csv format.

```markdown
cd Day3/

python3 etl_adventure.py 
```

### creating db schema and loading the data to sqlite db

```markdown
python3 loader.py
```

### Run SQL queries 

The queries answers the following questions:
1. What are the common publications in India and covid news?
2. Which sources do not publish information about covid?
3. Are there any common headlines in Indian and Covid news?

```markdown
/usr/bin/sqlite3 news_db.sqlite < answers.sql
```

### Create another sqlite db for the same tables but with a different schema, by adding some indexes. Also load the data.

```markdown
python3 loader_with_index.py
```

### To see the result of benchmarking run:

```markdown
python3 benchmarking.py 
```

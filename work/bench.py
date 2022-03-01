import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import time

# read the csv file into a dataframe
df = pd.read_csv('/work/Anime.csv')
df = df.fillna({'japanese_name':'', 'episodes':0, 'studio':'', 'release_season':'', 'tags':'', 'rating':0.0, 'release_year':0, 'end_year':0, 'description':'', 'content_warning':'', 'related_mange':'', 'related_anime':'', 'voice_actors':'', 'staff':''})

engine = create_engine('postgresql://postgres:@localhost/testdb')
conn = psycopg2.connect('dbname=testdb host=localhost user=postgres')
cur = conn.cursor()

# delete existing records
cur.execute('delete from anime')
conn.commit()

# insert by enumerating the dataframe
start = time.time()
for k, row in df.iterrows():
    cur.execute('insert into anime (rank, name, japanese_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, description, content_warning, related_mange, related_anime, voice_actors, staff) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',  list(row))
conn.commit()
end = time.time()
print('Inserts by enumerating dataframe: %.4fs' % (end-start))

# delete existing records
cur.execute('delete from anime')
conn.commit()

# insert by to_sql() using SQLAlchemy
start = time.time()
df.to_sql('anime', con=engine, if_exists='replace', index=False)
end = time.time()
print('Inserts by to_sql(): %.4fs' % (end-start))

# read by read_sql_query()
start = time.time()
df2 = pd.read_sql_query('select release_year from anime', con=engine)
end = time.time()
print('Reads by read_sql_query(): %.4fs' % (end-start))

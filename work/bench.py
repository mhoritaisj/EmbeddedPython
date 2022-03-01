import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import time

df = pd.read_csv('/work/Anime.csv')
df = df.fillna({'japanese_name':'', 'episodes':0, 'studio':'', 'release_season':'', 'tags':'', 'rating':0.0, 'release_year':0, 'end_year':0, 'description':'', 'content_warning':'', 'related_mange':'', 'related_anime':'', 'voice_actors':'', 'staff':''})

engine = create_engine('postgresql://postgres:@localhost/testdb')
conn = psycopg2.connect('dbname=testdb host=localhost user=postgres')
cur = conn.cursor()

start = time.time()
#for k, row in df.iterrows():
#    cur.execute('insert into anime (rank, name, japanese_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, description, content_warning, related_mange, related_anime, voice_actors, staff) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',  list(row))
df.to_sql('anime', con=engine, if_exists='replace', index=False)
#conn.commit()
end = time.time()
print(end-start)

#start = time.time()
#df2 = pd.read_sql_query('select release_year from anime', con=engine)
#end = time.time()
#print(df2)
#print(end-start)
import pandas as pd
import iris
import time

# read the csv file into a dataframe
df = pd.read_csv('/work/Anime.csv')
df = df.fillna({'japanese_name':'', 'episodes':0, 'studio':'', 'release_season':'', 'tags':'', 'rating':0.0, 'release_year':0, 'end_year':0, 'description':'', 'content_warning':'', 'related_mange':'', 'related_anime':'', 'voice_actors':'', 'staff':''})

# delete existing records
iris.sql.exec('delete from anime')

# insert by enumerating the dataframe
start = time.time()
stmt = iris.sql.prepare('insert into anime (rank, name, japanese_name, type, episodes, studio, release_season, tags, rating, release_year, end_year, description, content_warning, related_mange, related_anime, voice_actors, staff) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
for k, row in df.iterrows():
    stmt.execute(*list(row))
end = time.time()
print('Inserts by enumerating dataframe: %.4fs' % (end-start))

# read by dataframe()
start = time.time()
df2 = iris.sql.exec('select type from anime').dataframe()
end = time.time()
print('Reads by dataframe(): %.4fs' % (end-start))

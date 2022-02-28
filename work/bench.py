import pandas as pd
from sqlalchemy import create_engine
import time

df = pd.read_csv('/work/Anime.csv')
engine = create_engine('postgresql://postgres:@localhost/testdb')

start = time.time()
df.to_sql('anime', con=engine, if_exists='replace', index=False)
end = time.time()
print(end-start)
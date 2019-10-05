import pandas as pd
import sqlalchemy
from os import path


df = pd.read_csv(path.join('Region Temperature Reports', 'Aberdeen.csv'))
df['date'] = pd.to_datetime(df['date'])
print(df.dtypes)
print(df.head(10))
print(df.tail(10))

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/elliot_raju')
df.to_sql('weather_data', con=engine, if_exists = 'append')



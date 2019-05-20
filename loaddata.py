# from urllib import quote_plus as urlquote
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Float
from sqlalchemy.orm import sessionmaker
import pandas as pd
import numpy as np
import pymysql
import os

pymysql.install_as_MySQLdb()


# Set up of the engine to connect to the database
# the urlquote is used for passing the password which might contain special characters such as "/"
engine = create_engine(
    'mysql://rl91qzpzgty8oaf1:evamhxfd7l42mgso@y2w3wxldca8enczv.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/v21ogkg4wvsne316', echo=False)
conn = engine.connect()
Base = declarative_base()

# Declaration of the class in order to write into the database. This structure is standard and should align with SQLAlchemy's doc.


class Current(Base):
    __tablename__ = 'lex'

    Country = Column(String(60), primary_key=True)
    Year = Column(String(25), primary_key=True)
    LEX_at_birth_Both_sexes = Column(Float())
    LEX_at_birth_Male = Column(Float())
    LEX_at_birth_Female = Column(Float())
    LEX_at_age_60_Both_sexes = Column(Float())
    LEX_at_age_60_Male = Column(Float())
    LEX_at_age_60_Female = Column(Float())
    HALE_at_birth_Both_sexes = Column(Float())
    HALE_at_birth_Male = Column(Float())
    HALE_at_birth_Female = Column(Float())
    HALE_at_age_60_Both_sexes = Column(Float())
    HALE_at_age_60_Male = Column(Float())
    HALE_at_age_60_Female = Column(Float())

    # def __repr__(self):
    #     return "(id='%s', Date='%s', Type='%s', Value='%s')" % (self.id, self.Date, self.Type, self.Value)


# Set up of the table in db and the file to import
fileToRead = os.path.join('assets', 'data', 'lexbycountry.csv')
tableToWriteTo = 'lex'

# Panda to create a lovely dataframe
df_to_be_written = pd.read_csv(fileToRead)
df_to_be_written.fillna(0, inplace=True)
# print(df_to_be_written['LEX at birth Both sexes'])
# The orient='records' is the key of this, it allows to align with the format mentioned in the doc to insert in bulks.
listToWrite = df_to_be_written.to_dict(orient='records')

metadata = sqlalchemy.schema.MetaData(bind=engine, reflect=True)
table = sqlalchemy.Table(tableToWriteTo, metadata, autoload=True)

# Open the session
Session = sessionmaker(bind=engine)
session = Session()

# Inser the dataframe into the database in one bulk
conn.execute(table.insert(), listToWrite)

# Commit the changes
session.commit()

# Close the session
session.close()

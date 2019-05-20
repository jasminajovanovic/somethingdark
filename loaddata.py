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


class Obesity(Base):
    __tablename__ = 'obesity'

    Country = Column(String(60), primary_key=True)
    Both_sexes_2016 = Column(Float())
    Male_2016 = Column(Float())
    Female_2016 = Column(Float())
    Both_sexes_2015 = Column(Float())
    Male_2015 = Column(Float())
    Female_2015 = Column(Float())
    Both_sexes_2014 = Column(Float())
    Male_2014 = Column(Float())
    Female_2014 = Column(Float())
    Both_sexes_2013 = Column(Float())
    Male_2013 = Column(Float())
    Female_2013 = Column(Float())
    Both_sexes_2012 = Column(Float())
    Male_2012 = Column(Float())
    Female_2012 = Column(Float())
    Both_sexes_2011 = Column(Float())
    Male_2011 = Column(Float())
    Female_2011 = Column(Float())
    Both_sexes_2010 = Column(Float())
    Male_2010 = Column(Float())
    Female_2010 = Column(Float())
    Both_sexes_2009 = Column(Float())
    Male_2009 = Column(Float())
    Female_2009 = Column(Float())
    Both_sexes_2008 = Column(Float())
    Male_2008 = Column(Float())
    Female_2008 = Column(Float())
    Both_sexes_2007 = Column(Float())
    Male_2007 = Column(Float())
    Female_2007 = Column(Float())
    Both_sexes_2006 = Column(Float())
    Male_2006 = Column(Float())
    Female_2006 = Column(Float())
    Both_sexes_2005 = Column(Float())
    Male_2005 = Column(Float())
    Female_2005 = Column(Float())
    Both_sexes_2004 = Column(Float())
    Male_2004 = Column(Float())
    Female_2004 = Column(Float())
    Both_sexes_2003 = Column(Float())
    Male_2003 = Column(Float())
    Female_2003 = Column(Float())
    Both_sexes_2002 = Column(Float())
    Male_2002 = Column(Float())
    Female_2002 = Column(Float())
    Both_sexes_2001 = Column(Float())
    Male_2001 = Column(Float())
    Female_2001 = Column(Float())
    Both_sexes_2000 = Column(Float())
    Male_2000 = Column(Float())
    Female_2000 = Column(Float())
    Both_sexes_1999 = Column(Float())
    Male_1999 = Column(Float())
    Female_1999 = Column(Float())
    Both_sexes_1998 = Column(Float())
    Male_1998 = Column(Float())
    Female_1998 = Column(Float())
    Both_sexes_1997 = Column(Float())
    Male_1997 = Column(Float())
    Female_1997 = Column(Float())
    Both_sexes_1996 = Column(Float())
    Male_1996 = Column(Float())
    Female_1996 = Column(Float())
    Both_sexes_1995 = Column(Float())
    Male_1995 = Column(Float())
    Female_1995 = Column(Float())
    Both_sexes_1994 = Column(Float())
    Male_1994 = Column(Float())
    Female_1994 = Column(Float())
    Both_sexes_1993 = Column(Float())
    Male_1993 = Column(Float())
    Female_1993 = Column(Float())
    Both_sexes_1992 = Column(Float())
    Male_1992 = Column(Float())
    Female_1992 = Column(Float())
    Both_sexes_1991 = Column(Float())
    Male_1991 = Column(Float())
    Female_1991 = Column(Float())
    Both_sexes_1990 = Column(Float())
    Male_1990 = Column(Float())
    Female_1990 = Column(Float())
    Both_sexes_1989 = Column(Float())
    Male_1989 = Column(Float())
    Female_1989 = Column(Float())
    Both_sexes_1988 = Column(Float())
    Male_1988 = Column(Float())
    Female_1988 = Column(Float())
    Both_sexes_1987 = Column(Float())
    Male_1987 = Column(Float())
    Female_1987 = Column(Float())
    Both_sexes_1986 = Column(Float())
    Male_1986 = Column(Float())
    Female_1986 = Column(Float())
    Both_sexes_1985 = Column(Float())
    Male_1985 = Column(Float())
    Female_1985 = Column(Float())
    Both_sexes_1984 = Column(Float())
    Male_1984 = Column(Float())
    Female_1984 = Column(Float())
    Both_sexes_1983 = Column(Float())
    Male_1983 = Column(Float())
    Female_1983 = Column(Float())
    Both_sexes_1982 = Column(Float())
    Male_1982 = Column(Float())
    Female_1982 = Column(Float())
    Both_sexes_1981 = Column(Float())
    Male_1981 = Column(Float())
    Female_1981 = Column(Float())
    Both_sexes_1980 = Column(Float())
    Male_1980 = Column(Float())
    Female_1980 = Column(Float())
    Both_sexes_1979 = Column(Float())
    Male_1979 = Column(Float())
    Female_1979 = Column(Float())
    Both_sexes_1978 = Column(Float())
    Male_1978 = Column(Float())
    Female_1978 = Column(Float())
    Both_sexes_1977 = Column(Float())
    Male_1977 = Column(Float())
    Female_1977 = Column(Float())
    Both_sexes_1976 = Column(Float())
    Male_1976 = Column(Float())
    Female_1976 = Column(Float())
    Both_sexes_1975 = Column(Float())
    Male_1975 = Column(Float())
    Female_1975 = Column(Float())


# Set up of the table in db and the file to import
# fileToRead = os.path.join('assets', 'data', 'lexbycountry.csv')
fileToRead = os.path.join('assets', 'data', 'obesity.csv')
tableToWriteTo = 'obesity'

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

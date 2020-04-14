import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
import pandas as pd
import sys

engine = create_engine('sqlite:///first_PU.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# user = User("admin","password")
# session.add(user)

pd.options.display.max_rows = 999

df = pd.read_excel('test.xlsx')
print(len(df))

df['D.O.B'] = pd.to_datetime(df['D.O.B'], format='%d-%m-%Y')

print(df)
df.columns=df.columns.str.strip()



for i in range(len(df)):
    r=df['REG.NO'][i]
    d=df['D.O.B']
    n=df['STUDENT NAME'][i]
    r=str(r)
    d=str(d)
    n=str(n)
    user = User(r,d,n)
    session.add(user)
    session.commit()
    print(r,"\n",d,"\n",n)

#user = User("python","python")
#session.add(user)

#user = User("umesh","umesh","umesh")
#session.add(user)

# commit the record the database
session.commit()

session.commit()

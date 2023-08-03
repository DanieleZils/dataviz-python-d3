import csv
import json
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)

def dumps(obj):
    return json.dumps(obj, cls=JSONDateTimeEncoder)

nobel_winners = [
    {'category': 'Physics', 'name': 'Albert Einstein', 'nationality': 'Swiss', 'gender': 'male', 'year': 1921},
    {'category': 'Physics', 'name': 'Paul Dirac', 'nationality': 'British', 'gender': 'male', 'year': 1933},
    {'category': 'Chemistry', 'name': 'Marie Curie', 'nationality': 'Polish', 'gender': 'female', 'year': 1911}
]

# Create the CSV file and write the data to it
cols = nobel_winners[0].keys()
cols = sorted(cols)

with open('data/nobel_winners.csv', 'w') as f:
    fieldnames = nobel_winners[0].keys()
    fieldnames = sorted(fieldnames)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for w in nobel_winners:
        writer.writerow(w)

# Convert 'year' to integers in nobel_winners list
for w in nobel_winners:
    w['year'] = int(w['year'])

# Write the data to a JSON file using the dumps function
with open('data/nobel_winners.json', 'w') as f:
    json.dump(nobel_winners, f, default=JSONDateTimeEncoder)

# Read the JSON file and load the data back to nobel_winners
with open('data/nobel_winners.json') as f:
    nobel_winners = json.load(f)


# create the databse engine:
engine = create_engine('sqlite:///data/nobel_winners.db', echo=True)

Base =  declarative_base()

class Winner(Base):
    __tablename__= 'winners'
    id = Column(Integer, primary_key=True)
    category = Column(String)
    name = Column(String)
    nationality = Column(String)
    year = Column(Integer)
    gender = Column(Enum('male', 'female'))
    def __repr__(self):
        return "<Winner(name='%s', category='%s', year='%s')>"% (self.name, self.category, self.year)

Base.metadata.create_all(engine)

#create the session:

Session = sessionmaker(bind=engine)
session = Session()

# winner_rows = [Winner(**w) for w in nobel_winners]
# session.add_all(winner_rows)
# 


session.query(Winner).get(3)
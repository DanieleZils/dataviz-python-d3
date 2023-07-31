import csv;

nobel_winners = [
 {'category': 'Physics',
  'name': 'Albert Einstein',
  'nationality': 'Swiss',
  'gender': 'male',
  'year': 1921},
 {'category': 'Physics',
  'name': 'Paul Dirac',
  'nationality': 'British',
  'gender': 'male',
  'year': 1933},
 {'category': 'Chemistry',
  'name': 'Marie Curie',
  'nationality': 'Polish',
  'gender': 'female',
  'year': 1911}
]

#create the CSV file and write the data to it
cols = nobel_winners[0].keys()
cols = sorted(cols)

with open('data/nobel_winners.csv', 'w') as f:
    fieldnames = nobel_winners[0].keys() 
    fieldnames = sorted(fieldnames) 
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader() 

    for w in nobel_winners:
        writer.writerow(w)

with open('data/nobel_winners.csv') as f:
    reader = csv.reader(f)
    for row in reader: 
        print(row)

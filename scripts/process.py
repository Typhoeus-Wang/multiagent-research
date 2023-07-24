# import sqlite3

# con = sqlite3.connect("../db_app.db")
# cur = con.cursor()

# for row in cur.execute("SELECT * FROM record"):
#   print(row)

import sqlite3
import argparse
import json
import datetime

parser = argparse.ArgumentParser(prog='process.py', description='description')
parser.add_argument('pubkeys', metavar='N', nargs='+')
parser.add_argument('-o', default='output.csv')
parser.add_argument('-a', default='1000')
args = parser.parse_args()

pubkeys = args.pubkeys
placeholder = ', '.join(['?' for _ in pubkeys])

con = sqlite3.connect("../db_app.db")
cur = con.cursor()

print("== pubkeys == ")
for row in list(cur.execute("SELECT DISTINCT pubkey FROM record")):
  print(row[0])
print()

print("== processing ==")
# Open a file for writing
count = 0
with open(args.o, "w") as file:
  cmd = f"SELECT * FROM record \
          WHERE pubkey IN ({placeholder})" 

  for row in cur.execute(cmd, pubkeys):
    # Convert the row to a string
    id, kind, tags, pubkey, created_at, content = row
    data = json.loads(content)

    print(datetime.datetime.fromtimestamp(created_at), end='\t ')
    print(pubkey, end='\t')
    print(data[-1][0])

    if count == 0:
      header = 'pubkey,' + ','.join(data[0])
      file.write(header + "\n")

    for timestep in data[1:]:
      row_str = pubkey + ','
      row_str += ','.join(map(str, timestep))
      file.write(row_str + "\n")

    count += 1
# Close the database connection
con.close()

import sqlite3
import os
import json

f = os.path.dirname(os.path.abspath(__file__))
print(f)
conn = sqlite3.connect(os.path.join(f, "./seekers_personal.db"))
cur = conn.cursor()

cur.executescript(open('seekers_personal.sql', 'rU').read())
cur.executescript(open('experience.sql', 'rU').read())
cur.executescript(open('company.sql', 'rU').read())
cur.executescript(open('position.sql', 'rU').read())

for company in json.loads(open('companies.json').read()):
    cur.execute("""INSERT INTO company (name, url, formality, languages, locations, size)
                   VALUES ('{}','{}','{}','{}','{}','{}')""".format(
                   company['name'], company['url'], company['formality'],
                   ','.join(company['languages']), ','.join(company['locations']), company['size']))

for position in json.loads(open(os.path.join(f, 'positions.json')).read()):
    cur.execute("""INSERT INTO position (positionname, companyname, positionlength, positiontype, address, companyurl, blurb)
                   VALUES ('{}','{}','{}','{}','{}','{}', '{}')""".format(
                   position['positionname'], position['companyname'], position['positionlength'], position['positiontype'],
                   position['address'], position['companyurl'], position['blurb']))

conn.commit()
cur.close()
conn.close()

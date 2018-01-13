import sqlite3
import json

conn = sqlite3.connect('./seekers_personal.db')
cur = conn.cursor()

cur.executescript(open('seekers_personal.sql', 'rU').read())
cur.executescript(open('reviews.sql', 'rU').read())
cur.executescript(open('company.sql', 'rU').read())
cur.executescript(open('position.sql', 'rU').read())

for company in json.loads(open('companies.json').read()):
    cur.execute("""INSERT INTO company (name, url, formality, languages, locations, size)
                   VALUES ('{}','{}','{}','{}','{}','{}')""".format(
                   company['name'], company['url'], company['formality'],
                   ','.join(company['languages']), ','.join(company['locations']), company['size']))

conn.commit()
cur.close()
conn.close()

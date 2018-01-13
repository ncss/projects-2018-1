import sqlite3
import json

conn = sqlite3.connect('./seekers_personal.db')
cur = conn.cursor()

cur.executescript(open('database/seekers_personal.sql', 'rU').read())
cur.executescript(open('database/reviews.sql', 'rU').read())
cur.executescript(open('database/company.sql', 'rU').read())

for company in json.loads(open('database/companies.json').read()):
    cur.execute("""INSERT INTO company (name, url, formality, finance, difficulty, size)
                   VALUES ('{}','{}','{}','{}','{}','{}')""".format(
                   company['name'], company['url'], company['formality'],
                   company['finance'], company['difficulty'], company['size']))

conn.commit()
cur.close()
conn.close()

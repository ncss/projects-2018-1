import sqlite3
conn = sqlite3.connect('../seekers_personal.db')
cur = conn.cursor()

cur.executescript(open('database/seekers_personal.sql', 'rU').read())
cur.executescript(open('database/experience.sql', 'rU').read())
conn.commit()
cur.close()
conn.close()

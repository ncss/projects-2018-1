import sqlite3
conn = sqlite3.connect('database/seekers_personal.db')
cur = conn.cursor()

cur.executescript(open('databse/seekers_personal.sql', 'rU').read())
cur.executescript(open('databe/experience.sql', 'rU').read())
conn.commit()
cur.close()
conn.close()

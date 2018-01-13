import sqlite3
import json
conn = sqlite3.connect('database/seekers_personal.db')
cur = conn.cursor()

cur.executescript(open('database/company.sql', 'rU').read())
conn.commit()


companyData = [
    {
        "id" = 0,
        "name" = "Google",
    },
    {
        "": ""
    },
]


cur.close()
conn.close()

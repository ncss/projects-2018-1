import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE seekers_personal (
    id INTEGER NOT NULL,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    phone INTEGER NOT NULL,
    email TEXT NOT NULL,
    city TEXT NOT NULL,
    education TEXT NOT NULL,
    hobbies TEXT NOT NULL,
    skills TEXT NOT NULL,
    experiences TEXT NOT NULL,
    PRIMARY KEY (id)
);"""
)
#print("""INSERT INTO seekers_personal (id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
#            VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.id, self.fname, self.lname, self.birth_date, self.phone, self.email, self.city, self.education, self.hobbies, self.skills, self.experiences))
cur.execute("""INSERT INTO seekers_personal (id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
            VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(1, "James", "Curran", "1/1/2000", "000", "james@ncss.com", "abc", "abc", "abc", "abc", "abc"))
for line in cur:
    print(line)
conn.commit()
cur.close()
conn.close()
print('==================')
conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute("SELECT * FROM seekers_personal;")
info = []
for line in cur:
    print(line)
cur.close()
conn.close()

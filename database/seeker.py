import sqlite3
# move this to createdatabase file.
"""
conn = sqlite3.connect('seekers_personal.db')
cur = conn.cursor()

cur.execute(CREATE TABLE seekers_personal (
    id INTEGER AUTOINCREMENT NOT NULL,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    city TEXT NOT NULL,
    education TEXT NOT NULL,
    hobbies TEXT NOT NULL,
    skills TEXT NOT NULL,
    experiences TEXT NOT NULL,
    PRIMARY KEY (id));)

conn.commit()
cur.close()
conn.close()
"""


class Seeker(object):
    """Person searching for work experience."""
    def __init__(self, fname, lname, birthdate, phone, email, city, education, hobbies, skills, experiences):
        self.fname = fname
        self.lname = lname
        self.birth_date = birthdate
        self.phone = phone
        self.email = email
        self.city = city
        self.education = education
        self.hobbies = hobbies
        self.skills = skills
        self.experiences = experiences

    def upload_seeker(self,id):
        """Stores seeker information in the database"""
        conn = sqlite3.connect('seekers_personal.db')
        cur = conn.cursor()
        #print("""INSERT INTO seekers_personal (id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
        #            VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.id, self.fname, self.lname, self.birth_date, self.phone, self.email, self.city, self.education, self.hobbies, self.skills, self.experiences))
        cur.execute("""INSERT INTO seekers_personal (fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
                    VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.fname, self.lname, self.birth_date, self.phone, self.email, self.city, self.education, self.hobbies, self.skills, self.experiences))

        conn.commit()
        cur.close()
        conn.close()


#Find the seeker with specific id and return information
def get_seeker(id):
    """Returns information about a seeker from the database."""
    conn = sqlite3.connect('seekers_personal.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM seekers_personal WHERE id = ?;",(id,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences = row
    user = Seeker(fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
    return user

def create_seeker(info):
    """Creates a new seeker."""
    fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences = info
    user = Seeker(fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
    user.upload_seeker(id)



#cur.close()
#conn.close()
#create DB call in sepereate files (createdatabse file)
# class function to create user (INSERT INTO etc.)
# class function to get user from db

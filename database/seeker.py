import sqlite3
# move this to createdatabase file.
conn = sqlite3.connect('seekers_personal.db')
cur = conn.cursor()


class Seeker(object):
    """Person searching for work experience."""
    def __init__(self, id, fname, lname, birthdate, phone, email, city, education, hobbies, skills, experiences):
        self.id = id
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

    def new_user(self):
        conn = sqlite3.connect('seekers_personal.db')
        cur = conn.cursor()
        print("""INSERT INTO seekers_personal (id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
                    VALUES ('{}','{}'.'{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.id, self.fname, self.lname, self.birth_date, self.phone, self.email, self.city, self.education, self.hobbies, self.skills, self.experiences))
        cur.execute("""INSERT INTO seekers_personal (id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
                    VALUES ('{}','{}'.'{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.id, self.fname, self.lname, self.birth_date, self.phone, self.email, self.city, self.education, self.hobbies, self.skills, self.experiences))
        print(self.id)
        cur.close()
        conn.close()
cur.close()
conn.close()
#create DB call in sepereate files (createdatabse file)
# class function to create user (INSERT INTO etc.)
# class function to get user from db

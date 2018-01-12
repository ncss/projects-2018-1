import sqlite3
# move this to createdatabase file.
conn = sqlite3.connect('seekers_personal.db')
cur = conn.cursor()

cur.execute("")

cur.close()
conn.close()

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
#create DB call in sepereate files (createdatabse file)
# class function to create user (INSERT INTO etc.)
# class function to get user from db

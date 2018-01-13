import sqlite3
from position import *

class Review(object):
    def __init__(self, rating, content, person_id, position_id, id=None):
        self.id = id
        self.rating = rating
        self.content = content
        self.person_id = person_id
        self.position_id = position_id

    def __str__(self):
        return "id: {}, rating: {}, content: {}, person_id: {}, position_id: {}".format(self.id, self.rating, self.content, self.person_id, self.position_id)


    def save(self):
        conn = sqlite3.connect('./seekers_personal.db')
        cur = conn.cursor()
        cur.execute("""INSERT INTO reviews (rating, content, person_id, position_id)
        VALUES (?, ?, ?, ?)""", (self.rating, self.content, self.person_id, self.position_id))
        self.id = cur.lastrowid
        conn.commit()
        cur.close()
        conn.close()


class Seeker(object):
    """Person searching for work experience."""
    def __init__(self, fname, lname, birthdate, phone, email, city, education, hobbies, skills, username, password, bio, id = None):
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
        self.reviews = []
        self.username = username
        self.password = password
        self.bio = bio
    def __str__(self):

        return "fname: '{}', lname: '{}', birthdate: '{}', phone: '{}', email: '{}', city: '{}', eductaion: '{}', hobbies: '{}', skills: '{}', id: '{}', reviews: '{}', username: '{}', password: '{}', bio: '{}'".format(self.fname, self.lname, self.birth_date, self.phone, self.email, self.city, self.education, self.hobbies, self.skills, self.id, self.reviews, self.username, self.password, self.bio)

    def add_review(self,rating, content, position_id):

        rev = Review(rating, content, self.id, position_id)
        rev.save()
        self.reviews.append(rev.id)

#Find the seeker with specific id and return information
def get_seeker(id):
    """Returns information about a seeker from the database."""
    conn = sqlite3.connect('./seekers_personal.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM seekers_personal WHERE id = ?;",(id,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if row == None:
        return None
    id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, username, password, bio = row
    user = Seeker(fname, lname, birth_date, phone, email, city, education, hobbies, skills, username, password, bio, id)
    return user



def create_seeker(info):
    """Creates a new seeker."""
    fname, lname, birth_date, phone, email, city, education, hobbies, skills, username, password, bio = info
    user = Seeker(fname, lname, birth_date, phone, email, city, education, hobbies, skills, username, password, bio)
    conn = sqlite3.connect('./seekers_personal.db')
    cur = conn.cursor()
    #print("""INSERT INTO seekers_personal (id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
    #            VALUES ('?','?','?','?','?','?','?','?','?','?','?')""".format(self.id, self.fname, self.lname, self.birth_date, self.phone, self.email, self.city, self.education, self.hobbies, self.skills, self.experiences))
    cur.execute("""INSERT INTO seekers_personal (fname, lname, birth_date, phone, email, city, education, hobbies, skills, username, password, bio)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?);""",(fname, lname, birth_date, phone, email, city, education, hobbies, skills, username, password, bio))
    user.id = cur.lastrowid
    conn.commit()
    cur.close()
    conn.close()

def get_review(id):
    """Returns information about an experience from the database."""
    conn = sqlite3.connect('./seekers_personal.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM reviews WHERE id = ?;",(id,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    id, rating, content, person_id, position_id = row
    rev = Review(rating, content, person_id, position_id, id)
    return rev

def get_seekers():
    conn = sqlite3.connect('./seekers_personal.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM seekers_personal;")

    info = []
    for row in cur:

        id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, username, password, bio = row
        user = Seeker(fname, lname, birth_date, phone, email, city, education, hobbies, skills, username, password, bio, id)
        info.append(user)

    conn.commit()
    cur.close()
    conn.close()

    return info

def get_review_by_position(position_id):
    conn = sqlite3.connect('./seekers_personal.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM reviews WHERE position_id=?;",(position_id,))

    info = []
    for row in cur:
        id, rating, content, person_id, position_id = row
        review = Review(rating, content, person_id, position_id)
        info.append(review)

    conn.commit()
    cur.close()
    conn.close()
    return info


#cur.close()
#conn.close()
#create DB call in sepereate files (createdatabse file)
# class function to create user (INSERT INTO etc.)
# class function to get user from db

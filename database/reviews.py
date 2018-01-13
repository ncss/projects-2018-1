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

def get_review(db_file, id):
    """Returns information about an experience from the database."""
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM reviews WHERE id = ?;",(id,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    id, rating, content, person_id, position_id = row
    rev = Review(rating, content, person_id, position_id, id)
    return rev

def get_review_by_position(db_file, position_id):
    conn = sqlite3.connect(db_file)
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

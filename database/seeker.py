import sqlite3

class Experience(object):
    def __init__(self, companyname, experiencetype, rating, person_id):
        self.id = None
        self.companyname = companyname
        self.experiencetype = experiencetype
        self.rating = rating
        self.person_id = person_id

    def save(self):
        conn = sqlite3.connect('../seekers_personal.db')
        cur = conn.cursor()
        cur.execute("""INSERT INTO experience (companyname, experiencetype, rating, person_id)
        VALUES (?, ?, ?, ?)""", (self.companyname, self.experiencetype, self.rating, self.person_id))
        self.id = cur.lastrowid
        conn.commit()
        cur.close()
        conn.close()


class Seeker(object):
    """Person searching for work experience."""
    def __init__(self, fname, lname, birthdate, phone, email, city, education, hobbies, skills, id = None):
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
        self.experiences = []
    def __str__(self):

        return "fname: {}, lname: {}, birthdate: {}, phone: {}, email: {}, city: {}, eductaion: {}, hobbies: {}, skills: {}, id: {}, experinces: {}".format(self.fname, self.lname, self.birth_date, self.phone, self.email, self.city, self.education, self.hobbies, self.skills, self.id, self.experiences)

    def add_experience(self, companyname, experiencetype, rating):

        exp = Experience(companyname, experiencetype, rating, self.id)
        exp.save()
        self.experiences.append(exp.id)

#Find the seeker with specific id and return information
def get_seeker(id):
    """Returns information about a seeker from the database."""
    conn = sqlite3.connect('../seekers_personal.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM seekers_personal WHERE id = ?;",(id,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    id, fname, lname, birth_date, phone, email, city, education, hobbies, skills = row
    user = Seeker(fname, lname, birth_date, phone, email, city, education, hobbies, skills, id)
    return user

def create_seeker(info):
    """Creates a new seeker."""
    fname, lname, birth_date, phone, email, city, education, hobbies, skills = info
    user = Seeker(fname, lname, birth_date, phone, email, city, education, hobbies, skills)
    conn = sqlite3.connect('../seekers_personal.db')
    cur = conn.cursor()
    #print("""INSERT INTO seekers_personal (id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
    #            VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.id, self.fname, self.lname, self.birth_date, self.phone, self.email, self.city, self.education, self.hobbies, self.skills, self.experiences))
    cur.execute("""INSERT INTO seekers_personal (fname, lname, birth_date, phone, email, city, education, hobbies, skills)
                VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(fname, lname, birth_date, phone, email, city, education, hobbies, skills))
    user.id = cur.lastrowid
    conn.commit()
    cur.close()
    conn.close()

def get_experience(id):
    """Returns information about an experience from the database."""
    conn = sqlite3.connect('../seekers_personal.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM experience WHERE id = ?;",(id,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    id, companyname, experiencetype, rating, person_id = row
    experience = Experience(companyname, experiencetype, rating, person_id)
    return experience


#cur.close()
#conn.close()
#create DB call in sepereate files (createdatabse file)
# class function to create user (INSERT INTO etc.)
# class function to get user from db

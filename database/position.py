import sqlite3

class Position(object):
    def __init__(self, positionname, companyname, positionlength, positiontype, address, companyurl, blurb):
        self.id = None
        self.positionname = positionname
        self.companyname = companyname
        self.positionlength = positionlength
        self.positiontype = positiontype
        self.address = address
        self.companyurl = companyurl
        self.blurb = blurb

def create_position(positioninfo):
    positionname, companyname, positionlength, positiontype, address, companyurl, blurb = positioninfo
    finalposition = Position(positionname, companyname, positionlength, positiontype, address, companyurl, blurb)
    conn = sqlite3.connect('./seekers_personal.db')
    cur = conn.cursor()
    #print("""INSERT INTO seekers_personal (id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
    #            VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.id, self.fname, self.lname, self.birth_date, self.phone, self.email, self.city, self.education, self.hobbies, self.skills, self.experiences))
    cur.execute("""INSERT INTO position (positionname, companyname, positionlength, positiontype, address, companyurl, blurb)
                VALUES (?,?,?,?,?,?,?);""", (positionname, companyname, positionlength, positiontype, address, companyurl, blurb))
    finalposition.id = cur.lastrowid
    conn.commit()
    cur.close()
    conn.close()

def get_position(id):
    conn = sqlite3.connect('./seekers_personal.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM position WHERE id = ?;",(id,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    id, positionname, companyname, positionlength, positiontype, address, companyurl, blurb = row
    finalposition = Position(positionname, companyname, positionlength, positiontype, address, companyurl, blurb)
    return finalposition

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
    def __str__(self):

        return "positionname: '{}', companyname: '{}', positionlength: '{}', positiontype: '{}', address: '{}', companyurl: '{}', blurb: '{}'".format(self.positionname,self.companyname, self.positionlength, self.positiontype, self.address, self.companyurl, self.blurb)

def create_position(db_file, positioninfo):
    positionname, companyname, positionlength, positiontype, address, companyurl, blurb = positioninfo
    finalposition = Position(positionname, companyname, positionlength, positiontype, address, companyurl, blurb)
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    #print("""INSERT INTO seekers_personal (id, fname, lname, birth_date, phone, email, city, education, hobbies, skills, experiences)
    #            VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(self.id, self.fname, self.lname, self.birth_date, self.phone, self.email, self.city, self.education, self.hobbies, self.skills, self.experiences))
    cur.execute("""INSERT INTO position (positionname, companyname, positionlength, positiontype, address, companyurl, blurb)
                VALUES (?,?,?,?,?,?,?);""", (positionname, companyname, positionlength, positiontype, address, companyurl, blurb))
    finalposition.id = cur.lastrowid
    conn.commit()
    cur.close()
    conn.close()

def get_position(db_file, id):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM position WHERE id = ?;",(id,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    id, positionname, companyname, positionlength, positiontype, address, companyurl, blurb = row
    finalposition = Position(positionname, companyname, positionlength, positiontype, address, companyurl, blurb)
    return finalposition

def return_all_positions(db_file):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM position;")

    allpositions = []

    for row in cur:
        id, positionname, companyname, positionlength, positiontype, address, companyurl, blurb = row
        position = Position(positionname, companyname, positionlength, positiontype, address, companyurl, blurb)
        allpositions.append(position)

    conn.commit()
    cur.close()
    conn.close()
    return allpositions

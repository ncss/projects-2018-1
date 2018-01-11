import sqlite3

CREATE TABLE seekers_personal (
    id INTEGER NOT NULL,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    gender TEXT NOT NULL,
    age INTEGER NOT NULL,
    phone INTEGER NOT NULL,
    email TEXT NOT NULL,
    city TEXT NOT NULL,
    education TEXT NOT NULL,
    PRIMARY KEY (id)
);

class Seeker(object):
    """Person searching for work experience."""
    def __init__(self, fname, lname, gender, age, phone, email, city, education):
        self.fname = "James"
        self.lname = "Curran"
        self.gender = 'Non-binary'
        self.age = 25
        self.phone = "000"
        self.email = "james@ncss.com"
        self.city = "Sydney"
        self.education = "University of Sydney"

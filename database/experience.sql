CREATE TABLE reviews (
    id INTEGER PRIMARY KEY NOT NULL,
    companyname TEXT NOT NULL,
    experiencetype TEXT NOT NULL,
    rating TEXT NOT NULL,
    content TEXT NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY (person_id) REFERENCES seekers_personal (id)
);

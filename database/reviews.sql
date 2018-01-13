CREATE TABLE reviews (
    id INTEGER PRIMARY KEY NOT NULL,
    rating TEXT NOT NULL,
    content TEXT NOT NULL,
    person_id INTEGER NOT NULL,
    position_id INTEGER NOT NULL,
    --add foreign key to position table
    FOREIGN KEY (person_id) REFERENCES seekers_personal (id)
);

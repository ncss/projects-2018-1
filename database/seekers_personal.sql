CREATE TABLE seekers_personal (
    id INTEGER PRIMARY KEY NOT NULL,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    city TEXT NOT NULL,
    education TEXT,
    hobbies TEXT,
    skills TEXT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    bio TEXT NOT NULL
);

-- Active: 1714029462031@@baza.fmf.uni-lj.si@5432@sem2024_mihaj
CREATE TABLE Oseba (
    username TEXT PRIMARY KEY,
    ime TEXT NOT NULL,
    priimek TEXT NOT NULL,
    kontakt_ig TEXT NOT NULL);
    
CREATE TABLE Uporabnik (
    username TEXT,
    role TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    last_login DATE,
    FOREIGN KEY (username) REFERENCES Oseba(username));    

CREATE TABLE Emotion (
    username1 TEXT,
    username2 TEXT,
    vrednost TEXT NOT NULL,
    CONSTRAINT check_vrednost CHECK (vrednost IN ('like', 'dislike', 'block')),
    FOREIGN KEY (username1) REFERENCES Oseba(username),
    FOREIGN KEY (username2) REFERENCES Oseba(username)
);
CREATE TABLE Vprasanje (
    id SERIAL PRIMARY KEY,
    vprasanje TEXT NOT NULL
);

CREATE TABLE Mozni_odgovor (
    id SERIAL PRIMARY KEY,
    mozni_odgovor TEXT NOT NULL,
    id_vprasanja INT,
    FOREIGN KEY (id_vprasanja) REFERENCES Vprasanje(id)
);

CREATE TABLE Odgovor (
    id SERIAL PRIMARY KEY,
    id_moznega_odgovora INT,
    username TEXT,
    FOREIGN KEY (id_moznega_odgovora) REFERENCES Mozni_odgovor(id),
    FOREIGN KEY (username) REFERENCES Oseba(username)
);





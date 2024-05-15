CREATE TABLE Uporabnik (
    id SERIAL PRIMARY KEY,
    ime TEXT NOT NULL,
    uporabnisko_ime TEXT NOT NULL UNIQUE,
    geslo TEXT NOT NULL,
    starost INT,
    fakulteta TEXT
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
    id_uporabnika INT,
    FOREIGN KEY (id_moznega_odgovora) REFERENCES Mozni_odgovor(id),
    FOREIGN KEY (id_uporabnika) REFERENCES Uporabnik(id)
);

CREATE TABLE OdgovorDTO (
    id SERIAL PRIMARY KEY,
    id_moznega_odgovora INT,
    id_uporabnika INT,
    odgovor TEXT NOT NULL,
    vprasanje TEXT NOT NULL,
    FOREIGN KEY (id_moznega_odgovora) REFERENCES Mozni_odgovor(id),
    FOREIGN KEY (id_uporabnika) REFERENCES Uporabnik(id)
);

CREATE TABLE Emotion (
    id_uporabnika1 INT,
    id_uporabnika2 INT,
    vrednost TEXT NOT NULL,
    CONSTRAINT check_vrednost CHECK (vrednost IN ('like', 'dislike', 'block')),
    FOREIGN KEY (id_uporabnika1) REFERENCES Uporabnik(id),
    FOREIGN KEY (id_uporabnika2) REFERENCES Uporabnik(id)
);
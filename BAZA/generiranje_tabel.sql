-- Active: 1714029462031@@baza.fmf.uni-lj.si@5432@sem2024_mihaj
CREATE TABLE Uporabnik (
    uporabnisko_ime TEXT PRIMARY KEY,
    ime TEXT NOT NULL,
    geslo TEXT NOT NULL
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
    username_uporabnika TEXT,
    FOREIGN KEY (id_moznega_odgovora) REFERENCES Mozni_odgovor(id),
    FOREIGN KEY (username_uporabnika) REFERENCES Uporabnik(uporabnisko_ime)
);

CREATE TABLE OdgovorDTO (
    id SERIAL PRIMARY KEY,
    id_moznega_odgovora INT,
    username_uporabnika TEXT,
    odgovor TEXT NOT NULL,
    vprasanje TEXT NOT NULL,
    FOREIGN KEY (id_moznega_odgovora) REFERENCES Mozni_odgovor(id),
    FOREIGN KEY (username_uporabnika) REFERENCES Uporabnik(uporabnisko_ime)
);

CREATE TABLE Emotion (
    username_uporabnika1 TEXT,
    username_uporabnika2 TEXT,
    vrednost TEXT NOT NULL,
    CONSTRAINT check_vrednost CHECK (vrednost IN ('like', 'dislike', 'block')),
    FOREIGN KEY (username_uporabnika1) REFERENCES Uporabnik(uporabnisko_ime),
    FOREIGN KEY (username_uporabnika2) REFERENCES Uporabnik(uporabnisko_ime)
);
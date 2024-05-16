-- Active: 1714029462031@@baza.fmf.uni-lj.si@5432@sem2024_mihaj
-- Insert 20 people into the Oseba table
INSERT INTO Oseba (emso, ime, priimek, kontakt_ig) VALUES
('1111111111111', 'Ana', 'Novak', 'ana_novak123'),
('2222222222222', 'Borut', 'Kralj', 'borut_king'),
('3333333333333', 'Cilka', 'Breznik', 'cilka_breznik'),
('4444444444444', 'David', 'Kos', 'david_kos'),
('5555555555555', 'Eva', 'Horvat', 'eva_horvat'),
('6666666666666', 'Franc', 'Majer', 'franc_majer'),
('7777777777777', 'Grega', 'Petek', 'grega_petek'),
('8888888888888', 'Helena', 'Kovač', 'helena_kovac'),
('9999999999999', 'Igor', 'Zajc', 'igor_zajc'),
('1010101010101', 'Jana', 'Novak', 'jana_novak'),
('1111111111110', 'Klara', 'Vidmar', 'klara_vidmar'),
('1212121212121', 'Lovro', 'Bizjak', 'lovro_bizjak'),
('1313131313131', 'Maja', 'Bohinc', 'maja_bohinc'),
('1414141414141', 'Nina', 'Rupnik', 'nina_rupnik'),
('1515151515151', 'Oskar', 'Petrič', 'oskar_petric'),
('1616161616161', 'Petra', 'Kralj', 'petra_kralj'),
('1717171717171', 'Rok', 'Pahor', 'rok_pahor'),
('1818181818181', 'Sara', 'Zorko', 'sara_zorko'),
('1919191919191', 'Tina', 'Urh', 'tina_urh'),
('2020202020202', 'Urban', 'Žagar', 'urban_zagar');
INSERT INTO Oseba (emso, ime, priimek, kontakt_ig) VALUES ('0909000500044', 'Miha', 'Jan', 'mihc');
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (1, '0909000500044'); -- Moški
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (3, '0909000500044');
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (11, '0909000500044');
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (13, '0909000500044');
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (20, '0909000500044');
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (28, '0909000500044');
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (32, '0909000500044');
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (38, '0909000500044');
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (39, '0909000500044');
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (45, '0909000500044');
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (53, '0909000500044');
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (72, '0909000500044');


-- Person 1: Ana Novak
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (1, '1111111111111'); -- Moški
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (3, '1111111111111'); -- K4
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (7, '1111111111111'); -- Foerster
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (10, '1111111111111'); -- Das ist Valter
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (15, '1111111111111'); -- Odbojka
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (17, '1111111111111'); -- Da
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (21, '1111111111111'); -- NUK
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (27, '1111111111111'); -- Kaotično
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (31, '1111111111111'); -- Rjava
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (34, '1111111111111'); -- One night stand
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (38, '1111111111111'); -- 20
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (50, '1111111111111'); -- FRI

-- Person 2: Borut Kralj
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (2, '2222222222222'); -- Ženska
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (4, '2222222222222'); -- Cirkus
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (8, '2222222222222'); -- Semafor
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (11, '2222222222222'); -- Dabuda
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (16, '2222222222222'); -- Fitnes
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (18, '2222222222222'); -- Ne
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (22, '2222222222222'); -- Biljard
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (28, '2222222222222'); -- Organizirano
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (32, '2222222222222'); -- Črna
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (35, '2222222222222'); -- Iščem bodočo Ženo/Moža
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (39, '2222222222222'); -- 21
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (51, '2222222222222'); -- FDV

-- Person 3: Cilka Breznik
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (1, '3333333333333'); -- Moški
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (5, '3333333333333'); -- Square
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (9, '3333333333333'); -- Castle
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (12, '3333333333333'); -- McDonald's
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (17, '3333333333333'); -- Joga
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (19, '3333333333333'); -- Da
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (23, '3333333333333'); -- Piknik v parku
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (29, '3333333333333'); -- Brezskrbno
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (33, '3333333333333'); -- Blond
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (36, '3333333333333'); -- Poletna romanca
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (40, '3333333333333'); -- 22
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (52, '3333333333333'); -- EF

-- Person 4: David Kos
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (2, '4444444444444'); -- Ženska
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (6, '4444444444444'); -- Tiffany
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (10, '4444444444444'); -- Nabrežje 15
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (13, '4444444444444'); -- Menza FE
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (18, '4444444444444'); -- Pilates
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (20, '4444444444444'); -- Ne
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (24, '4444444444444'); -- Atlantis
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (30, '4444444444444'); -- Nekje med A in B
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (34, '4444444444444'); -- One night stand
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (37, '4444444444444'); -- Drugo
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (41, '4444444444444'); -- 23
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (53, '4444444444444'); -- BF

-- Person 5: Eva Horvat
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (1, '5555555555555'); -- Moški
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (3, '5555555555555'); -- K4
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (7, '5555555555555'); -- Foerster
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (14, '5555555555555'); -- Foculus
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (15, '5555555555555'); -- Odbojka
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (17, '5555555555555'); -- Da
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (21, '5555555555555'); -- NUK
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (27, '5555555555555'); -- Kaotično
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (31, '5555555555555'); -- Rjava
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (34, '5555555555555'); -- One night stand
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (38, '5555555555555'); -- 24
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (54, '5555555555555'); -- ALUO

-- Person 6: Franc Majer
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (2, '6666666666666'); -- Ženska
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (4, '6666666666666'); -- Cirkus
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (8, '6666666666666'); -- Semafor
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (11, '6666666666666'); -- Dabuda
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (16, '6666666666666'); -- Fitnes
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (18, '6666666666666'); -- Ne
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (22, '6666666666666'); -- Biljard
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (28, '6666666666666'); -- Organizirano
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (32, '6666666666666'); -- Črna
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (35, '6666666666666'); -- Iščem bodočo Ženo/Moža
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (39, '6666666666666'); -- 25
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (55, '6666666666666'); -- FSD

-- Person 7: Grega Petek
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (1, '7777777777777'); -- Moški
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (5, '7777777777777'); -- Square
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (9, '7777777777777'); -- Castle
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (12, '7777777777777'); -- McDonald's
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (17, '7777777777777'); -- Joga
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (19, '7777777777777'); -- Da
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (23, '7777777777777'); -- Piknik v parku
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (29, '7777777777777'); -- Brezskrbno
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (33, '7777777777777'); -- Blond
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (36, '7777777777777'); -- Poletna romanca
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (40, '7777777777777'); -- 26
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (56, '7777777777777'); -- EF

-- Person 8: Helena Kovač
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (2, '8888888888888'); -- Ženska
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (6, '8888888888888'); -- Tiffany
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (10, '8888888888888'); -- Nabrežje 15
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (13, '8888888888888'); -- Menza FE
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (18, '8888888888888'); -- Pilates
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (20, '8888888888888'); -- Ne
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (24, '8888888888888'); -- Atlantis
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (30, '8888888888888'); -- Nekje med A in B
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (34, '8888888888888'); -- One night stand
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (37, '8888888888888'); -- Drugo
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (41, '8888888888888'); -- 27
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (57, '8888888888888'); -- BF

-- Person 9: Igor Zajc
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (1, '9999999999999'); -- Moški
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (3, '9999999999999'); -- K4
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (7, '9999999999999'); -- Foerster
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (14, '9999999999999'); -- Foculus
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (15, '9999999999999'); -- Odbojka
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (17, '9999999999999'); -- Da
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (21, '9999999999999'); -- NUK
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (27, '9999999999999'); -- Kaotično
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (31, '9999999999999'); -- Rjava
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (34, '9999999999999'); -- One night stand
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (38, '9999999999999'); -- 28
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (58, '9999999999999'); -- ALUO

-- Person 10: Jana Novak
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (2, '1010101010101'); -- Ženska
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (4, '1010101010101'); -- Cirkus
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (8, '1010101010101'); -- Semafor
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (11, '1010101010101'); -- Dabuda
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (16, '1010101010101'); -- Fitnes
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (18, '1010101010101'); -- Ne
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (22, '1010101010101'); -- Biljard
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (28, '1010101010101'); -- Organizirano
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (32, '1010101010101'); -- Črna
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (35, '1010101010101'); -- Iščem bodočo Ženo/Moža
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (39, '1010101010101'); -- 29
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (59, '1010101010101'); -- FSD

-- Še 10 ljudi
-- Person 11: Klara Vidmar
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (1, '1111111111110'); -- Moški
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (3, '1111111111110'); -- K4
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (7, '1111111111110'); -- Foerster
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (10, '1111111111110'); -- Das ist Valter
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (15, '1111111111110'); -- Odbojka
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (17, '1111111111110'); -- Da
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (21, '1111111111110'); -- NUK
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (27, '1111111111110'); -- Kaotično
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (31, '1111111111110'); -- Rjava
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (34, '1111111111110'); -- One night stand
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (38, '1111111111110'); -- 20
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (50, '1111111111110'); -- FRI

-- Person 12: Lovro Bizjak
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (2, '1212121212121'); -- Ženska
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (4, '1212121212121'); -- Cirkus
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (8, '1212121212121'); -- Semafor
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (11, '1212121212121'); -- Dabuda
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (16, '1212121212121'); -- Fitnes
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (18, '1212121212121'); -- Ne
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (22, '1212121212121'); -- Biljard
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (28, '1212121212121'); -- Organizirano
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (32, '1212121212121'); -- Črna
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (35, '1212121212121'); -- Iščem bodočo Ženo/Moža
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (39, '1212121212121'); -- 21
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (51, '1212121212121'); -- FDV

-- Person 13: Maja Bohinc
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (1, '1313131313131'); -- Moški
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (5, '1313131313131'); -- Square
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (9, '1313131313131'); -- Castle
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (12, '1313131313131'); -- McDonald's
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (17, '1313131313131'); -- Joga
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (19, '1313131313131'); -- Da
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (23, '1313131313131'); -- Piknik v parku
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (29, '1313131313131'); -- Brezskrbno
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (33, '1313131313131'); -- Blond
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (36, '1313131313131'); -- Poletna romanca
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (40, '1313131313131'); -- 22
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (52, '1313131313131'); -- EF

-- Person 14: Nina Rupnik
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (2, '1414141414141'); -- Ženska
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (6, '1414141414141'); -- Tiffany
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (10, '1414141414141'); -- Nabrežje 15
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (13, '1414141414141'); -- Menza FE
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (18, '1414141414141'); -- Pilates
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (20, '1414141414141'); -- Ne
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (24, '1414141414141'); -- Atlantis
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (30, '1414141414141'); -- Nekje med A in B
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (37, '1414141414141'); -- Drugo
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (41, '1414141414141'); -- 23
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (53, '1414141414141'); -- BF

-- Person 15: Oskar Petrič
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (1, '1515151515151'); -- Moški
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (3, '1515151515151'); -- K4
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (7, '1515151515151'); -- Foerster
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (14, '1515151515151'); -- Foculus
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (15, '1515151515151'); -- Odbojka
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (17, '1515151515151'); -- Da
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (21, '1515151515151'); -- NUK
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (27, '1515151515151'); -- Kaotično
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (31, '1515151515151'); -- Rjava
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (34, '1515151515151'); -- One night stand
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (38, '1515151515151'); -- 24
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (54, '1515151515151'); -- ALUO

-- Person 16: Petra Kralj
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (2, '1616161616161'); -- Ženska
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (4, '1616161616161'); -- Cirkus
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (8, '1616161616161'); -- Semafor
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (11, '1616161616161'); -- Dabuda
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (16, '1616161616161'); -- Fitnes
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (18, '1616161616161'); -- Ne
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (22, '1616161616161'); -- Biljard
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (28, '1616161616161'); -- Organizirano
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (32, '1616161616161'); -- Črna
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (35, '1616161616161'); -- Iščem bodočo Ženo/Moža
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (39, '1616161616161'); -- 25
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (55, '1616161616161'); -- FSD

-- Person 17: Rok Pahor
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (1, '1717171717171'); -- Moški
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (5, '1717171717171'); -- Square
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (9, '1717171717171'); -- Castle
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (12, '1717171717171'); -- McDonald's
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (17, '1717171717171'); -- Joga
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (19, '1717171717171'); -- Da
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (23, '1717171717171'); -- Piknik v parku
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (29, '1717171717171'); -- Brezskrbno
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (33, '1717171717171'); -- Blond
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (36, '1717171717171'); -- Poletna romanca
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (40, '1717171717171'); -- 26
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (56, '1717171717171'); -- EF

-- Person 18: Sara Zorko
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (2, '1818181818181'); -- Ženska
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (6, '1818181818181'); -- Tiffany
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (10, '1818181818181'); -- Nabrežje 15
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (13, '1818181818181'); -- Menza FE
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (18, '1818181818181'); -- Pilates
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (20, '1818181818181'); -- Ne
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (24, '1818181818181'); -- Atlantis
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (30, '1818181818181'); -- Nekje med A in B
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (34, '1818181818181'); -- One night stand
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (37, '1818181818181'); -- Drugo
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (41, '1818181818181'); -- 27
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (57, '1818181818181'); -- BF

-- Person 19: Tina Urh
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (1, '1919191919191'); -- Moški
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (3, '1919191919191'); -- K4
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (7, '1919191919191'); -- Foerster
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (14, '1919191919191'); -- Foculus
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (15, '1919191919191'); -- Odbojka
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (17, '1919191919191'); -- Da
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (21, '1919191919191'); -- NUK
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (27, '1919191919191'); -- Kaotično
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (31, '1919191919191'); -- Rjava
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (34, '1919191919191'); -- One night stand
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (38, '1919191919191'); -- 28
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (58, '1919191919191'); -- ALUO

-- Person 20: Urban Žagar
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (2, '2020202020202'); -- Ženska
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (4, '2020202020202'); -- Cirkus
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (8, '2020202020202'); -- Semafor
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (11, '2020202020202'); -- Dabuda
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (16, '2020202020202'); -- Fitnes
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (18, '2020202020202'); -- Ne
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (22, '2020202020202'); -- Biljard
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (28, '2020202020202'); -- Organizirano
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (32, '2020202020202'); -- Črna
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (35, '2020202020202'); -- Iščem bodočo Ženo/Moža
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (39, '2020202020202'); -- 29
INSERT INTO Odgovor (id_moznega_odgovora, emso) VALUES (59, '2020202020202'); -- FSD


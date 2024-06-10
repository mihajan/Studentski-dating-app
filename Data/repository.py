import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki
import Data.auth_public as auth
from Data.models import Oseba, OsebaDTO, OsebafullDTO, Emotion, Vprasanje, Mozni_odgovor, Odgovor, Uporabnik, UporabnikDto
from typing import List


## V tej datoteki bomo implementirali razred Repo, ki bo vseboval metode za delo z bazo.


class Repo:
    def __init__(self):
        # Ko ustvarimo novo instanco definiramo objekt za povezavo in cursor
        self.conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password, port=5432)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

 
#metode za pridobivanje oseb za različne uporabnike glede na njihov status
    def dobi_osebo(self, username: str) -> Oseba:
        '''
        Uporabljamo za spreminjanje Emotionov
        '''
        self.cur.execute("""
            SELECT username, ime, priimek, kontakt_ig
            FROM Oseba
            WHERE username = %s
        """, (username,))
        oseba = Oseba.from_dict(self.cur.fetchone())
        return oseba

#lahko bi meli samo fullDTO sam bi blo preveč za spreminjat
    def dobi_osebo_fullDTO(self, username: str) -> OsebafullDTO:
        '''
        Tako osebo vidijo matchi (vsi podatki kar jih imamo)
        (kličemo ko rabimo seznam matchov)
        '''
        # Pridobimo podatke o osebi
        self.cur.execute("""
            SELECT username, ime, priimek, kontakt_ig
            FROM Oseba
            WHERE username = %s
        """, (username,))
        oseba = self.cur.fetchone()
    
        if not oseba:
            return None  # Oseba ne obstaja
    
        ime = oseba['ime']
        priimek = oseba['priimek']
        kontakt_ig = oseba['kontakt_ig']
    
        # Pridobimo odgovore za določeno osebo skupaj z besedili vprašanj
        self.cur.execute("""
            SELECT v.vprasanje, mo.mozni_odgovor
            FROM Odgovor o
            JOIN Mozni_odgovor mo ON o.id_moznega_odgovora = mo.id
            JOIN Vprasanje v ON mo.id_vprasanja = v.id
            WHERE o.username = %s
            ORDER BY o.id
        """, (username,))
        
        results = self.cur.fetchall()
        odgovori = {row['vprasanje']: row['mozni_odgovor'] for row in results}
    
        # Ustvarimo OsebafullDTO
        oseba_full_dto = OsebafullDTO(
            username=username,
            ime=ime,
            priimek=priimek,
            kontakt_ig=kontakt_ig,
            odgovori=odgovori
        )
    
        return oseba_full_dto
       
    def dobi_oseboDTO(self, username: str) -> OsebaDTO:
        '''
        Tako osebo vidiš na searchu, like in dislike
        (kličemo ko rabimo sezname oseb na zgornjih seznamih)
        '''
        # podatki o osebi
        self.cur.execute("""
            SELECT username, ime
            FROM Oseba
            WHERE username = %s
        """, (username,))
        oseba = self.cur.fetchone()

        ime = oseba['ime']

        # Odgovori za osebo skupaj z besedili vprašanj
        self.cur.execute("""
            SELECT v.vprasanje, mo.mozni_odgovor
            FROM Odgovor o
            JOIN Mozni_odgovor mo ON o.id_moznega_odgovora = mo.id
            JOIN Vprasanje v ON mo.id_vprasanja = v.id
            WHERE o.username = %s
            ORDER BY o.id
        """, (username,))

        results = self.cur.fetchall()
        odgovori = {row['vprasanje']: row['mozni_odgovor'] for row in results}

        # Ustvarimo  OsebaDTO
        oseba_dto = OsebaDTO(
            username=username,
            ime=ime,
            odgovori=odgovori
        )

        return oseba_dto
    
#-----------------------------------------------------------------------------------------------------    
#metode za vprašanja in odgovore
    def dodaj_vprasanje(self, vprasanje: Vprasanje):
        '''
        Doda novo vprašanje
        '''
        self.cur.execute("""
            INSERT INTO Vprasanje (vprasanje)
            VALUES (%s)
        """, (vprasanje.vprasanje,))
        self.conn.commit()  

    def izbrisi_vprasanje(self, vprasanje_id: int):
        '''
        Izbriše vprašanje
        '''
        self.cur.execute("""
            DELETE FROM Vprasanje
            WHERE id = %s
        """, (vprasanje_id,))
        self.conn.commit()     

    def dobi_vprasanja(self) -> List[Vprasanje]:
        '''
        Dobi vsa vprašanja
        '''
        self.cur.execute("""
            SELECT id, vprasanje
            FROM Vprasanje
        """)
        vprasanja = [Vprasanje.from_dict(t) for t in self.cur.fetchall()]
        return vprasanja

    def dobi_mozne_odgovore(self, id_vprasanja: int) -> List[Mozni_odgovor]:
        '''
        Pridobi vse možne odgovore za določeno vprašanje
        '''
        self.cur.execute("""
            SELECT id, mozni_odgovor, id_vprasanja
            FROM Mozni_odgovor
            WHERE id_vprasanja = %s
        """, (id_vprasanja,))
        mozni_odgovori = [Mozni_odgovor.from_dict(t) for t in self.cur.fetchall()]
        return mozni_odgovori
    
    def izbrisi_odgovore_osebe(self, username: str) -> None:
        """
        Izbriše vse odgovore za podano osebo.
        """
        self.cur.execute("""
            DELETE FROM Odgovor
            WHERE username = %s
        """, (username,))
        self.conn.commit()

    def dodaj_mozni_odgovor(self, mozni_odgovor: Mozni_odgovor) -> None:
        '''
        Doda nov možni odgovor (id se sam nardi)
        '''
        self.cur.execute("""
            INSERT INTO Mozni_odgovor (mozni_odgovor, id_vprasanja)
            VALUES (%s, %s)
        """, (mozni_odgovor.mozni_odgovor, mozni_odgovor.id_vprasanja))
        self.conn.commit()

    def dodaj_odgovor(self, odgovor: Odgovor) -> None:
        '''
        Zapiše kaj je odgovoril user
        '''
        self.cur.execute("""
            INSERT INTO Odgovor (id_moznega_odgovora, username)
            VALUES (%s, %s)
        """, (odgovor.id_moznega_odgovora, odgovor.username))
        self.conn.commit()

#-----------------------------------------------------------------------------------------------------
#Metode, ki se nanašajo na emotione 
    def spremeni_emotion(self, oseba1: Oseba, oseba2: Oseba, vrednost: str) -> None:
        '''
        Spremeni ali doda vrednost za podan par v tabeli Emotion.
        Vrednost je lahko 'like', 'dislike'
        '''
        if vrednost not in ['like', 'dislike', 'block']:
            raise ValueError("Vrednost mora biti 'like' ali 'dislike'")

        self.cur.execute("""
            SELECT 1 FROM Emotion WHERE username1 = %s AND username2 = %s
        """, (oseba1.username, oseba2.username))
        
        if self.cur.fetchone():
            # Če vrstica obstaja, posodobimo vrednost
            self.cur.execute("""
                UPDATE Emotion 
                SET vrednost = %s 
                WHERE username1 = %s AND username2 = %s
            """, (vrednost, oseba1.username, oseba2.username))
        else:
            # Če vrstica ne obstaja, dodamo novo vrstico
            self.cur.execute("""
                INSERT INTO Emotion (username1, username2, vrednost)
                VALUES (%s, %s, %s)
            """, (oseba1.username, oseba2.username, vrednost))
        
        self.conn.commit()   

    def oseba_matchi(self, username: str) -> List[str]:
        '''
        Vrne seznam usernamov matchov za dano osebo
        '''
        self.cur.execute("""
            SELECT e1.username2 AS match_username
            FROM Emotion e1
            JOIN Emotion e2 ON e1.username2 = e2.username1
            WHERE e1.username1 = %s AND e1.vrednost = 'like' AND e2.vrednost = 'like' AND e2.username2 = %s
        """, (username, username))
        
        results = self.cur.fetchall()
        matchi = [row['match_username'] for row in results]
        return matchi  

    def oseba_like(self, username: str) -> List[str]:
        '''
        Vrne seznam usernamov oseb, ki smo jim dali "like" vendar ni matcha
        '''
        self.cur.execute("""
            SELECT e1.username2 AS liked_username
            FROM Emotion e1
            LEFT JOIN Emotion e2 ON e1.username2 = e2.username1 AND e2.username2 = e1.username1
            WHERE e1.username1 = %s AND e1.vrednost = 'like' AND (e2.vrednost IS NULL OR e2.vrednost != 'like')
        """, (username,))
        
        results = self.cur.fetchall()
        likes = [row['liked_username'] for row in results]
        return likes

    def oseba_dislike(self, username: str) -> List[str]:
        '''
        Vrne seznam usernamov oseb, ki jim dali "dislike"
        '''
        self.cur.execute("""
            SELECT username2 AS disliked_username
            FROM Emotion
            WHERE username1 = %s AND vrednost = 'dislike'
        """, (username,))
        
        results = self.cur.fetchall()
        dislikes = [row['disliked_username'] for row in results]
        return dislikes

    def oseba_brezstika(self, username: str) -> List[str]:
        '''
        Vrne seznam usernamov vseh oseb, s katerimi nismo bili še v stiku
        Izključi uporabnike z vlogo "admin"
        '''
        # Najprej pridobimo vse usernamove, ki imajo vlogo admin
        self.cur.execute("""
            SELECT username
            FROM Uporabnik
            WHERE role = 'admin'
        """)
        admin_usernames = [row['username'] for row in self.cur.fetchall()]

        # Sedaj pridobimo vse usernamove, s katerimi nismo bili še v stiku in izključimo admin uporabnike
        self.cur.execute("""
            SELECT o.username
            FROM Oseba o
            WHERE o.username != %s
            AND o.username NOT IN (
                SELECT e.username2
                FROM Emotion e
                WHERE e.username1 = %s
            )
        """, (username, username))

        results = self.cur.fetchall()
        usernames = [row['username'] for row in results if row['username'] not in admin_usernames]
        return usernames

#-------------------------------------------------------------------------------------------------------
#metode, ki jih bova dejansko klicala (vrnejo vse osebe za določen seznam za našga userja)
    def dobi_like_osebeDTO(self, username: str) -> List[OsebaDTO]:
        '''
        Za podan username prikaže vse ki bodo na prikazani pod like.
        '''
        # Najprej pridobimo seznam usernamov oseb, ki jih je dana oseba "like"
        liked_usernames = self.oseba_like(username)

        oseba_dto_list = []
        for liked_username in liked_usernames:
            oseba_dto = self.dobi_oseboDTO(liked_username)
            if oseba_dto:
                oseba_dto_list.append(oseba_dto)
        return oseba_dto_list

    def dobi_dislike_osebeDTO(self, username: str) -> List[OsebaDTO]:
        '''
        Za podan username prikaže vse ki bodo na prikazani pod dislike.
        '''
        # Najprej pridobimo seznam usernamov oseb, ki jih je dana oseba dislikala
        disliked_usernames = self.oseba_dislike(username)

        oseba_dto_list = []
        for disliked_username in disliked_usernames:
            oseba_dto = self.dobi_oseboDTO(disliked_username)
            if oseba_dto:
                oseba_dto_list.append(oseba_dto)
        return oseba_dto_list
    
    def dobi_brezstika_osebeDTO(self, username: str) -> List[OsebaDTO]:
        '''
        Za podan username prikaže vse ki bodo na prikazani na prvotni strani
        oz jih še nismo nič reactal
        '''
        # Najprej pridobimo seznam usernamov oseb, ki jih je dana oseba dislikala
        usernames = self.oseba_brezstika(username)

        oseba_dto_list = []
        for username in usernames:
            oseba_dto = self.dobi_oseboDTO(username)
            if oseba_dto:
                oseba_dto_list.append(oseba_dto)
        return oseba_dto_list    
    
    def dobi_matche_osebefullDTO(self, username: str) -> List[OsebafullDTO]:
        '''
        Za podan username prikaže vse ki bodo na prikazani pod matchi.
        '''
        # Najprej pridobimo seznam usernamov oseb, ki jih je dana oseba matchala
        matched_usernames = self.oseba_matchi(username)

        oseba_dto_list = []
        for matched_username in matched_usernames:
            oseba_dto = self.dobi_osebo_fullDTO(matched_username)
            if oseba_dto:
                oseba_dto_list.append(oseba_dto)
        return oseba_dto_list

#-------------------------------------------------------------------------------------------------------
#Metode za upravljanje uporabnikov
    def dodaj_osebo(self, oseba: Oseba):
        '''Dodamo osebo; še prej preverimo če tak username še ne obstaja'''
        try:
            # Preverimo, če oseba že obstaja
            self.cur.execute("""
                SELECT COUNT(*) FROM Oseba WHERE username = %s
            """, (oseba.username,))
            if self.cur.fetchone()[0] > 0:
                raise ValueError("Oseba z enakim uporabniškim imenom že obstaja.")
            
            # Če oseba ne obstaja, jo dodamo
            self.cur.execute("""
                INSERT INTO Oseba (username, ime, priimek, kontakt_ig)
                VALUES (%s, %s, %s, %s)
            """, (oseba.username, oseba.ime, oseba.priimek, oseba.kontakt_ig))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(f"Oseba z takim usernamom {e} že obstaja!!")
            raise e

    def dodaj_uporabnika(self, uporabnik: Uporabnik):
        self.cur.execute("""
            INSERT into Uporabnik(username, role, password_hash, last_login)
            VALUES (%s, %s, %s, %s)
            """, (uporabnik.username,uporabnik.role, uporabnik.password_hash, uporabnik.last_login))
        self.conn.commit()

    def dobi_uporabnika(self, username:str) -> Uporabnik:
        self.cur.execute("""
            SELECT username, role, password_hash, last_login
            FROM uporabnik
            WHERE username = %s
        """, (username,))
         
        u = Uporabnik.from_dict(self.cur.fetchone())
        return u
    
    def posodobi_uporabnika(self, uporabnik: Uporabnik):
        self.cur.execute("""
            Update uporabnik set last_login = %s where username = %s
            """, (uporabnik.last_login,uporabnik.username))
        self.conn.commit()



#--------------------------------------
#brisanje vprašanj in možnih odgovorov

    def izbrisi_mozne_odgovore(self, id_vprasanja: int) -> None:
        '''
        Izbriše vse možne odgovore za podano vprašanje
        '''
        try:
            self.cur.execute("""
                DELETE FROM Mozni_odgovor
                WHERE id_vprasanja = %s
            """, (id_vprasanja,))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        
    
    def izbrisi_vprasanje(self, id_vprasanja: int) -> None:
        '''
        Izbriše vprašanje iz baze
        '''
        try:
            self.cur.execute("""
                DELETE FROM Vprasanje
                WHERE id = %s
            """, (id_vprasanja,))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        
    def izbrisi_odgovore_za_vprasanje(self, id_vprasanja: int) -> None:
        '''
        Izbriše vse vnose v tabeli Odgovor, ki se navezujejo na podano vprašanje
        '''
        try:
            self.cur.execute("""
                DELETE FROM Odgovor
                WHERE id_moznega_odgovora IN (
                    SELECT id
                    FROM Mozni_odgovor
                    WHERE id_vprasanja = %s
                )
            """, (id_vprasanja,))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

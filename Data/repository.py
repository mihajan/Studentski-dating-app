import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki
#import Data.auth_public as auth
#import auth_public as auth
import auth as auth

#from Data.Models import Oseba, Emotion, Vprasanje, Mozni_odgovor, Odgovor, OdgovorDTO
from Models import Oseba, Emotion, Vprasanje, Mozni_odgovor, Odgovor, OdgovorDTO, Uporabnik, UporabnikDto
from typing import List
import datetime

## V tej datoteki bomo implementirali razred Repo, ki bo vseboval metode za delo z bazo.

class Repo:
    def __init__(self):
        # Ko ustvarimo novo instanco definiramo objekt za povezavo in cursor
        self.conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password, port=5432)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def dobi_osebo(self, emso: str) -> Oseba:
        self.cur.execute("""
            SELECT emso, ime, priimek, kontakt_ig
            FROM Oseba
            WHERE emso = %s
        """, (emso,))
        oseba = Oseba.from_dict(self.cur.fetchone())
        return oseba

    def dobi_osebe(self) -> List[Oseba]:
        self.cur.execute("""
            SELECT ime, priimek
            FROM Oseba
        """)
        osebe = [Oseba.from_dict(t) for t in self.cur.fetchall()]
        return osebe
    

#Metode, ki se nanašajo na pridobivanje odgovorov.

    def dobi_odgovore_ids_za_osebo(self, emso: str) -> List[int]:
        '''
        Za določeno osebo vrne seznam idjev odgovorov na katere je oseba odgovorila
        '''
        self.cur.execute("""
            SELECT id_moznega_odgovora
            FROM Odgovor
            WHERE emso = %s
            ORDER BY id
        """, (emso,))
        
        results = self.cur.fetchall()
        answer_ids = [row["id_moznega_odgovora"] for row in results]
        return answer_ids
    


    def dobi_odgovore_texts_za_osebo(self, emso: str) -> List[str]:
        '''
        Za določeno osebo vrne seznam besedil odgovorov na katere je oseba odgovorila.
        '''
        self.cur.execute("""
            SELECT mo.mozni_odgovor
            FROM Odgovor o
            JOIN Mozni_odgovor mo ON o.id_moznega_odgovora = mo.id
            WHERE o.emso = %s
            ORDER BY o.id
        """, (emso,))
        
        results = self.cur.fetchall()
        answer_texts = [row['mozni_odgovor'] for row in results]
        return answer_texts


#Metode, ki se nanašajo na emotione 

    def spremeni_emotion(self, emso_oseba1: str, emso_oseba2: str, vrednost: str):
        '''
        Spremeni ali doda vrednost za podan par v tabeli Emotion.
        Vrednost je lahko 'like', 'dislike' ali 'block'.
        '''
        if vrednost not in ['like', 'dislike', 'block']:
            raise ValueError("Vrednost mora biti 'like', 'dislike' ali 'block'")

        self.cur.execute("""
            SELECT 1 FROM Emotion WHERE emso_oseba1 = %s AND emso_oseba2 = %s
        """, (emso_oseba1, emso_oseba2))
        
        if self.cur.fetchone():
            # Če vrstica obstaja, posodobimo vrednost
            self.cur.execute("""
                UPDATE Emotion 
                SET vrednost = %s 
                WHERE emso_oseba1 = %s AND emso_oseba2 = %s
            """, (vrednost, emso_oseba1, emso_oseba2))
        else:
            # Če vrstica ne obstaja, dodamo novo vrstico
            self.cur.execute("""
                INSERT INTO Emotion (emso_oseba1, emso_oseba2, vrednost)
                VALUES (%s, %s, %s)
            """, (emso_oseba1, emso_oseba2, vrednost))
        
        self.conn.commit()    

    def matchi_osebe(self, emso: str) -> List[str]:
        '''
        Vrne seznam matchov za dano osebo
        '''
        self.cur.execute("""
            SELECT e1.emso_oseba2 AS match_emso
            FROM Emotion e1
            JOIN Emotion e2 ON e1.emso_oseba2 = e2.emso_oseba1
            WHERE e1.emso_oseba1 = %s AND e1.vrednost = 'like' AND e2.vrednost = 'like' AND e2.emso_oseba2 = %s
        """, (emso, emso))
        
        results = self.cur.fetchall()
        matchi = [row['match_emso'] for row in results]
        return matchi  




#Metode za upravljanje uporabnikov

    def dodaj_uporabnika(self, uporabnik: Uporabnik):
        self.cur.execute("""
            INSERT into uporabniki(username, role, password_hash, last_login)
            VALUES (%s, %s, %s, %s)
            """, (uporabnik.username,uporabnik.role, uporabnik.password_hash, uporabnik.last_login))
        self.conn.commit()


    def dobi_uporabnika(self, username:str) -> Uporabnik:
        self.cur.execute("""
            SELECT username, role, password_hash, last_login
            FROM uporabniki
            WHERE username = %s
        """, (username,))
         
        u = Uporabnik.from_dict(self.cur.fetchone())
        return u
    
    def posodobi_uporabnika(self, uporabnik: Uporabnik):
        self.cur.execute("""
            Update uporabniki set last_login = %s where username = %s
            """, (uporabnik.last_login,uporabnik.username))
        self.conn.commit()

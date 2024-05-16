import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki
#import Data.auth_public as auth
#import auth_public as auth
import auth as auth

#from Data.Models import Oseba, Emotion, Vprasanje, Mozni_odgovor, Odgovor, OdgovorDTO
from Models import Oseba, Emotion, Vprasanje, Mozni_odgovor, Odgovor, OdgovorDTO
from typing import List

## V tej datoteki bomo implementirali razred Repo, ki bo vseboval metode za delo z bazo.

class Repo:
    def __init__(self):
        # Ko ustvarimo novo instanco definiramo objekt za povezavo in cursor
        self.conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password, port=5432)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def dobi_osebe(self) -> List[Oseba]:
        self.cur.execute("""
            SELECT emso, ime, priimek, kontakt_ig
            FROM Oseba
        """)
        osebe = [Oseba.from_dict(t) for t in self.cur.fetchall()]
        return osebe
    
    def dobi_odgovore_za_osebo(self, emso: str) -> List[dict]:
        self.cur.execute("""
            SELECT v.vprasanje, mo.mozni_odgovor
            FROM Odgovor o
            JOIN Mozni_odgovor mo ON o.id_moznega_odgovora = mo.id
            JOIN Vprasanje v ON mo.id_vprasanja = v.id
            WHERE o.emso = %s
            ORDER BY v.id
        """, (emso,))
        
        results = self.cur.fetchall()
        answers = [{"question": row["vprasanje"], "answer": row["mozni_odgovor"]} for row in results]
        return answers
    
    def dobi_odgovore_ids_za_osebo(self, emso: str) -> List[int]:
        self.cur.execute("""
            SELECT o.id_moznega_odgovora
            FROM Odgovor o
            WHERE o.emso = %s
            ORDER BY o.id
        """, (emso,))
        
        results = self.cur.fetchall()
        answer_ids = [row["id_moznega_odgovora"] for row in results]
        return answer_ids
    
    def dobi_odgovore_texts_za_osebo(self, emso: str) -> List[str]:
        self.cur.execute("""
            SELECT mo.mozni_odgovor
            FROM Odgovor o
            JOIN Mozni_odgovor mo ON o.id_moznega_odgovora = mo.id
            WHERE o.emso = %s
            ORDER BY o.id
        """, (emso,))
        
        results = self.cur.fetchall()
        answer_texts = [row["mozni_odgovor"] for row in results]
        return answer_texts
    
    def dodaj_emotion_like(self, emso_oseba1: str, emso_oseba2: str):
        self.cur.execute("""
            SELECT * FROM Emotion WHERE emso_oseba1 = %s AND emso_oseba2 = %s
        """, (emso_oseba1, emso_oseba2))
        
        if self.cur.fetchone():
            self.cur.execute("""
                UPDATE Emotion 
                SET vrednost = %s 
                WHERE emso_oseba1 = %s AND emso_oseba2 = %s
            """, ('like', emso_oseba1, emso_oseba2))
        else:
            self.cur.execute("""
                INSERT INTO Emotion (emso_oseba1, emso_oseba2, vrednost)
                VALUES (%s, %s, %s)
            """, (emso_oseba1, emso_oseba2, 'like'))
        
        self.conn.commit()

    def dodaj_emotion_dislike(self, emso_oseba1: str, emso_oseba2: str):
        self.cur.execute("""
            SELECT * FROM Emotion WHERE emso_oseba1 = %s AND emso_oseba2 = %s
        """, (emso_oseba1, emso_oseba2))
        
        if self.cur.fetchone():
            self.cur.execute("""
                UPDATE Emotion 
                SET vrednost = %s 
                WHERE emso_oseba1 = %s AND emso_oseba2 = %s
            """, ('dislike', emso_oseba1, emso_oseba2))
        else:
            self.cur.execute("""
                INSERT INTO Emotion (emso_oseba1, emso_oseba2, vrednost)
                VALUES (%s, %s, %s)
            """, (emso_oseba1, emso_oseba2, 'dislike'))
        
        self.conn.commit()

    def dodaj_emotion_block(self, emso_oseba1: str, emso_oseba2: str):
        self.cur.execute("""
            SELECT * FROM Emotion WHERE emso_oseba1 = %s AND emso_oseba2 = %s
        """, (emso_oseba1, emso_oseba2))
        
        if self.cur.fetchone():
            self.cur.execute("""
                UPDATE Emotion 
                SET vrednost = %s 
                WHERE emso_oseba1 = %s AND emso_oseba2 = %s
            """, ('block', emso_oseba1, emso_oseba2))
        else:
            self.cur.execute("""
                INSERT INTO Emotion (emso_oseba1, emso_oseba2, vrednost)
                VALUES (%s, %s, %s)
            """, (emso_oseba1, emso_oseba2, 'block'))
        
        self.conn.commit()
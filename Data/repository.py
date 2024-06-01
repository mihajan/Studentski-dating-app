import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki
#import Data.auth_public as auth
#import auth_public as auth
import auth as auth

#from Data.Models import Oseba, Emotion, Vprasanje, Mozni_odgovor, Odgovor, OdgovorDTO
from Models import Oseba, OsebaDTO, OsebafullDTO, Emotion, Vprasanje, VprasanjeDTO, Mozni_odgovor, Mozni_odgovorDTO,Odgovor, OdgovorDTO, Uporabnik, UporabnikDto
from typing import List
import datetime

## V tej datoteki bomo implementirali razred Repo, ki bo vseboval metode za delo z bazo.

class Repo:
    def __init__(self):
        # Ko ustvarimo novo instanco definiramo objekt za povezavo in cursor
        self.conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password, port=5432)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#metode za 

#metode za pridobivanje oseb za različne uporabnike glede na njihov status
    def dobi_osebo(self, username: str) -> Oseba:
        '''Tako vidiš sebe'''
        self.cur.execute("""
            SELECT username, ime, priimek, kontakt_ig
            FROM Oseba
            WHERE username = %s
        """, (username,))
        oseba = Oseba.from_dict(self.cur.fetchone())
        return oseba
    
    def dobi_osebo_fullDTO(self, username: str) -> OsebafullDTO:
        '''
        Tako osebo vidijo matchi (vsi podatki kar jih imamo)
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

        # Pridobimo odgovore za določeno osebo
        self.cur.execute("""
            SELECT mo.mozni_odgovor
            FROM Odgovor o
            JOIN Mozni_odgovor mo ON o.id_moznega_odgovora = mo.id
            WHERE o.username = %s
            ORDER BY o.id
        """, (username,))
        
        results = self.cur.fetchall()
        answer_texts = [row['mozni_odgovor'] for row in results]

        # Ustvarimo instanco razreda OsebafullDTO
        oseba_full_dto = OsebafullDTO(
            username=username,
            ime=ime,
            priimek=priimek,
            kontakt_ig=kontakt_ig,
            odgovori=answer_texts
        )

        return oseba_full_dto    
    
    def dobi_oseboDTO(self, username: str) -> OsebaDTO:
        '''
        Tako osebo vidiš na searchu, like in dislike
        '''
        # Pridobimo podatke o osebi
        self.cur.execute("""
            SELECT username, ime
            FROM Oseba
            WHERE username = %s
        """, (username,))
        oseba = self.cur.fetchone()

        ime = oseba['ime']

        # Pridobimo odgovore za določeno osebo
        self.cur.execute("""
            SELECT mo.mozni_odgovor
            FROM Odgovor o
            JOIN Mozni_odgovor mo ON o.id_moznega_odgovora = mo.id
            WHERE o.username = %s
            ORDER BY o.id
        """, (username,))
        
        results = self.cur.fetchall()
        answer_texts = [row['mozni_odgovor'] for row in results]

        # Ustvarimo instanco razreda OsebaDTO
        oseba_dto = OsebaDTO(
            username=username,
            ime=ime,
            odgovori=answer_texts
        )

        return oseba_dto

#metode za vprašanja in odgovore
    def dobi_vprasanje(self, id: int) -> Vprasanje:
        '''
        Vrne celotno vprašanje z izbranim id
        '''
        self.cur.execute("""
            SELECT id, vprasanje
            FROM Vprasanje
            WHERE id = %s
        """, (id,))
        vprasanje = self.cur.fetchone()
        return Vprasanje.from_dict(vprasanje)

    def dobi_vprasanjeDTO(self, id: int) -> VprasanjeDTO:
        '''
        Vrne samo besedilo vprašanja
        '''
        self.cur.execute("""
            SELECT vprasanje
            FROM Vprasanje
            WHERE id = %s
        """, (id,))
        vprasanje = self.cur.fetchone()
        return VprasanjeDTO.from_dict(vprasanje)

    def dodaj_vprasanje(self, vprasanje: Vprasanje):
        '''
        Doda novo vprašanje
        '''
        self.cur.execute("""
            INSERT INTO Vprasanje (vprasanje)
            VALUES (%s)
        """, (vprasanje.vprasanje,))
        self.conn.commit()

    def dobi_mozni_odgovorDTO(self, id: int) -> Mozni_odgovorDTO:
        '''
        Vrne besedilo možnega odgovora za id
        '''
        self.cur.execute("""
            SELECT mozni_odgovor
            FROM Mozni_odgovor
            WHERE id = %s
        """, (id,))
        
        mozni_odgovor = self.cur.fetchone()
        return Mozni_odgovorDTO(mozni_odgovor=mozni_odgovor['mozni_odgovor'])    

    def dobi_mozni_odgovor(self, id: int) -> Mozni_odgovor:
        '''
        Vrne besedilo možnega odgovora za id
        '''
        self.cur.execute("""
            SELECT id, mozni_odgovor, id_vprasanja
            FROM Mozni_odgovor
            WHERE id = %s
        """, (id,))
        
        mozni_odgovor = self.cur.fetchone()
        return Mozni_odgovor(mozni_odgovor=mozni_odgovor['mozni_odgovor']) 

    def dodaj_mozni_odgovor(self, mozni_odgovor: str, id_vprasanja: int):
        '''
        Doda nov možni odgovor (id se sam nardi)
        '''
        self.cur.execute("""
            INSERT INTO Mozni_odgovor (mozni_odgovor, id_vprasanja)
            VALUES (%s, %s)
        """, (mozni_odgovor, id_vprasanja))
        self.conn.commit()

    def dodaj_odgovor(self, id_moznega_odgovora: int, username: str):
        '''
        Zapiše kaj je odgovoril user
        '''
        self.cur.execute("""
            INSERT INTO Odgovor (id_moznega_odgovora, username)
            VALUES (%s, %s)
        """, (id_moznega_odgovora, username))
        self.conn.commit()

    def spremeni_odgovor(self, id: int, nov_id_moznega_odgovora: int):
        '''
        Spremeni id_moznega_odgovora za podan ID (usernama ne spreminjamo)
        torej zamenjamo le odgovor nekega fiksnega uporabnika
        '''
        self.cur.execute("""
            UPDATE Odgovor
            SET id_moznega_odgovora = %s
            WHERE id = %s
        """, (nov_id_moznega_odgovora, id))
        self.conn.commit()        

    def dobi_odgovor(self, id: int) -> Odgovor:
        '''
        Vrne vse kar pripada točno določenemu odgovoru
        '''
        self.cur.execute("""
            SELECT id, id_moznega_odgovora, username
            FROM Odgovor
            WHERE id = %s
        """, (id,))
        
        odgovor = self.cur.fetchone()
        return Odgovor.from_dict(odgovor)

    def dobi_odgovore_osebe(self, username: str) -> List[Odgovor]:
        '''
        Za določeno osebo vrne seznam vseh odgovorov
        '''
        self.cur.execute("""
            SELECT id, id_moznega_odgovora, username
            FROM Odgovor
            WHERE username = %s
        """, (username,))
        
        odgovori = self.cur.fetchall()
        return [Odgovor.from_dict(odgovor) for odgovor in odgovori]

    def dobi_odgovorDTO(self, id: int) -> OdgovorDTO:
        '''
        Vrne besedilo vprašanja in odgovora glede na Id odgovora
        '''
        self.cur.execute("""
            SELECT v.vprasanje, mo.mozni_odgovor
            FROM Odgovor o
            JOIN Mozni_odgovor mo ON o.id_moznega_odgovora = mo.id
            JOIN Vprasanje v ON mo.id_vprasanja = v.id
            WHERE o.id = %s
        """, (id,))
        
        rezultat = self.cur.fetchone()
        return OdgovorDTO(vprasanje=rezultat['vprasanje'], odgovor=rezultat['mozni_odgovor'])

    def dobi_odgovore_osebeDTO(self, username: str) -> List[OdgovorDTO]:
        '''
        Za določeno osebo vrne seznam vseh odgovorov v obliki objektov OdgovorDTO
        '''
        self.cur.execute("""
            SELECT v.vprasanje, mo.mozni_odgovor
            FROM Odgovor o
            JOIN Mozni_odgovor mo ON o.id_moznega_odgovora = mo.id
            JOIN Vprasanje v ON mo.id_vprasanja = v.id
            WHERE o.username = %s
        """, (username,))
        
        rezultati = self.cur.fetchall()
        return [OdgovorDTO(vprasanje=rezultat['vprasanje'], odgovor=rezultat['mozni_odgovor']) for rezultat in rezultati]


#Metode, ki se nanašajo na pridobivanje odgovorov.
#teh mislm da po novem ne bova uporabiljala, ker bova uporabila te z DTO-ji
    def dobi_odgovore_ids_za_osebo(self, username: str) -> List[int]:
        '''
        Za določeno osebo vrne seznam idjev odgovorov na katere je oseba odgovorila
        '''
        self.cur.execute("""
            SELECT id_moznega_odgovora
            FROM Odgovor
            WHERE username = %s
            ORDER BY id
        """, (username,))
        
        results = self.cur.fetchall()
        answer_ids = [row["id_moznega_odgovora"] for row in results]
        return answer_ids
    
    def dobi_odgovore_texts_za_osebo(self, username: str) -> List[str]:
        '''
        Za določeno osebo vrne seznam besedil odgovorov na katere je oseba odgovorila.
        '''
        self.cur.execute("""
            SELECT mo.mozni_odgovor
            FROM Odgovor o
            JOIN Mozni_odgovor mo ON o.id_moznega_odgovora = mo.id
            WHERE o.username = %s
            ORDER BY o.id
        """, (username,))
        
        results = self.cur.fetchall()
        answer_texts = [row['mozni_odgovor'] for row in results]
        return answer_texts


#Metode, ki se nanašajo na emotione 

    def spremeni_emotion(self, username1: str, username2: str, vrednost: str):
        '''
        Spremeni ali doda vrednost za podan par v tabeli Emotion.
        Vrednost je lahko 'like', 'dislike' ali 'block'.
        '''
        if vrednost not in ['like', 'dislike', 'block']:
            raise ValueError("Vrednost mora biti 'like', 'dislike' ali 'block'")

        self.cur.execute("""
            SELECT 1 FROM Emotion WHERE username1 = %s AND username2 = %s
        """, (username1, username2))
        
        if self.cur.fetchone():
            # Če vrstica obstaja, posodobimo vrednost
            self.cur.execute("""
                UPDATE Emotion 
                SET vrednost = %s 
                WHERE username1 = %s AND username2 = %s
            """, (vrednost, username1, username2))
        else:
            # Če vrstica ne obstaja, dodamo novo vrstico
            self.cur.execute("""
                INSERT INTO Emotion (username1, username2, vrednost)
                VALUES (%s, %s, %s)
            """, (username1, username2, vrednost))
        
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

#potrebno bi bilo dodati še metode za spreminjanje.. nevem točno kje bi se tega lotil
from Data.repository import Repo
from Data.models import *
from typing import List


# V tej datoteki bomo definirali razred za obdelavo in delo z osebami in njihovimi matchi


class OsebaService:
    def __init__(self) -> None:
        # Potrebovali bomo instanco repozitorija. Po drugi strani bi tako instanco 
        # lahko dobili tudi kot input v konstrukturju.
        self.repo = Repo()
    
    def dobi_osebo(self, username: str) -> Oseba:
        '''
        Prikaži sebi svoje podatke
        '''
        return self.repo.dobi_osebo_fullDTO(username)    

#--------------------------------------
#metode za emotions
    def dobi_like_osebe(self, username) -> List[OsebaDTO]:
        '''
        Prikaz na like meniju
        '''
        return self.repo.dobi_like_osebeDTO(username)

    def dobi_dislike_osebe(self, username) -> List[OsebaDTO]:
        '''
        Prikaz na dislike meniju
        '''
        return self.repo.dobi_dislike_osebeDTO(username)
    
    def dobi_brezstika_osebe(self, username) -> List[OsebaDTO]:
        '''
        Prikaz osnovnem home meniju
        '''
        return self.repo.dobi_brezstika_osebeDTO(username)
        
    def dobi_matche_osebe(self, username) -> List[OsebafullDTO]:
        '''
        Prikaz na meniju kjer so tvoji matchi
        '''
        return self.repo.dobi_matche_osebefullDTO(username)        

    def spremeni_emotion(self, username1: str, username2: str, vrednost: str) -> None:
        '''
        Spremeni ali doda emotion med dvema osebama
        '''
        oseba1 = self.repo.dobi_osebo(username1)
        oseba2 = self.repo.dobi_osebo(username2)
        self.repo.spremeni_emotion(oseba1, oseba2, vrednost)


#--------------------------------------
#metode za dodajanje oseb, uporabnikov, posodobitev
    def dodaj_osebo(self, username: str, ime: str, priimek: str, kontakt_ig: str) -> None:
        '''
        Doda osebo
        '''
        oseba = Oseba(username=username, ime=ime, priimek=priimek, kontakt_ig=kontakt_ig)
        self.repo.dodaj_osebo(oseba)

    def dodaj_uporabnika(self, username: str, role: str, password_hash: str, last_login: str) -> None:
        '''
        Doda uporabnika
        '''
        uporabnik = Uporabnik(username=username, role=role, password_hash=password_hash, last_login=last_login)
        self.repo.dodaj_uporabnika(uporabnik)

    def posodobi_ime_priimek(self, username: str, ime: str, priimek: str) -> None:
        '''
        Spremeni ime/priimek uporabnika
        '''
        self.repo.posodobi_ime_priimek(username, ime, priimek)


#--------------------------------------
#metode za delo z vprašanji in odgovori
    def dobi_vsa_vprasanja_in_mozne_odgovore(self) -> List[Vprasanje]:
        '''
        prikazovanje adminu katera vprašanja obstajajo
        '''
        vprasanja = self.repo.dobi_vprasanja()
        for vprasanje in vprasanja:
            mozni_odgovori = self.repo.dobi_mozne_odgovore(vprasanje.id)
            vprasanje.mozni_odgovori = mozni_odgovori
        return vprasanja

    def dodaj_mozni_odgovor(self, mozni_odgovor: str, id_vprasanja: int) -> None:
        '''
        Doda možni odgovor
        '''
        mozni_odgovor_objekt = Mozni_odgovor(mozni_odgovor=mozni_odgovor, id_vprasanja=id_vprasanja)
        self.repo.dodaj_mozni_odgovor(mozni_odgovor_objekt)

    def dodaj_odgovor_uporabnika(self, username: str, id_moznega_odgovora: int) -> None:
        '''
        Doda odgovor na vprašanje za določenega uporabnika
        '''
        odgovor = Odgovor(id_moznega_odgovora=id_moznega_odgovora, username=username)
        self.repo.dodaj_odgovor(odgovor)

    def izbrisi_odgovore_uporabnika(self, username: str) -> None:
        '''
        Izbriše vse odgovore za podanega uporabnika
        '''
        self.repo.izbrisi_odgovore_osebe(username)

    def dobi_vsa_vprasanja(self) -> List[Vprasanje]:
        '''
        Vrne vsa vprašanja kot seznam objektov Vprasanje
        '''
        return self.repo.dobi_vprasanja()

    def dodaj_vprasanje(self, vprasanje_text: str) -> None:
        '''
        Dodaj novo vprašanje
        '''
        vprasanje = Vprasanje(vprasanje=vprasanje_text)
        self.repo.dodaj_vprasanje(vprasanje)

    def izbrisi_vprasanje_in_odgovore(self, vprasanje_id: int) -> None:
        '''
        Izbriše vprašanja in odgovore
        '''
        self.repo.izbrisi_odgovore_za_vprasanje(vprasanje_id)
        self.repo.izbrisi_mozne_odgovore(vprasanje_id)
        self.repo.izbrisi_vprasanje(vprasanje_id)
from Data.repository import Repo
from Data.Models import *
from typing import List


# V tej datoteki bomo definirali razred za obdelavo in delo z osebami in njihovimi matchi

class OsebaService:
    def __init__(self) -> None:
        # Potrebovali bomo instanco repozitorija. Po drugi strani bi tako instanco 
        # lahko dobili tudi kot input v konstrukturju.
        self.repo = Repo()
    
    #metode za dobit pravilne sezname osebe glede na username uporabnika
    def dobi_like_osebe(self, username) -> List[OsebaDTO]:
        return self.repo.dobi_like_osebeDTO(username)

    def dobi_dilike_osebe(self, username) -> List[OsebaDTO]:
        return self.repo.dobi_dislike_osebeDTO(username)
    
    def dobi_brezstika_osebe(self, username) -> List[OsebaDTO]:
        return self.repo.dobi_brezstika_osebeDTO(username)

    def dobi_matche_osebe(self, username) -> List[OsebafullDTO]:
        return self.repo.dobi_matche_osebefullDTO(username)        

    #metoda za spreminjanje Emotiona (mogoče bo kj druzga za input treba npr. OsebaDTO)
    #alpa celo dve različni da dobiš iz osebafullDto posebej za matchane
    def spremeni_emotion(self, o1 : Oseba, o2 : Oseba, vrednost : str) -> None:
        self.repo.spremeni_emotion(o1.username, o2.username, vrednost)


    # to bo delal ko MJ commita Data
    # def dobi_osebo(self, emso) -> Oseba:
    #     return self.repo.dobi_osebo()

   
    

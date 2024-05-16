from Data.repository import Repo
from Data.Models import *
from typing import List


# V tej datoteki bomo definirali razred za obdelavo in delo s transakcijami

class MatchService:
    def __init__(self) -> None:
        # Potrebovali bomo instanco repozitorija. Po drugi strani bi tako instanco 
        # lahko dobili tudi kot input v konstrukturju.
        self.repo = Repo()



    def dobi_osebe(self) -> List[Oseba]:
        return self.repo.dobi_osebe()
    
    #ta funkcija bo spremenila emotion
    # def spremeni_emotion(self, o: Oseba, v : str) -> None:
    #     self.repo

    # def spremeni_podatke_o_osebi(self) -> None:
    #     oseba = 
        

    # def spremeni_emotion(self, e : str) -> None:
        


    
    # def dobi_dogovore_dto(self) -> List[OdgovorDTO]:
    #     return self.repo.dobi_transakcije_dto()
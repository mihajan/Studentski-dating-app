from Data.repository import Repo
from Data.Models import *
from typing import List


# V tej datoteki bomo definirali razred za obdelavo in delo s transakcijami

class OsebaService:
    def __init__(self) -> None:
        # Potrebovali bomo instanco repozitorija. Po drugi strani bi tako instanco 
        # lahko dobili tudi kot input v konstrukturju.
        self.repo = Repo()
    
    # to bo delal ko MJ commita Data
    # def dobi_osebo(self, emso) -> Oseba:
    #     return self.repo.dobi_osebo()

    #def dobi_emotion(self, 
    

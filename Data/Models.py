from dataclasses import dataclass, field
#from dataclasses_json import dataclass_json

# V tej datoteki definiramo vse podatkovne modele, ki jih bomo uporabljali v aplikaciji

#@dataclass_json
@dataclass
class Uporabnik:
    id: int = field(default=0)
    ime: str = field(default="")
    uporabnisko_ime: str = field(default="")
    geslo: str = field(default="")
    starost: int = field(default=0)
    fakulteta: str = field(default="")


#@dataclass_json
@dataclass
class Emotion:
    id_uporabnika1: int = field(default=0)
    id_uporabnika2: int = field(default=0)
    vrednost: str = field(default="") #vrednosti bodo lahko like/dislike/block


#@dataclass_json
@dataclass
class Vprasanje:
    id: int = field(default=0)
    vprasanje: str = field(default="")


#@dataclass_json
@dataclass
class Mozni_odgovor:
    id: int = field(default=0)
    mozni_odgovor: str = field(default="")
    id_vprasanja: int = field(default=0)


#@dataclass_json
@dataclass
class Odgovor:
    id: int = field(default=0)
    id_moznega_odgovora: int = field(default=0)
    id_uporabnika: int = field(default=0)

#@dataclass_json
@dataclass
class OdgovorDTO:
    id: int = field(default=0)
    id_moznega_odgovora: int = field(default=0)
    id_uporabnika: int = field(default=0)
    odgovor: str = field(default="")
    vprasanje: str = field(default="")
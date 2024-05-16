from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from datetime import date

# V tej datoteki definiramo vse podatkovne modele, ki jih bomo uporabljali v aplikaciji

@dataclass_json
@dataclass
class Oseba:
    emso: str = field(default="")    
    ime: str = field(default="")
    priimek: str = field(default="")
    kontakt_ig: str = field(default="")



@dataclass_json
@dataclass
class Emotion:
    emso_oseba1: int = field(default="")
    emso_oseba2: int = field(default="")
    vrednost: str = field(default="") #vrednosti bodo lahko like/dislike/block


@dataclass_json
@dataclass
class Vprasanje:
    id: int = field(default=0)
    vprasanje: str = field(default="")


@dataclass_json
@dataclass
class Mozni_odgovor:
    id: int = field(default=0)
    mozni_odgovor: str = field(default="")
    id_vprasanja: int = field(default=0)


@dataclass_json
@dataclass
class Odgovor:
    id: int = field(default=0)
    id_moznega_odgovora: int = field(default=0)
    emso: int = field(default="")

@dataclass_json
@dataclass
class OdgovorDTO:
    id: int = field(default=0)
    id_moznega_odgovora: int = field(default=0)
    emso: int = field(default="")
    odgovor: str = field(default="") #dodatno celo besedilo odgovora
    vprasanje: str = field(default="") #dodatno celo besedilo vprašanja

@dataclass_json
@dataclass
class Uporabnik:
    username: str = field(default="")
    role: str = field(default="")
    password_hash: str = field(default="")
    last_login: str = field(default="")

@dataclass
class UporabnikDto:
    username: str = field(default="")
    role: str = field(default="")
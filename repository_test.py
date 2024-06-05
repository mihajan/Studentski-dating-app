from Data.repository import Repo
from Data.models import *


repo = Repo()

# Dobimo vse osebe

#to nekak dela

# Jih izpišemo
#for o in osebe:
#    print(o)


#######################
#testiranje chat predstavitev rezultatov
username = '0909000500044'  
#answers = repo.dobi_odgovore_za_osebo(username)

#matchi = repo.matchi_osebe(username)

#print("Matchi:", matchi)

#matchi2 = repo.matchi_osebe('1111111111111')
#print("Matchi:", matchi2)

username1 = '1111111111111'  # Zamenjajte z dejanskim usernamem
username2 = '2222222222222'  # Zamenjajte z dejanskim usernamem

# Dodaj ali posodobi 'like'
#repo.spremeni_emotion(username1, username2, 'like')
#repo.spremeni_emotion(username, username2, 'like')
#repo.spremeni_emotion(username2, username1, 'dislike')
#repo.spremeni_emotion(username2, username, 'like')
# Dodaj ali posodobi 'dislike'
#repo.spremeni_emotion(username1, username2, 'dislike')

# Dodaj ali posodobi 'block'
#repo.spremeni_emotion(username1, username2, 'block')


#vsi_odgovori = repo.odgovori_text_vsi()
#for v in vsi_odgovori:
#    print(v)
#print(repo.oseba_matchi(username))
#print(repo.oseba_dislike(username2))

#repo.dodaj_vprasanje(Vprasanje(vprasanje="A to dela?"))
#dela
id_odgovora = 3  # Zamenjajte z dejanskim ID-jem odgovora


#odgovor_dto = repo.dobi_odgovorDTO(id_odgovora)

#print(f"Vprašanje: {odgovor_dto.vprasanje}, Odgovor: {odgovor_dto.odgovor}")

#odgovori_dto = repo.dobi_odgovore_osebeDTO(username)

#for v in odgovori_dto:
    #print(f"Vprašanje: {odgovor_dto.vprasanje}, Odgovor: {odgovor_dto.odgovor}")
    #print(v)

#osebe_dto = repo.dobi_matche_osebefullDTO(username2)
#for oseba_dto in osebe_dto:
#    print(oseba_dto)
    
oseba1 = Oseba(
    username="user1",
    ime="Janez",
    priimek="Novak",
    kontakt_ig="janez.n"
)

oseba2 = Oseba(
    username="user2",
    ime="Maja",
    priimek="Kovač",
    kontakt_ig="maja.k"
)
#repo.spremeni_emotion(oseba1, oseba2, "like")  
#repo.spremeni_emotion(oseba2, oseba1, "like") 

odg = Odgovor(
    id=253,
    id_moznega_odgovora = 20,
    username='hruska'
)

#repo.spremeni_odgovor(odg, 19)

#a= repo.dobi_brezstika_osebeDTO('mihc')
#for os in a:
#    print(os.ime)

b= repo.dobi_like_osebeDTO('hruska')
print(b)
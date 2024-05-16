from repository import Repo
from Models import *


repo = Repo()

# Dobimo vse osebe

osebe = repo.dobi_osebe()
#to nekak dela

# Jih izpišemo
#for o in osebe:
#    print(o)


#######################
#testiranje chat predstavitev rezultatov
repo = Repo()
emso = '0909000500044'  # Replace with the actual emso you want to query
#answers = repo.dobi_odgovore_za_osebo(emso)

#for answer in answers:
#    print(f"Question: {answer['question']}, Answer: {answer['answer']}")

oseba = repo.dobi_osebo(emso)
print(f"Ime: {oseba.ime}, Priimek: {oseba.priimek}, Kontakt IG: {oseba.kontakt_ig}")

#test seznama
answer_ids = repo.dobi_odgovore_ids_za_osebo(emso)

print("Answer IDs:", answer_ids)
answer_texts = repo.dobi_odgovore_texts_za_osebo(emso)

print("Odogovri za", emso, "so:", answer_texts)

#dodajanje emotionov
#repo.dodaj_emotion_like(emso, "2222222222222")
#repo.dodaj_emotion_dislike(emso, "2222222222222")
#repo.dodaj_emotion_block(emso, "2222222222222")
# repo.dodaj_emotion_like(emso, "1111111111111")
# repo.dodaj_emotion_like("1111111111111", emso)
# repo.dodaj_emotion_like(emso, "3333333333333")
# repo.dodaj_emotion_like(emso, "8888888888888")
# repo.dodaj_emotion_like(emso, "1111111111110")
# repo.dodaj_emotion_like("3333333333333",emso)
# repo.dodaj_emotion_like("8888888888888",emso)
# repo.dodaj_emotion_like("1111111111110",emso)




#matchi = repo.matchi_osebe(emso)

#print("Matchi:", matchi)

#matchi2 = repo.matchi_osebe('1111111111111')
#print("Matchi:", matchi2)

emso_oseba1 = '1111111111111'  # Zamenjajte z dejanskim emsom
emso_oseba2 = '2222222222222'  # Zamenjajte z dejanskim emsom

# Dodaj ali posodobi 'like'
#repo.spremeni_emotion(emso_oseba1, emso_oseba2, 'like')

# Dodaj ali posodobi 'dislike'
repo.spremeni_emotion(emso_oseba1, emso_oseba2, 'dislike')

# Dodaj ali posodobi 'block'
#repo.spremeni_emotion(emso_oseba1, emso_oseba2, 'block')

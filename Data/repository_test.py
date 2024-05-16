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
emso = '1111111111111'  # Replace with the actual emso you want to query
answers = repo.dobi_odgovore_za_osebo(emso)

#for answer in answers:
#    print(f"Question: {answer['question']}, Answer: {answer['answer']}")

#test seznama
answer_ids = repo.dobi_odgovore_ids_za_osebo(emso)

print("Answer IDs:", answer_ids)
answer_texts = repo.dobi_odgovore_texts_za_osebo(emso)

print("Odogovri za", emso, "so:", answer_texts)

#dodajanje emotionov
repo.dodaj_emotion_like(emso, "2222222222222")
#repo.dodaj_emotion_dislike(emso, "2222222222222")
#repo.dodaj_emotion_block(emso, "2222222222222")
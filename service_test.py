from Services.oseba_service import OsebaService
from Services.auth_service import AuthService
from Data.models import *

service = OsebaService()
auth = AuthService()

# Preizkus pridobivanja osebe
#oseba = service.dobi_osebo('user1')
#print(oseba)

#service.dodaj_osebo("hruska", "Luka", "houska", "debela_hruska")
#service.dodaj_osebo('mihc','Miha', 'Jan', 'mj9')


#service.spremeni_emotion('hruska', 'user1', 'like')

#matchi = service.dobi_like_osebe('user1')
#for m in matchi:
#    print(m)

#service.dodaj_odgovor_uporabnika("hruska", 1)
#service.dodaj_odgovor_uporabnika("hruska", 9)

#auth.prijavi_uporabnika('mihc', 'mihc')

test = service.dobi_brezstika_osebe('mihc')
#for a in test:
#    print(a)
print(test)
service.spremeni_emotion('test1', 'mihc', 'like')
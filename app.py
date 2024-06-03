from functools import wraps
from Presentation.bottleext import route, get, post, run, request, template, redirect, static_file, url, response
from Services.oseba_service import OsebaService
from Services.auth_service import AuthService
import os

# Ustvarimo instance servisov, ki jih potrebujemo.
service = OsebaService()
auth = AuthService()

# privzete nastavitve
SERVER_PORT = os.environ.get('BOTTLE_PORT', 8080)
RELOADER = os.environ.get('BOTTLE_RELOADER', True)

def cookie_required(f):
    """
    Dekorator, ki zahteva veljaven piškotek. Če piškotka ni, uporabnika preusmeri na stran za prijavo.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        cookie = request.get_cookie("uporabnik")
        if cookie:
            return f(*args, **kwargs)
        return template("prijava2.html", uporabnik=None, rola=None, napaka="Potrebna je prijava!")
    return decorated

#tole vsaj zaenkrat še ne naredi nič
# Določimo statične datoteke
@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='Presentation/static')

def cookie_required(f):
    """
    Dekorator, ki zahteva veljaven piškotek. Če piškotka ni, uporabnika preusmeri na stran za prijavo.
    """
    def decorated(*args, **kwargs):
        cookie = request.get_cookie("uporabnik")
        if cookie:
            return f(*args, **kwargs)
        return template("prijava2.html", uporabnik=None, rola=None, napaka="Potrebna je prijava!")
    return decorated

@get('/')
@cookie_required
def index():
    username = request.get_cookie("uporabnik")
    osebe_dto = service.dobi_brezstika_osebe(username)
    return template('domaca_stran.html', osebe=osebe_dto, username=username)

@post('/prijava')
def prijava():
    """
    Prijavi uporabnika v aplikacijo. Če je prijava uspešna, ustvari piškotke o uporabniku in njegovi roli.
    Drugače sporoči, da je prijava neuspešna.
    """
    username = request.forms.get('username')
    password = request.forms.get('password')

    if not auth.obstaja_uporabnik(username):
        return template("prijava2.html", napaka="Uporabnik s tem imenom ne obstaja")

    prijava = auth.prijavi_uporabnika(username, password)
    if prijava:
        response.set_cookie("uporabnik", username)
        response.set_cookie("rola", prijava.role)
        #neka drugam te bo mogl redirectat
        redirect(url('/'))
        
    else:
        return template("prijava2.html", uporabnik=None, rola=None, napaka="Neuspešna prijava. Napačno geslo ali uporabniško ime.")

@get('/odjava')
def odjava():
    """
    Odjavi uporabnika iz aplikacije. Pobriše piškotke o uporabniku in njegovi roli.
    """
    response.delete_cookie("uporabnik")
    response.delete_cookie("rola")
    return template('prijava2.html', uporabnik=None, rola=None, napaka=None)

@get('/register')
def register_form():
    return template('registracija2.html')

@post('/register')
def register():
    username = request.forms.get('username')
    ime = request.forms.get('ime')
    priimek = request.forms.get('priimek')
    geslo = request.forms.get('geslo')
    kontakt_ig = request.forms.get('kontakt_ig')
    role = request.forms.get('role')
    
    if auth.obstaja_uporabnik(username):
        return template('registracija2.html', napaka="Uporabnik s tem imenom že obstaja.")
    
    service.dodaj_osebo(username, ime, priimek, kontakt_ig)
    auth.dodaj_uporabnika(username, role, geslo)
    redirect('/questions')


@get('/questions')
@cookie_required
def questions_get():
    vprasanja = service.dobi_vsa_vprasanja_in_mozne_odgovore()
    return template('vprasanja2.html', vprasanja=vprasanja)

@post('/questions')
@cookie_required
def questions_post():
    username = request.get_cookie("uporabnik")
    vprasanja = service.dobi_vsa_vprasanja_in_mozne_odgovore()
    for vprasanje in vprasanja:
        odgovor = request.forms.get(f'vprasanje_{vprasanje.id}')
        if odgovor:
            service.dodaj_odgovor_uporabnika(username, int(odgovor))
    
    redirect(url('/'))


#prikaz templatov za matche, like in dislike
@get('/matchi')
@cookie_required
def matchi():
    username = request.get_cookie("uporabnik")
    matchi = service.dobi_matche_osebe(username)
    return template('matchi.html', osebe=matchi)

@get('/likes')
@cookie_required
def likes():
    username = request.get_cookie("uporabnik")
    osebe_dto = service.dobi_like_osebe(username)
    return template('likes.html', osebe=osebe_dto)

@get('/dislikes')
@cookie_required
def dislikes():
    username = request.get_cookie("uporabnik")
    osebe_dto = service.dobi_dislike_osebe(username)
    #lahko kr isti html vrnemo k isto zgleda
    return template('dislikes.html', osebe=osebe_dto)


#dodajanje funkcionalnosti gumbom za like in dislike
@post('/like')
@cookie_required
def like():
    username1 = request.get_cookie("uporabnik")
    username2 = request.forms.get('username2')
    service.spremeni_emotion(username1, username2, 'like')
    redirect(url('/'))

@post('/dislike')
@cookie_required
def dislike():
    username1 = request.get_cookie("uporabnik")
    username2 = request.forms.get('username2')
    service.spremeni_emotion(username1, username2, 'dislike')
    redirect(url('/'))

#prikaz samega sebi
@get('/jaz')
@cookie_required
def jaz():
    """
    Stran za prikaz osebnih podatkov uporabnika.
    """
    username = request.get_cookie("uporabnik")
    oseba = service.dobi_osebo(username)
    return template('jaz.html', oseba=oseba)

#spreminjanje odgovorov
@post('/izbrisi_odgovore')
@cookie_required
def izbrisi_odgovore():
    """
    Izbriše vse odgovore uporabnika in preusmeri na stran z vprašanji.
    """
    username = request.get_cookie("uporabnik")
    service.izbrisi_odgovore_uporabnika(username)
    redirect(url('/questions'))

#auth.dodaj_uporabnika('mihc', 'admin', 'mihc')
#auth.dodaj_uporabnika('user1', 'admin', 'user1')

if __name__ == '__main__':
    run(host="localhost", port=SERVER_PORT, reloader=True)

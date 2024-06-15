from functools import wraps
from Presentation.bottleext import *
from Services.oseba_service import OsebaService
from Services.auth_service import AuthService
import os
#import socket

# Ustvarimo instance servisov, ki jih potrebujemo.
service = OsebaService()
auth = AuthService()

# privzete nastavitve
SERVER_PORT = int(os.environ.get('BOTTLE_PORT', 8080))
RELOADER = os.environ.get('BOTTLE_RELOADER', True)
#HOST = os.environ.get('BOTTLE_HOST', 'localhost')

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

# Določimo statične datoteke
@route('/static/<filename:path>', name='static')
def static(filename):
    return static_file(filename, root='Presentation/static')

@get('/', name='index')
@cookie_required
def index():
    username = request.get_cookie("uporabnik")
    role = request.get_cookie("rola")

    if role == 'admin':
        redirect(url('urejanje'))
    else:
        filter_text = request.query.filter_text or ''
        osebe_dto = service.dobi_brezstika_osebe(username)
        oseba = service.dobi_osebo(username)
        return template('domaca_stran.html', oseba=oseba, osebe=osebe_dto, filter_text=filter_text)

@post('/prijava', name='prijava')
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
        
        if prijava.role == 'admin':
            redirect(url('urejanje'))
        else:
            redirect(url('index'))
        
    else:
        return template("prijava2.html", uporabnik=None, rola=None, napaka="Neuspešna prijava. Napačno geslo ali uporabniško ime.")

@get('/odjava', name='odjava')
def odjava():
    """
    Odjavi uporabnika iz aplikacije. Pobriše piškotke o uporabniku in njegovi roli.
    """
    response.delete_cookie("uporabnik")
    response.delete_cookie("rola")
    return template('prijava2.html', uporabnik=None, rola=None, napaka=None)

@get('/register', name='register')
def register():
    return template('registracija.html', napaka = None)

@post('/register', name='register_post')
def register_post():
    username = request.forms.get('username').encode('iso-8859-1').decode('utf-8')
    ime = request.forms.get('ime').encode('iso-8859-1').decode('utf-8')
    priimek = request.forms.get('priimek').encode('iso-8859-1').decode('utf-8')
    geslo = request.forms.get('geslo').encode('iso-8859-1').decode('utf-8')
    kontakt_ig = request.forms.get('kontakt_ig').encode('iso-8859-1').decode('utf-8')
    role = 'user'

    oseba = service.dobi_osebo(username)

    if oseba is not None:
        return template('registracija.html', napaka = "Uporabniško ime je že zasedeno.")
    else:
        service.dodaj_osebo(username, ime, priimek, kontakt_ig)
        auth.dodaj_uporabnika(username, role, geslo)
        response.set_cookie("uporabnik", username)
        redirect(url('questions_get'))

@get('/izbira_role', name='izbira_role')
def izbira_role():
    return template('izbira_role.html')

@post('/izbira_role', name='izbira_role_post')
def izbira_role_post():
    role = request.forms.get('role')
    if role == 'admin':
        redirect(url('admin_auth'))
    elif role == 'user':
        redirect(url('register'))

@get('/admin_auth', name='admin_auth')
def admin_auth():
    return template('admin_aktivacija.html', napaka = None)

@post('/admin_auth', name='admin_auth_post')
def admin_auth_post():
    auth_code = request.forms.get('aktivacija')
    if auth_code == '123':  # zamenjajte z dejansko avtorizacijsko kodo
        redirect(url('admin_register'))
    else:
        return template('admin_aktivacija.html', napaka = "Napačna avtorizacijska koda.")

@get('/admin_register', name='admin_register')
def admin_register():
    return template('admin_register.html', napaka = None)

@post('/admin_register', name='admin_register_post')
def admin_register_post():
    username = request.forms.get('username').encode('iso-8859-1').decode('utf-8')
    geslo = request.forms.get('geslo').encode('iso-8859-1').decode('utf-8')
    role = 'admin'
    
    oseba = service.dobi_osebo(username)

    if oseba is not None:
        return template('admin_register.html', napaka = "Uporabniško ime je že zasedeno.")
    else:
        service.dodaj_osebo(username, 'ime', 'priimek', 'kontakt_ig')
        auth.dodaj_uporabnika(username, role, geslo)
        response.set_cookie("uporabnik", username)
        redirect(url('urejanje'))

@get('/urejanje', name='urejanje')
@cookie_required
def urejanje():
    username = request.get_cookie("uporabnik")
    user = auth.dobi_uporabnika(username)
    
    if user.role != 'admin':
        redirect(url('index'))
    
    vprasanja = service.dobi_vsa_vprasanja()
    vprasanja_mozni_odgovori = service.dobi_vsa_vprasanja_in_mozne_odgovore()
    return template('urejanje2.html', vprasanja=vprasanja, vprasanja_mozni_odgovori=vprasanja_mozni_odgovori)

@post('/dodaj_vprasanje', name='dodaj_vprasanje')
@cookie_required
def dodaj_vprasanje():
    vprasanje_text = request.forms.get('vprasanje').encode('iso-8859-1').decode('utf-8')
    service.dodaj_vprasanje(vprasanje_text)
    redirect(url('urejanje'))

@post('/dodaj_mozni_odgovor', name='dodaj_mozni_odgovor')
@cookie_required
def dodaj_mozni_odgovor():
    vprasanje_id = request.forms.get('vprasanje_id')
    mozni_odgovor = request.forms.get('mozni_odgovor').encode('iso-8859-1').decode('utf-8')
    service.dodaj_mozni_odgovor(mozni_odgovor, int(vprasanje_id))
    redirect(url('urejanje'))

@post('/izbrisi_vprasanje', name='izbrisi_vprasanje')
@cookie_required
def izbrisi_vprasanje():
    vprasanje_id = request.forms.get('vprasanje_id')
    service.izbrisi_vprasanje(int(vprasanje_id))
    redirect(url('urejanje'))

@get('/questions', name='questions_get')
@cookie_required
def questions_get():
    vprasanja = service.dobi_vsa_vprasanja_in_mozne_odgovore()
    return template('vprasanja.html', vprasanja=vprasanja)

@post('/questions', name='questions_post')
@cookie_required
def questions_post():
    username = request.get_cookie("uporabnik")
    vprasanja = service.dobi_vsa_vprasanja_in_mozne_odgovore()
    for vprasanje in vprasanja:
        odgovor = request.forms.get(f'vprasanje_{vprasanje.id}')
        if odgovor:
            service.dodaj_odgovor_uporabnika(username, int(odgovor))
    
    redirect(url('index'))

@get('/matchi', name='matchi')
@cookie_required
def matchi():
    username = request.get_cookie("uporabnik")
    filter_text = request.query.filter_text or ''
    osebe_dto = service.dobi_matche_osebe(username)
    return template('matchi.html', osebe=osebe_dto, filter_text=filter_text)

@get('/likes', name='likes_get')
@cookie_required
def likes_get():
    username = request.get_cookie("uporabnik")
    filter_text = request.query.filter_text or ''
    osebe_dto = service.dobi_like_osebe(username)
    return template('likes.html', osebe=osebe_dto, filter_text=filter_text)

@get('/dislikes', name='dislikes_get')
@cookie_required
def dislikes_get():
    username = request.get_cookie("uporabnik")
    filter_text = request.query.filter_text or ''
    osebe_dto = service.dobi_dislike_osebe(username)
    return template('dislikes.html', osebe=osebe_dto, filter_text=filter_text)

@post('/likes', name='likes_post')
@cookie_required
def likes_post():
    username1 = request.get_cookie("uporabnik")
    username2 = request.forms.get('username2')
    service.spremeni_emotion(username1, username2, 'like')
    redirect(url('index'))

@post('/dislikes', name='dislike_post')
@cookie_required
def dislike_post():
    username1 = request.get_cookie("uporabnik")
    username2 = request.forms.get('username2')
    service.spremeni_emotion(username1, username2, 'dislike')
    redirect(url('index'))

@get('/jaz', name='jaz_get')
@cookie_required
def jaz_get():
    """
    Stran za prikaz osebnih podatkov uporabnika.
    """
    username = request.get_cookie("uporabnik")
    oseba = service.dobi_osebo(username)
    return template('jaz.html', oseba=oseba)

@post('/jaz', name='jaz_post')
@cookie_required
def jaz_post():
    """
    Endpoint za posodobitev osebnih podatkov uporabnika.
    """
    username = request.get_cookie("uporabnik")
    ime = request.forms.get('ime')
    priimek = request.forms.get('priimek')
    novo_geslo = request.forms.get('geslo')

    if ime and priimek:
        service.posodobi_ime_priimek(username, ime, priimek)

    if novo_geslo:
        service.posodobi_geslo(username, novo_geslo)

    redirect(url('jaz_get'))

@post('/izbrisi_odgovore', name='izbrisi_odgovore')
@cookie_required
def izbrisi_odgovore():
    """
    Izbriše vse odgovore uporabnika in preusmeri na stran z vprašanji.
    """
    username = request.get_cookie("uporabnik")
    service.izbrisi_odgovore_uporabnika(username)
    redirect(url('questions_get'))

@post('/izbrisi_vprasanje', name='izbrisi_vprasanje')
@cookie_required
def izbrisi_vprasanje():
    """
    Izbriše vprašanje in vse možne odgovore nanj.
    """
    vprasanje_id = request.forms.get('vprasanje_id')
    if vprasanje_id:
        service.izbrisi_vprasanje_in_odgovore(int(vprasanje_id))
    redirect(url('urejanje'))  

run(host="localhost", port=SERVER_PORT, reloader=RELOADER, debug=True)

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
    role = request.get_cookie("rola")

    if role == 'admin':
        redirect(url('/urejanje'))
    else:
        filter_text = request.query.filter_text or ''
        osebe_dto = service.dobi_brezstika_osebe(username)
        return template('domaca_stran.html', osebe=osebe_dto, filter_text=filter_text)


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
        
        if prijava.role == 'admin':
            redirect(url('/urejanje'))
        else:
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
def register():
    return template('registracija2.html')

@post('/register')
def register_post():
    username = request.forms.get('username')
    ime = request.forms.get('ime')
    priimek = request.forms.get('priimek')
    geslo = request.forms.get('geslo')
    kontakt_ig = request.forms.get('kontakt_ig')
    role = 'user'

    service.dodaj_osebo(username, ime, priimek, kontakt_ig)
    auth.dodaj_uporabnika(username, role, geslo)
    response.set_cookie("uporabnik", username)
    redirect('/questions')

@get('/izbira_role')
def izbira_role():
    return template('izbira_role.html')

@post('/izbira_role')
def izbira_role_post():
    role = request.forms.get('role')
    if role == 'admin':
        redirect('/admin_auth')
    elif role == 'user':
        redirect('/register')

@get('/admin_auth')
def admin_auth():
    return template('admin_aktivacija.html')

@post('/admin_auth')
def admin_auth_post():
    auth_code = request.forms.get('aktivacija')
    if auth_code == '123':  # zamenjajte z dejansko avtorizacijsko kodo
        redirect('/admin_register')
    else:
        return template('admin_aktivacija.html', napaka="Napačna avtorizacijska koda.")

@get('/admin_register')
def admin_register():
    return template('admin_register.html')

@post('/admin_register')
def admin_register_post():
    username = request.forms.get('username')
    geslo = request.forms.get('geslo')
    role = 'admin'
    service.dodaj_osebo(username, 'ime', 'priimek', 'kontakt_ig')
    auth.dodaj_uporabnika(username, role, geslo)
    response.set_cookie("uporabnik", username)
    redirect('/urejanje')

#-------------------------------------------------------------------
#dodajanje vprašanj in možnih odgovorov (za admine)
@get('/urejanje')
@cookie_required
def urejanje():
    username = request.get_cookie("uporabnik")
    user = auth.dobi_uporabnika(username)
    
    if user.role != 'admin':
        redirect(url('/'))
    
    vprasanja = service.dobi_vsa_vprasanja()
    vprasanja_mozni_odgovori = service.dobi_vsa_vprasanja_in_mozne_odgovore()
    return template('urejanje2.html', vprasanja=vprasanja, vprasanja_mozni_odgovori=vprasanja_mozni_odgovori)


@post('/dodaj_vprasanje')
@cookie_required
def dodaj_vprasanje():
    vprasanje_text = request.forms.get('vprasanje')
    service.dodaj_vprasanje(vprasanje_text)
    redirect('/urejanje')

@post('/dodaj_mozni_odgovor')
@cookie_required
def dodaj_mozni_odgovor():
    vprasanje_id = request.forms.get('vprasanje_id')
    mozni_odgovor = request.forms.get('mozni_odgovor')
    service.dodaj_mozni_odgovor(mozni_odgovor, int(vprasanje_id))
    redirect('/urejanje')

#--------------------------------------------------------------------
#stran za odgovarjanje na vprašanja
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

#------------------------------------------------------------------------------------
#prikaz templatov za matche, like in dislike
@get('/matchi')
@cookie_required
def matchi():
    username = request.get_cookie("uporabnik")
    filter_text = request.query.filter_text or ''
    osebe_dto = service.dobi_matche_osebe(username)
    return template('matchi.html', osebe=osebe_dto, filter_text=filter_text)

@get('/likes')
@cookie_required
def likes():
    username = request.get_cookie("uporabnik")
    filter_text = request.query.filter_text or ''
    osebe_dto = service.dobi_like_osebe(username)
    return template('likes.html', osebe=osebe_dto, filter_text=filter_text)

@get('/dislikes')
@cookie_required
def dislikes():
    username = request.get_cookie("uporabnik")
    filter_text = request.query.filter_text or ''
    osebe_dto = service.dobi_dislike_osebe(username)
    return template('dislikes.html', osebe=osebe_dto, filter_text=filter_text)


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


@post('/izbrisi_vprasanje')
@cookie_required
def izbrisi_vprasanje():
    """
    Izbriše vprašanje in vse možne odgovore nanj.
    """
    vprasanje_id = request.forms.get('vprasanje_id')
    if vprasanje_id:
        service.izbrisi_vprasanje_in_odgovore(int(vprasanje_id))
    redirect('/urejanje')  

#auth.dodaj_uporabnika('mihc', 'admin', 'mihc')
#auth.dodaj_uporabnika('user1', 'admin', 'user1')


run(host="localhost", port=SERVER_PORT, reloader=True)

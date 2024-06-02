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
    """
    Domača stran.
    """
    return "Hello, World!"  

@post('/prijava')
def prijava():
    """
    Prijavi uporabnika v aplikacijo. Če je prijava uspešna, ustvari piškotke o uporabniku in njegovi roli.
    Drugače sporoči, da je prijava neuspešna.
    """
    username = request.forms.get('username')
    password = request.forms.get('password')

    if not auth.obstaja_uporabnik(username):
        return template("vprasanja.html", napaka="Uporabnik s tem imenom ne obstaja")

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
    redirect('/')


#@get('/')
#def zacetek():
#    return template(
#        'zacetna_stran.html'
#        )


#auth.dodaj_uporabnika('mihc', 'admin', 'mihc')
#auth.dodaj_uporabnika('user1', 'admin', 'user1')

if __name__ == '__main__':
    run(host="localhost", port=SERVER_PORT, reloader=True)

from functools import wraps
from Presentation.bottleext import route, get, post, run, request, template, redirect, static_file, url, response

    # from Services.transakcije_service import TransakcijeService
    # from Services.auth_service import AuthService
import os

# Ustvarimo instance servisov, ki jih potrebujemo. 
# Če je število servisov veliko, potem je service bolj smiselno inicializirati v metodi in na
# začetku datoteke (saj ne rabimo vseh servisov v vseh metodah!)

    # service = TransakcijeService()
    # auth = AuthService()


# privzete nastavitve
SERVER_PORT = os.environ.get('BOTTLE_PORT', 8080)
RELOADER = os.environ.get('BOTTLE_RELOADER', True)

    # def cookie_required(f):
    #     """
    #     Dekorator, ki zahteva veljaven piškotek. Če piškotka ni, uporabnika preusmeri na stran za prijavo.
    #     """
    #     @wraps(f)
    #     def decorated( *args, **kwargs):
    #         cookie = request.get_cookie("uporabnik")
    #         if cookie:
    #             return f(*args, **kwargs)
    #         return template("prijava.html",uporabnik=None, rola=None, napaka="Potrebna je prijava!")
            
    #     return decorated

    # @get('/static/<filename:path>')
    # def static(filename):
    #     return static_file(filename, root='Presentation/static')

    # @get('/prijava')
    # def prijava_get():
    #     return template(
    #         "prijava.html"
    #     )

    # @post('/prijava')
    # def prijava_post():
    #     uporabnisko_ime = request.forms.getunicode("uporabnisko_ime")
    #     geslo = request.forms.getunicode("geslo")
    #     if uporabnisko_ime == geslo[::-1]:
    #         response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/", secret=SIFRIRNI_KLJUC)
    #         redirect("/")
    #     else:
    #         return "Napaka ob prijavi"

    # @route("/odjava/")
    # def odjava_post():
    #     response.delete_cookie("uporabnisko_ime", path="/")
    #     redirect("/")
    #
    # tole je sam prekopiran iz mojga starga projekta; vsako stvar k jo lohka spreminjaš more met posebi get in post metodo
    # @get("/spremeni-ime/<id_osebe:int>/")
    # def spremeni_ime_get(id_osebe):
    #     return template(
    #         "spremeni_ime.html", napake={}, polja={}
    #     )

    # @post("/spremeni-ime/<id_osebe:int>/")
    # def spremeni_ime(id_osebe):
    #     stanje = stanje_trenutnega_uporabnika()
    #     oseba = stanje.ljudje[id_osebe]
    #     novo_ime = request.forms.getunicode("ime")
    #     nova_oseba = Oseba(novo_ime, stroski=[])
    #     napake = stanje.preveri_osebo(nova_oseba)
    #     if napake:
    #         polja = {"ime": novo_ime}
    #         return template("dodaj_osebo.html", napake=napake, polja=polja)
    #     else:
    #         oseba.spremeni_ime(novo_ime)
    #         shrani_stanje_trenutnega_uporabnika(stanje)
    #         redirect(url_osebe(id_osebe))

@get('/')
def zacetek():
    return template(
        'zacetna_stran.html'
        )


if __name__ == '__main__':
    run(host="localhost", port=SERVER_PORT, reloader=True)

from functools import wraps
from Presentation.bottleext import route, get, post, run, request, template, redirect, static_file, url, response, template_user

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


@get('/')
def zacetek():
    return template(
        'zacetna_stran.html'
        )


run(host="localhost", port=8080, reloader=True)

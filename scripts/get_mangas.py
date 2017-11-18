import json
from classes.request import Request
from classes.manga import Manga

def get_mangas():

    try:
        req = Request("https://mcd.iosphe.re/api/v1/database/")
        obj = json.loads(req.request_page())

        for key, value in obj.items():
            manga = Manga(key, value)
            manga.check_manga()

    
    except (TypeError, ValueError, OverflowError) as err:
        print("Mangas request error: %s" % err)
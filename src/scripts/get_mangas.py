import json
from src.classes.request import Request
from src.classes.manga import Manga

def get_mangas():

    try:
        loop_index = 1
        while loop_index > 0:

            req = Request("http://unionmangas.net/mangas/a-z/%s/*" % loop_index)
            soup = req.soup()
            data = soup.findAll("div", {"class": "bloco-manga"})

            if data is not []:
                for manga_block in data:
                    manga_a_tags = manga_block.findAll("a", {"class": None, "href": True})
                    manga_url = manga_a_tags[0]['href']
                    manga = Manga(manga_url)
                    
                loop_index += 1

            else:
                loop_index = -1

    except (TypeError, ValueError, OverflowError) as err:
        print("Manga request error: %s" % err)
#bs4, urllib, html5lib, PyMySQL

# from class.request import Request
from scripts.get_mangas import get_mangas
from classes.database import Database

# req = Request("http://unionmangas.net/leitor/Berserk/112")
# print(req.soup())

if __name__ == "__main__":
    get_mangas()
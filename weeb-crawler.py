#bs4, urllib, html5lib

from lib.request import Request

req = Request("http://unionmangas.net/leitor/Berserk/112")
print(req.soup())
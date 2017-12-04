#bs4, requests, html5lib, PyMySQL, zlib

import time, datetime
from src.scripts.get_mangas import get_mangas

if __name__ == "__main__":
    string_stating = datetime.datetime.now()
    get_mangas()
    string_ending = datetime.datetime.now()
    string_diff = string_ending - string_stating

    print("Start: %s | End: %s | Elapsed: %s" % (string_stating, string_ending, string_diff))

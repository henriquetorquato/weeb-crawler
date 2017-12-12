# bs4, requests, html5lib, PyMySQL, zlib, Flask

from datetime import datetime
from flask import Flask
from multiprocessing import Process, Value
from src.classes.logging import Logging
from src.scripts.get_mangas import get_mangas
from src.classes.api import Api

if __name__ == "__main__":

    log = Logging("App")
    log.info("App started at %s" % datetime.now())

    crawler_process = Process(target=get_mangas)
    crawler_process.start()
    
    api = Api()
    api.run()

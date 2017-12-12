import logging, jinja2
from flask import Flask, render_template
from src.classes.database import Database
from src.classes.config import Config
from src.classes.logging import Logging

class Api:

    def __init__(self):

        cfg = Config()
        cfg = cfg.get("api")

        self.log = Logging("Api")
        self.debug = int(cfg["logging"])
        self.host = cfg["host"]
        self.port = cfg["port"]
        self.app = self.create_app()


    def create_app(self):

        app = Flask(__name__)
        app.debug = self.debug

        app.logger.disable = not self.debug
        log = logging.getLogger("werkzeug")
        log.disabled = not self.debug

        custom_loader = jinja2.ChoiceLoader([
            app.jinja_loader,
            jinja2.FileSystemLoader("src/views")
        ])
        app.jinja_loader = custom_loader

        app.add_url_rule("/", "index", self.index)
        return app


    def run(self):

        self.log.info("Api started in %s:%s" % (self.host, self.port))
        self.app.run(use_reloader=False,
                     host=self.host,
                     port=self.port)


    def index(self):

        database = Database()
        result = database.execute("""SELECT COUNT(official_title) AS quant 
                                  FROM weeb_crawler.manga""", [])

        with self.app.app_context():
            return render_template("index.html", var=result[0][0])

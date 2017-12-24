import logging, jinja2, json
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from src.classes.database import Database
from src.classes.config import Config
from src.classes.logging import Logging

class Api:

    def __init__(self):

        self.cfg = Config()
        cfg = self.cfg.get("api")

        self.log = Logging("Api")
        self.debug = int(cfg["logging"])
        self.host = cfg["host"]
        self.port = int(cfg["port"])
        self.app = self.create_app()
        self.add_routes()


    def create_app(self):

        app = Flask(__name__)
        app.debug = self.debug

        app.logger.disable = not self.debug
        log = logging.getLogger("werkzeug")
        log.disabled = not self.debug

        cors = CORS(app)
        app.config['CORS_HEADERS'] = 'Content-Type'

        return app


    def add_routes(self):

        @self.app.route("/getLog", methods=["GET"])
        @cross_origin()
        def get_log():
            log_name = self.log.get_log_name()
            cfg = self.cfg.get("getLog")
            return_amount = int(cfg["return_amount"])
            with open(log_name, "r") as log:
                return_data = {
                    "name": log_name,
                    "amount": return_amount,
                    "content": log.readlines()[-return_amount:]
                }
                return json.dumps(return_data)

        @self.app.route("/getStats", methods=["GET"])
        @cross_origin()
        def get_stats():
            database = Database()
            result = database.execute("""SELECT
                                        (SELECT COUNT(id) FROM manga) AS manga_amount,
                                        (SELECT COUNT(id) FROM chapter) AS chapter_amount,
                                        (SELECT COUNT(id) FROM page) AS page_amount""")
            return json.dumps(result[0])


    def run(self):

        self.log.info("Api started in %s:%s" % (self.host, self.port))
        self.app.run(use_reloader=False,
                     host=self.host,
                     port=self.port)

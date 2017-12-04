import json
from src.classes.database import Database
from src.classes.request import Request

class Covers:

    """
    Class responsible for consult the MCD, and save
    all the front covers of the manga
    """

    def __init__(self, manga_id, muID=None):
        self.base_url = "https://mcd.iosphe.re/api/v1/series/%s/"
        self.manga_id = manga_id
        self.muID = muID
        self.covers = []

    def get(self):
        """
        Request the manga covers from MCD,
        then stores all the front cover of the manga
        """
        try:
            req = Request(self.base_url % self.muID)

            page = "Error"
            while page is "Error":
                page = req.request_page()

            data = json.loads(page)
            sections = data['Covers']
            for key, covers in sections.items():
                for cover in covers:
                    if cover['Side'] == 'front':
                        cover_obj = {
                            'url': cover['Raw'],
                            'width': cover['RawX'],
                            'height': cover['RawY']
                        }
                        self.covers.append(cover_obj)

        except Exception as err:
            print("Covers get error: ", err)


    def save(self):
        """
        Saves the covers in the database
        """
        try:
            database = Database()
            query = """INSERT INTO cover VALUES (NULL, %s, %s, %s, %s)"""
            for cover in self.covers:
                database.execute(query,
                                 [cover['url'], cover['width'], cover['height'], self.manga_id])

            print("Found %s cover(s)" % len(self.covers))

        except Exception as err:
            print("Covers save error: ", err)
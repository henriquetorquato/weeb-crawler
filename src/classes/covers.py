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

    def save(self):
        """
        Saves the covers in the database
        """
        new_covers = 0
        database = Database()
        check_query = """SELECT id FROM cover WHERE url=%s AND manga_id=%s"""
        insert_query = """INSERT INTO cover VALUES (NULL, %s, %s, %s, %s)"""
        for cover in self.covers:
            result = database.execute(check_query, [cover['url'], self.manga_id])
            if result is ():
                database.execute(insert_query,
                                [cover['url'], cover['width'], cover['height'], self.manga_id])
                new_covers += 1

        print("Found %s new cover(s)" % new_covers)

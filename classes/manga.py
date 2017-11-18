import json
from classes.database import Database
from classes.request import Request

class Manga:

    def __init__(self, index, names):

        self.index = index
        self.names = names
        self.db = Database()


    def check_manga(self):
        """
        Responsible for checking if the manga is already
        at the database, if it is then updates the informations,
        if not then get all the info and then save it
        """
        try:
            query = """SELECT * FROM manga WHERE muID=%s""" % self.index
            if self.db.execute(query) is ():
                self.get_info()
                self.save_manga()
            else:
                print("Manga already present: ", self.names[0])

        except Exception as err:
            print("Manga database check error: ", err)


    def get_info(self):

        try:
            req = Request('https://mcd.iosphe.re/api/v1/series/%s/' % self.index)
            obj = json.loads(req.request_page())
            self.release_year = obj['ReleaseYear']
            self.status_tags = obj['StatusTags']
            self.gender_tags = obj['Tags']
            self.official_title = obj['Title']
            self.artists = obj['Artists']
            self.authors = obj['Authors']
            self.covers = obj['Covers']

        except Exception as err:
            print("Manga get info error: ", err)


    def save_manga(self):

        try:
            query = """INSERT INTO manga VALUES (NULL, %s, %s, %s, 0)"""
            self.db.execute(query, [self.index, self.release_year, self.official_title])
            print("Added new manga: %s" % self.official_title)

        except Exception as err:
            print("Manga save error", err)


    

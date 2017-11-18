import json
from classes.database import Database
from classes.request import Request

class Manga:

    def __init__(self, index, names):

        self.database_id = None
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
            query = """SELECT * FROM manga WHERE muID=%s"""
            result = self.db.execute(query, [self.index])
            if result is ():
                self.get_info()
                self.save_manga()
                self.save_gender_tags()
                self.save_status_tags()
                self.save_titles()
                self.save_artists()
                self.save_authors()
                print("Added new manga: %s" % self.official_title)

            else:
                self.database_id = result[0][0]
                print("Manga already present: ", self.names[0])

        except Exception as err:
            print("Manga database check error: ", err)


    def get_info(self):
        """
        Request using id and store info in class
        """
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
        """
        Save the main part of the manga
        """
        try:
            query = """INSERT INTO manga VALUES (NULL, %s, %s, %s, 0)"""
            self.db.execute(query, [self.index, self.release_year, self.official_title])
            self.database_id = self.db.last_inserted_id()

        except Exception as err:
            print("Manga save error", err)


    def save_gender_tags(self):
        """
        Save the gender tags of the manga
        """
        try:
            for gender_tag in self.gender_tags:
                gender_id = None

                query = """SELECT * FROM gender_tags WHERE tag_name=%s"""
                result = self.db.execute(query, [gender_tag])
                if result is ():
                    query = """INSERT INTO gender_tags VALUES(NULL, %s)"""
                    self.db.execute(query, [gender_tag])
                    gender_id = self.db.last_inserted_id()
                else:
                    gender_id = result[0][0]

                query = """INSERT INTO manga_gender_tags VALUES (%s, %s)"""
                self.db.execute(query, [gender_id, self.database_id])

        except Exception as err:
            print("Manga gender tag save error: ", err)


    def save_status_tags(self):
        """
        Save the status tags of the manga
        """
        try:
            for status_tag, tag_value in self.status_tags.items():
                query = """INSERT INTO manga_status_tags VALUES
                ((SELECT id FROM status_tags WHERE tag_name=%s), %s, %s)"""
                self.db.execute(query, [status_tag, self.database_id, tag_value])

        except Exception as err:
            print("Manga status tag save error: ", err)


    def save_titles(self):
        """
        Save the alternative titles of the manga
        """
        try:
            for manga_title in self.names:
                query = """INSERT INTO titles VALUES (NULL, %s, %s)"""
                self.db.execute(query, [manga_title, self.database_id])

        except Exception as err:
            print("Manga title save error: ", err)


    def save_authors(self):
        """
        Save the author(s) of the manga
        """
        try:
            for author in self.authors:
                query = """INSERT INTO authors VALUES (NULL, %s, %s)"""
                self.db.execute(query, [author, self.database_id])

        except Exception as err:
            print("Manga author save error: ", err)


    def save_artists(self):
        """
        Save the artist(s) of the manga
        """
        try:
            for artist in self.artists:
                query = """INSERT INTO artists VALUES (NULL, %s, %s)"""
                self.db.execute(query, [artist, self.database_id])

        except Exception as err:
            print("Manga artist save error: ", err)

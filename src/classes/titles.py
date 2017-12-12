from src.classes.database import Database
from src.classes.logging import Logging

class Titles:

    """
    Class responsible for inserting the manga alternative
    titles in the database
    """

    def __init__(self, manga_id, titles=None):

        self.log = Logging("weeb_crawler")

        self.manga_id = manga_id
        if titles is None:
            self.titles = []
        else:
            self.titles = titles


    def save(self):
        """
        Insert the manga alternative titles
        in the database
        """
        new_titles = 0
        database = Database()
        check_query = """SELECT id FROM titles WHERE name=%s AND manga_id=%s"""
        insert_query = """INSERT INTO titles VALUES (NULL, %s, %s)"""
        for title in self.titles:
            result = database.execute(check_query, [title, self.manga_id])
            title = title[1:] if title[0] == " " else title

            if title != "-" and result is ():
                database.execute(insert_query, [title, self.manga_id])
                new_titles += 1

        self.log.info("Found %s new alternative title(s)" % new_titles)

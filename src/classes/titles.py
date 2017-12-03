from src.classes.database import Database

class Titles:

    """
    Class responsible for inserting the manga alternative
    titles in the database
    """

    def __init__(self, manga_id, titles=None):
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
        try:
            database = Database()
            check_query = """SELECT id FROM titles WHERE name=%s AND manga_id=%s"""
            insert_query = """INSERT INTO titles VALUES (NULL, %s, %s)"""
            for title in self.titles:
                result = database.execute(check_query, [title, self.manga_id])
                if title != "-" and result is ():
                    database.execute(insert_query, [title, self.manga_id])
            print("Found %s alternative title(s)" % len(self.titles))

        except Exception as err:
            print("Alternative title save error: ", err)

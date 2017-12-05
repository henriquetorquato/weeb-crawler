from src.classes.database import Database

class Authors:

    """
    Class responsible for inserting the authors in the database
    """

    def __init__(self, manga_id, authors=None):
        self.manga_id = manga_id
        if authors is None:
            self.authors = []
        else:
            self.authors = authors


    def save(self):
        """
        Save the manga authors at the database
        """
        new_authors = 0
        database = Database()
        check_query = """SELECT id FROM authors WHERE name=%s AND manga_id=%s"""
        insert_query = """INSERT INTO authors VALUES (NULL, %s, %s)"""
        for author in self.authors:
            result = database.execute(check_query, [author, self.manga_id])
            if result is ():
                database.execute(insert_query, [author, self.manga_id])
                new_authors += 1

        print("Found %s new author(s)" % new_authors)
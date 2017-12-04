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
        database = Database()
        query = """INSERT INTO authors VALUES (NULL, %s, %s)"""
        for author in self.authors:
            database.execute(query, [author, self.manga_id])

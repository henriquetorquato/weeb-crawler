from src.classes.database import Database

class Artists:

    """
    Class responsible for inserting the artists in the database
    """

    def __init__(self, manga_id, artists=None):
        self.manga_id = manga_id
        if artists is None:
            self.artists = []
        else:
            self.artists = artists


    def save(self):
        """
        Save the manga artists in the database
        """
        database = Database()
        query = """INSERT INTO artists VALUES (NULL, %s, %s)"""
        for artist in self.artists:
            database.execute(query, [artist, self.manga_id])

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
        new_artists = 0
        database = Database()
        check_query = """SELECT id FROM artists WHERE name=%s AND manga_id=%s"""
        insert_query = """INSERT INTO artists VALUES (NULL, %s, %s)"""
        for artist in self.artists:
            result = database.execute(check_query, [artist, self.manga_id])
            if result is ():
                database.execute(insert_query, [artist, self.manga_id])
                new_artists += 1
        
        print("Found %s new artist(s)" % new_artists)

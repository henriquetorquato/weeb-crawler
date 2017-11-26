from src.classes.database import Database
from src.classes.pages import Pages

class Chapter:

    def __init__(self, url, manga_id):

        self.chapter_id = None
        self.manga_id = manga_id
        self.url = url
        self.number = url.split("/")[-1]
        self.save_chapter()
        self.pages = Pages(url, self.chapter_id, self.manga_id)

    def save_chapter(self):
        """
        Save the chapter in the database
        """
        try:
            query = """INSERT INTO chapter VALUES (NULL, %s, %s, %s)"""
            database = Database()
            database.execute(query, [self.number, self.url, self.manga_id])
            self.chapter_id = database.last_inserted_id()
            return True

        except Exception as err:
            print("Chapter %s save error: ", err)
            return False

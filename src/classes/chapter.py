from src.classes.database import Database
from src.classes.pages import Pages

class Chapter:

    def __init__(self, manga_id, url=""):

        self.chapter_id = None
        self.manga_id = manga_id
        self.url = url
        self.number = url.split("/")[-1]
        self.pages = []


    def save(self):
        """
        Save the chapter in the database
        """
        try:
            database = Database()
            check_query = """SELECT id FROM chapter WHERE manga_id=%s AND number=%s"""
            insert_query = """INSERT INTO chapter VALUES (NULL, %s, %s, %s)"""
            result = database.execute(check_query, [self.manga_id, self.number])
            if result is ():
                database.execute(insert_query, [self.number, self.url, self.manga_id])
                self.chapter_id = database.last_inserted_id()
            else:
                self.chapter_id = result[0][0]

        except Exception as err:
            print("Chapter %s save error: ", err)


    def get_pages(self):
        """
        Instantiate the pages class, and call for
        pages methods
        """
        self.pages = Pages(self.manga_id, self.chapter_id, self.url)
        self.pages.save()

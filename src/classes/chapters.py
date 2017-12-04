from src.classes.database import Database
from src.classes.pages import Pages

class Chapters:

    def __init__(self, manga_id, urls=None):
        if urls is None:
            self.urls = []
        else:
            self.urls = urls

        self.manga_id = manga_id


    def save(self):
        """
        Save the chapter in the database
        """
        try:
            database = Database()
            check_query = """SELECT id FROM chapter WHERE manga_id=%s AND number=%s"""
            insert_query = """INSERT INTO chapter VALUES (NULL, %s, %s, %s)"""
            for url in self.urls:
                chapter_id = None
                chapter_number = url.split("/")[-1]
                result = database.execute(check_query, [self.manga_id, chapter_number])

                if result is ():
                    database.execute(insert_query, [chapter_number, url, self.manga_id])
                    chapter_id = database.last_inserted_id()

                else:
                    chapter_id = result[0][0]

                chapter_pages = Pages(self.manga_id, chapter_id, url)
                chapter_pages.save()

        except Exception as err:
            print("Chapter %s save error: ", err)

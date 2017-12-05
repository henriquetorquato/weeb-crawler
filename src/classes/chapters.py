from src.classes.database import Database
from src.classes.pages import Pages

class Chapters:

    """
    Get the chapters of the manga
    """

    def __init__(self, manga_id, urls=None):
        if urls is None:
            self.urls = []
        else:
            self.urls = urls

        self.all_pages = False
        self.manga_id = manga_id


    def save(self):
        """
        Save the chapter in the database
        """
        new_chapters = 0
        database = Database()
        check_query = """SELECT id, all_pages FROM chapter WHERE manga_id=%s AND number=%s"""
        insert_query = """INSERT INTO chapter VALUES (NULL, %s, %s, 0, %s)"""
        update_query = """UPDATE chapter SET all_pages=1 WHERE id=%s"""
        for url in self.urls:
            chapter_id = None
            chapter_number = url.split("/")[-1]
            result = database.execute(check_query, [self.manga_id, chapter_number])

            if result is ():
                database.execute(insert_query, [chapter_number, url, self.manga_id])
                chapter_id = database.last_inserted_id()
                new_chapters += 1

            else:
                chapter_id = result[0][0]
                self.all_pages = True if result[0][1] == 1 else False

            if not self.all_pages:
                chapter_pages = Pages(self.manga_id, chapter_id, url)
                chapter_pages.save()
                database.execute(update_query, [chapter_id])

        print("Found %s new chapter(s)" % new_chapters)

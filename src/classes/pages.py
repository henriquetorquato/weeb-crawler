from src.classes.request import Request
from src.classes.database import Database

class Pages:

    """
    Get the pages of the chapter, of a manga
    """

    def __init__(self, manga_id, chapter_id, chapter_url=""):

        self.chapter_id = chapter_id
        self.manga_id = manga_id
        self.chapter_url = chapter_url
        self.chapter = self.get_chapter()
        self.pages = self.get_pages()


    def get_chapter(self):
        """
        Request the chapters and returns a soup
        """
        req = Request(self.chapter_url)
        soup = req.soup()
        return soup


    def get_pages(self):
        """
        Find the images on the page
        """
        pages = []
        page_containers = self.chapter.findAll("img",
                                               {"class": "real img-responsive", "id": True})
        for page in page_containers:
            if page['id'] not in ["imagem-forum", "imagem-anime"]:
                pages.append(page['data-lazy'])

        return pages


    def save(self):
        """
        Saves the manga pages
        """
        database = Database()
        check_query = """SELECT id FROM page WHERE img_url=%s"""
        insert_query = """INSERT INTO page VALUES (NULL, %s, %s, %s)"""
        for page in self.pages:
            result = database.execute(check_query, [page])
            if result is ():
                database.execute(insert_query, [page, self.chapter_id, self.manga_id])

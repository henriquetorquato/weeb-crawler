from src.classes.request import Request
from src.classes.database import Database

class Pages:

    def __init__(self, chapter_url, chapter_id, manga_id):

        self.chapter_id = chapter_id
        self.manga_id = manga_id
        self.url = chapter_url
        self.error_count = 0
        self.chapter = self.get_chapter()
        self.pages = self.get_pages()
        self.save_pages()


    def get_chapter(self):
        """
        Request the chapters and returns a soup
        """
        try:
            req = Request(self.url)
            soup = req.soup()
            return soup

        except Exception as err:
            self.error_count += 1
            print("Get chapters error: ", err)


    def get_pages(self):
        """
        Find the images on the page
        """
        try:
            pages = []
            page_containers = self.chapter.findAll("img",
                                                   {"class": "real img-responsive", "id": True})
            for page in page_containers:
                if page['id'] not in ["imagem-forum", "imagem-anime"]:
                    pages.append(page['data-lazy'])

            return pages

        except Exception as err:
            self.error_count += 1
            print("Get pages error: ", err)


    def save_pages(self):
        """
        Saves the manga pages
        """
        try:
            database = Database()
            query = """INSERT INTO page VALUES (NULL, %s, %s, %s)"""
            for page in self.pages:
                database.execute(query, [page, self.chapter_id, self.manga_id])

        except Exception as err:
            print("Save page error: ", err)

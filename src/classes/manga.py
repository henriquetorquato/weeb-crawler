import json
from src.classes.database import Database
from src.classes.request import Request
from src.classes.chapter import Chapter

class Manga:

    def __init__(self, url):

        self.url = url
        self.id = None

        query = """SELECT id FROM manga WHERE page_url=%s"""
        database = Database()
        result = database.execute(query, [url])
        if result is ():
            self.page = self.get_page()
            self.title = self.get_title()
            self.description = self.get_description()
            self.muID = self.get_mu_id()
            self.alternative_titles = None
            self.gender_tags = None
            self.authors = None
            self.artists = None
            self.status = None
            self.get_header_info()
            self.save_manga()
            self.get_chapters()
        else:
            self.id = result[0][0]


    def get_page(self):
        """
        Requests the manga page and returns a soup
        """
        try:
            req = Request(self.url)
            soup = req.soup()
            return soup

        except Exception as err:
            print("Manga page request error: ", err)


    def get_title(self):
        """
        Get the manga title, return the text of the first h2
        """
        try:
            return self.page.findAll("h2")[0].text

        except Exception as err:
            print("Manga title search error: ", err)


    def get_description(self):
        """
        Get the manga description, search for a div with
        a specific class and returns the inner text
        """
        try:
            desc_container = self.page.find("div", {"class": "panel panel-default"})
            desc_body = desc_container.find("div", {"class": "panel-body"})
            return desc_body.text

        except Exception as err:
            print("Manga description search error: ", err)


    def get_header_info(self):
        """
        Get the manga indo present on the top of the page
        """
        try:
            header_content = self.page.findAll("h4", {"class": "media-heading manga-perfil"})

            self.alternative_titles = header_content[0].contents[1:]

            gender_tags_container = header_content[1].findAll("a", {"href": True})
            self.gender_tags = [tag.text for tag in gender_tags_container]

            self.authors = header_content[2].contents[1:]
            self.artists = header_content[3].contents[1:]

            status_tag = header_content[4].find("span")
            self.status = status_tag.text

        except Exception as err:
            print("Manga header info search error: ", err)


    def get_mu_id(self):
        """
        Uses MCD api to search for the
        id to be user on MCD and Manga Updates
        """
        try:
            mu_id = None
            req = Request('https://mcd.iosphe.re/api/v1/search/')
            results = req.get_json({"Title": self.title})
            for result in results['Results']:
                if self.title == result[1]:
                    mu_id = result[0]

            return mu_id

        except Exception as err:
            print("MCD search error: ", err)


    def get_chapters(self):
        """
        Get all the chapter from the manga main page,
        then save each one
        """
        try:
            chapter_containers = self.page.findAll("div", {"class": "row lancamento-linha"})
            for chapter_container in chapter_containers:
                chapter_container = chapter_container.findAll("div",
                                                              {"class": "col-xs-6 col-md-6"})[0]
                chapter = Chapter(chapter_container.findAll("a", {"href": True})[0]['href'], self.id)

        except Exception as err:
            print("Chapters search error: ", err)


    def save_manga(self):
        """
        Save the manga in the database
        """

        try:
            database = Database()
            if self.id is None:
                query = """INSERT INTO manga VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)"""
                database.execute(query, [self.muID, self.url, None, self.title,
                                         self.description, self.status, 0, None])
                self.id = database.last_inserted_id()
                print("Added new manga: [%s] %s" % (self.id, self.title))
            else:
                print("Already at database: [%s]" % self.id)

        except Exception as err:
            print("Save manga error: ", err)



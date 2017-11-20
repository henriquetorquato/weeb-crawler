import json
from classes.database import Database
from classes.request import Request
from classes.chapters import Chapters

class Manga:

    def __init__(self, url):

        self.url = url
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

        print("[%s] %s" % (self.muID, self.title))


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

import json
from urllib import request, error
from bs4 import BeautifulSoup

class Request:

    """
    Handles the requests, and return a soup
    """

    def __init__(self, url):

        self.req = request.Request(url, headers=self.read_header())


    def read_header(self):
        """
        Returns the header in the json file
        """
        try:
            header_file = open("lib/data/header.json", "r")
            header_obj = json.loads(header_file.read())
            return header_obj

        except (OSError, IOError) as err:
            print(err)
            return []


    def request_page(self):
        """
        Makes the actual request, return a soup
        """
        try:
            response = request.urlopen(self.req)
            return BeautifulSoup(response.read(), "html5lib")

        except error.HTTPError as err:
            return err


    def soup(self):
        """
        Request wrapper, to garante request is successful
        """
        request_result = self.request_page()
        while isinstance(request_result, str):
            request_result = self.request_page()

        return request_result

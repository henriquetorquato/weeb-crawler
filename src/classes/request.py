import json, zlib
from requests import get, post, exceptions
from bs4 import BeautifulSoup
from src.classes.logging import Logging

class Request:

    """
    Handles the requests
    """

    def __init__(self, url):

        self.log = Logging("Requests")
        self.url = url
        self.decode_gzip = lambda response: zlib.decompress(response, 16 + zlib.MAX_WBITS)


    def header(self, header_type):
        """
        Returns the get header stored in the json file
        """
        try:
            header_file = open("src/headers/%s.json" % header_type, "r")
            header_obj = json.loads(header_file.read())
            return header_obj

        except (OSError, IOError) as err:
            self.log.error(err)
            return {'':''}


    def request_page(self):
        """
        Makes the actual request, return a soup
        """
        try:
            req = get(self.url, headers=self.header('get'))
            while req.status_code != 200:
                req = get(self.url, headers=self.header('get'))

            if req.encoding == 'gzip':
                return self.decode_gzip(req.text)
            else:
                return req.text
            
        except exceptions.TooManyRedirects:
            self.log.error("Request too many redirections on url <%s>" % self.url)
            return "Error"

        except exceptions.Timeout:
            self.log.error("Request timeout on url <%s>" % self.url)
            return "Error"

        except exceptions.RequestException as err:
            self.log.error(err)
            return "Error"


    def get_json(self, send_data=None):
        """
        Send json post and expects a json return
        """
        if send_data is None:
            send_data = []

        try:
            req = post(self.url, headers=self.header('post'), data=json.dumps(send_data))
            return req.json()

        except Exception as err:
            self.log.error(err)


    def soup(self):
        """
        Request wrapper, to garante request is successful
        """
        request_result = self.request_page()
        while request_result is "Error":
            request_result = self.request_page()

        return BeautifulSoup(request_result, "html5lib")

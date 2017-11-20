from classes.database import Database
from classes.request import Request

class Chapters:

    def __init__(self, manga):

        self.manga = manga
        self.char_to_line = [' ', ':', '!', '.', ',', '=', '--']
        self.char_to_none = ['(', ')']
        self.base_url = 'http://unionmangas.net/manga/%s'
        self.name = None
    
    def format_name_to_url(self):

        self.name = self.manga.official_title.lower()

        for char in self.char_to_line:
            self.name = self.name.replace(char, '-')

        for char in self.char_to_none:
            self.name = self.name.replace(char, '')

        self.name = self.name.replace("'", '’')

        if self.name[-1] == '-':
            self.name = self.name[:-1]

        print('%s - %s' % (self.manga.official_title, self.name))

import pymysql
from classes.config import Config
from classes.singleton import Singleton

class Database(metaclass=Singleton):

    """
    Class responsible for connecting and making
    operations on the database, it uses a singleton
    to maintain a always open connection,
    thus saving resources
    """

    def __init__(self):

        conf = Config()
        database_conf = conf.get('database')
        self.host = database_conf['host']
        self.name = database_conf['name']
        self.user = database_conf['user']
        self.passwd = database_conf['passwd']

        self.conn = self.connect()


    def connect(self):
        """
        Responsible for opening the connection to the database
        and setting the charset
        """
        try:
            conn = pymysql.connect(self.host,
                                   self.user,
                                   self.passwd,
                                   self.name)
            cursor = conn.cursor()
            conn.set_charset('utf8')
            cursor.execute('SET NAMES utf8;')
            cursor.execute('SET CHARACTER SET utf8;')
            cursor.execute('SET character_set_connection=utf8;')
            return conn

        except pymysql.MySQLError as err:
            print(err)
            return False


    def disconnect(self):
        """
        Responsible for closing the connection to the database
        """
        self.conn.close()


    def execute(self, query, params=None):
        """
        Responsible for executing queries on the database
        """
        if params is None:
            params = []

        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            return cursor.fetchall()

        except pymysql.MySQLError as err:
            print(err)
            return []
import pymysql
from classes.config import Config

class Database:

    def __init__(self):

        conf = Config()
        database_conf = conf.get('database')
        self.host = database_conf['host']
        self.name = database_conf['name']
        self.user = database_conf['user']
        self.passwd = database_conf['passwd']

        self.conn = self.connect()


    def connect(self):

        try:
            conn = pymysql.connect(self.host,
                                   self.user,
                                   self.passwd,
                                   self.name)
            return conn

        except pymysql.MySQLError as err:
            print(err)
            return False

    
    def disconnect(self):

        self.conn.close()

    def query(self, query):

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            print(cursor.fetchall())
            self.disconnect()

        except pymysql.MySQLError as err:
            print(err)
            return []
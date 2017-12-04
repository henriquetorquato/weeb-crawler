from src.classes.database import Database

class Genders:

    """
    Class responsible for managing the genders of
    the manga
    """

    def __init__(self, manga_id, genders=None):
        self.manga_id = manga_id
        if genders is None:
            self.genders = []
        else:
            self.genders = genders


    def save(self):
        """
        Checks for existing genders on the database,
        then links the gender to the manga
        """
        gender_id = None
        database = Database()
        check_query = """SELECT id FROM gender_tags WHERE tag_name=%s"""
        insert_query = """INSERT INTO gender_tags VALUES (NULL, %s)"""
        foreign_query = """INSERT INTO manga_gender_tags VALUES (%s, %s)"""
        for gender in self.genders:
            result = database.execute(check_query, [gender])
            if result is ():
                database.execute(insert_query, [gender])
                gender_id = database.last_inserted_id()

            else:
                gender_id = result[0][0]

            database.execute(foreign_query, [gender_id, self.manga_id])
            
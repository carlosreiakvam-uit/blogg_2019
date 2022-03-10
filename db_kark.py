import mysql.connector
from mysql.connector import cursor


class Db:
    def __init__(self) -> None:
        dbconfig = {'host': 'kark.uit.no',
                    'user': 'stud_v21_reiakvam',
                    'password': 'tresko',
                    'database': 'stud_v21_reiakvam', }
        self.configuration = dbconfig

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor(prepared=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def getAll(self):
        query = ("SELECT * FROM oppslag INNER JOIN kategori ON kategori = kategori.kat_id ")
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def getCategory(self, kategori):
        self.cursor.execute("SELECT * FROM oppslag INNER JOIN kategori ON kategori = kategori.kat_id "
                            "WHERE kategori.navn = %s ", (kategori,))
        result = self.cursor.fetchall()
        return result

    def getPost(self, db_id):
        self.cursor.execute("UPDATE oppslag SET treff = treff+1 WHERE oppslag.id = %s", (db_id,))
        self.cursor.execute("SELECT * FROM oppslag INNER JOIN kategori ON kategori = kategori.kat_id "
                            "WHERE oppslag.id = %s", (db_id,))
        result = self.cursor.fetchall()
        return result

    def createPost(self, vals):
        sql = "INSERT INTO oppslag (kategori, bruker,tittel,ingress,oppslagstekst ) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, vals)

    def deletePost(self, db_id):
        self.cursor.execute("DELETE FROM oppslag WHERE id = %s;", (db_id,))

    def updatePost(self, vals):
        sql = """UPDATE
            oppslag
            SET
            kategori = %s,
            tittel = %s,
            ingress = %s,
            oppslagstekst = %s
            WHERE
            id = %s;"""
        self.cursor.execute(sql, vals)

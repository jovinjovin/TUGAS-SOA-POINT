import uuid

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

from nameko.extensions import DependencyProvider

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection

    def add_news(self, judul, isi, gambar):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        cursor.execute("""
        SELECT * FROM news 
        WHERE judul = %s;
        """, (judul,))
        for row in cursor.fetchall():
            result.append({
                'judul': row['judul'],
                'isi': row['isi'],
                'gambar': row['gambar']
            })
        if result:
            cursor.close()
            return "News Sudah ada!"
        else:
            cursor = self.connection.cursor(dictionary=True)
            generateUUID = str(uuid.uuid4())
            cursor.execute("""
            INSERT INTO news (id, judul, isi, gambar)
            VALUES (%s, %s, %s, %s);
            """, (generateUUID, judul, isi , gambar))
            cursor.close()
            self.connection.commit()
            return "Add News Success!"

    def edit_news(self, judul, isi, gambar):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        cursor.execute("""
        SELECT * FROM news 
        WHERE judul = %s;
        """, (judul,))
        for row in cursor.fetchall():
            result.append({
                'judul': row['judul'],
                'isi': row['isi'],
                'gambar': row['gambar']
            })
        if result:
            cursor.execute("""
            UPDATE news SET judul = %s, isi = %s, gambar = %s
            """, (judul, isi , gambar))
            cursor.close()
            self.connection.commit()
            return "News sudah di edit!"
        else:
            cursor.close()
            return "News tidak ada!"

    def get_all_news(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        cursor.execute("""
        SELECT * FROM news;
        """)
        for row in cursor.fetchall():
            result.append({
                'judul': row['judul'],
                'isi': row['isi'],
                'gambar': row['gambar']
            })
        if result:
            cursor.close()
            return result
        else:
            cursor.close()
            return "News tidak ada!"

    def get_news_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        cursor.execute("""
        SELECT * FROM news
        WHERE id = %s;
        """, (id, ))
        for row in cursor.fetchall():
            result.append({
                'judul': row['judul'],
                'isi': row['isi'],
                'gambar': row['gambar']
            })
        if result:
            cursor.close()
            return result
        else:
            cursor.close()
            return "News tidak ada!"

    def delete_news(self, id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("""
        DELETE FROM news
        WHERE id = %s;
        """, (id, ))
        cursor.close()
        self.connection.commit()
        return "News sudah di delete!"

    def download_file_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        cursor.execute("""
        SELECT * FROM news
        WHERE id = %s;
        """, (id, ))
        for row in cursor.fetchall():
            result.append({
                'judul': row['judul'],
                'isi': row['isi'],
                'gambar': row['gambar']
            })
        if result:
            cursor.close()
            return result
        else:
            cursor.close()
            return "News tidak ada!"

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="database_pool",
                pool_size=5,
                pool_reset_session=True,
                host='localhost',
                database='soa',
                user='root',
                password=''
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
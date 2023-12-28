from abc import ABC, abstractmethod
import logging
import psycopg


logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Datastore(ABC):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    @abstractmethod
    def getData(self):
        pass
    
    @abstractmethod
    def putData(self):
        pass

class SqlDB(Datastore):
    def __init__(self,host="127.0.0.1"):
        super().__init__()
        self.host = host
        self.db = "url"
        self.username = "testuser"
        self.password = "password"
        self.table_name = "url_mapping"
  
    def connectToDb(self):
        connection = psycopg.connect(
            host=self.host,
            user=self.username,
            dbname=self.db,
            password=self.password
        )
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        return connection, cursor

    def close_connection(self,connection, cursor):
        cursor.close()
        connection.close()
    
    def getData(self,short_url):
        connection,cursor = self.connectToDb()
        response = None
        short_url = f"http://squeezer/{short_url}"
        try:
            #query = f"SELECT * FROM {self.table_name};"
            cursor.execute("SELECT * FROM url_mapping WHERE short_url = %s;", (short_url,))
            response = list(cursor.fetchone())
        except Exception as e:
            print(f"I can't drop our test database! : {e}")
        finally:
            self.close_connection(connection,cursor)
            return response
    
    def putData(self,uid,short_url,long_url):
        connection,cursor = self.connectToDb()
        
        try:
            cursor.execute("INSERT INTO url_mapping (id,short_url, long_url) VALUES (%s, %s, %s);",
            (uid,short_url, long_url))
            # Commit the transaction
            connection.commit()
            self.logger.info(f"Record Created into Table: {self.table_name}")
        except Exception as e:
            connection.rollback()
            print(f"Error: {e}")
        finally:
            # Close the connection
            self.close_connection(connection, cursor)

    def checkLongUrl(self,long_url):
        connection,cursor = self.connectToDb()
        response = None
        try:
            #query = f"SELECT * FROM {self.table_name};"
            cursor.execute("SELECT * FROM url_mapping WHERE long_url = %s;", (long_url,))
            response = list(cursor.fetchone())
        except Exception as e:
            print(f"I can't drop our test database! : {e}")
        finally:
            self.close_connection(connection,cursor)
            return response
        
    
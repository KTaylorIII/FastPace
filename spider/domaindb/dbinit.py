from config import *
import sqlite3

class Initializer:
    def __init__(self):
        pass;
    

    def init_db(self, cleanup=False):
        """ Initializes the database at config.SQLITE_FILE_DIR.
        Cleans up residual data from prior crawls as well as recreates relevant 
        tables in the DB File.
        """
        if cleanup:
            self.cleanup_db();
        self._init_domains_db();


    def cleanup_db(self):
        conn = self._connect_db();
        c = conn.cursor();
        if self._table_exists('Domains'):
            c.execute('DROP TABLE Domains');
        conn.commit();
        conn.close();


###
## HELPER METHODS
###



    def _connect_db(self):
        return sqlite3.connect(SQLITE_FILE_DIR);


    def _table_exists(self, tablename):
        conn = self._connect_db();
        c = conn.cursor();
        c.execute('SELECT * FROM SQLITE_MASTER WHERE name = ?', (tablename,));
        results = c.fetchall();
        conn.close();
        if not results:
            return False;
        else:
            return True;


    def _init_domains_db(self):
        if not self._table_exists('Domains'):
            conn = self._connect_db();
            c = conn.cursor();
            c.execute('CREATE TABLE Domains (id INT NOT NULL, url TEXT NOT NULL, title TEXT NOT NULL)');
            conn.commit();
            conn.close();

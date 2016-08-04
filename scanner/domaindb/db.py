from config import *

import sqlite3


class Domains:
    
    def __init__(self):
        pass;


    def fetch_domains(self):
        conn = self._connectdb();
        c = conn.cursor();

        c.execute('SELECT * FROM Domains');
        results = c.fetchall();
        conn.close();
        return results;
        
    def add_domain(self, data):
        # data: Expected args include url, title, and date visited
        # Future items of note may include lexical analysis of suspected
        # websites' involvement in illicit activities

        pass;
    def purge_domains(self):
        # Eliminates all data in DB.

    def _connectdb(self):
        return sqlite3.connect(SQLITE_FILE_DIR);

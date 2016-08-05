from config import *
from dbinit import Initializer
import sqlite3


class DomainsInterface:
    
    def __init__(self, suppress_domains=False):
        pass;


    def initialize_db(self):
        Initializer().init_db();


    def fetch_domain(self, url):
        url = unicode(url);
        conn = self._connectdb();
        c = conn.cursor();
        
        c.execute('SELECT * FROM Domains WHERE url = ?', (url,));
        result = c.fetchone();
        if result:   
            domain = {};
            domain['id'] = result[0];
            domain['url'] = unicode(result[1]);
        
            return domain;
        else:
            return False;

    def fetch_domains(self):
        conn = self._connectdb();
        c = conn.cursor();

        c.execute('SELECT * FROM Domains');
        results = c.fetchall();
        conn.close();
        if not results:
            return False;
        domains = [];
        for result in results:
            domain = {};
            domain['id'] = result[0];
            domain['url'] = unicode(result[1]);
            domains.append(domain);
        return domains;
        
    def add_domain(self, data):
        if DEBUG:
            print '[*] ' + data['url'];
        # data: Expected args include url, title, and date visited
        # Future items of note may include lexical analysis of suspected
        # websites' involvement in illicit activities
        
        domain = {};
        domain['id'] = self._get_max_id() + 1;
        domain['url'] = unicode(data['url']);
        domain['title'] = unicode(data['title']);

        conn = self._connectdb();
        c = conn.cursor();
        c.execute('INSERT INTO Domains (id, url, title) VALUES (?,?,?)', (domain['id'],domain['url'],domain['title'],));
        conn.commit();
        conn.close();

    def purge_domains(self):
        # Eliminates all data in DB.
        Initializer().cleanup_db();


###
## HELPER METHODS
###
    def _connectdb(self):
        return sqlite3.connect(SQLITE_FILE_DIR);
    def _get_max_id(self):
        conn = self._connectdb();
        c = conn.cursor();
        c.execute('SELECT MAX(id) FROM Domains');
        result = c.fetchone()[0];
        if result:
            return result;
        else:
            return 0;

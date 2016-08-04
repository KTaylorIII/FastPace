import pycurl
import io
import atexit
from config import *
import stem.process

class Strapper:
    """
    A pycurl & stem wrapper that simplifies the request process.
    """
    def __init__(self):
        # TOR_CONFIG referenced from local config.py
        self.tor = stem.process.launch_tor_with_config(TOR_CONFIG);
        atexit.register(self._handle_termination);


    def request(self, url):
        """
        Takes a url and outputs the requested html document.
        HTMLParser expected to handle the request elsewhere in the program.
        """
    
        buffer = io.BytesIO();
        query = pycurl.Curl();
        query.setopt(pycurl.URL, url);
        query.setopt(pycurl.PROXY, 'localhost');
        # SOCKS_PORT referenced from local config.py
        query.setopt(pycurl.PROXYPORT, SOCKS_PORT);
        query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME);
        query.setopt(pycurl.WRITEFUNCTION, buffer.write);
        
        try:
            query.perform();
            return buffer.getvalue();
        except pycurl.error as e:
            return False;
        

###
## HELPER METHODS
###
    def _handle_termination(self):
        self.tor.kill();





from htmlparser.parser import Parser
from domaindb.db import DomainsInterface
from stemwrapper.strapper import Strapper

class Scanner:
    def __init__(self):
        self.parser = Parser();
        self.requester = None;

    def start(self, starturl):
        if not self.parser.is_tor_service(starturl):
            print '[-] ERROR: ' + starturl + ' is not a valid tor service!'
            return False;
        iface = DomainsInterface();


        self.requester = Strapper();
        

    def _processurl(url):
        pass;
    

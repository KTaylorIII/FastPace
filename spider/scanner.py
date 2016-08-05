from htmlparser.parser import Parser
from domaindb.db import DomainsInterface
from stemwrapper.strapper import Strapper

from config import *

class Scanner:
    def __init__(self):
        self.parser = Parser();
        self.requester = None;

    def start(self, starturl):
        if not self.parser.is_tor_service(starturl):
            print '[-] ERROR: ' + starturl + ' is not a valid tor service!'
            return False;
        iface = DomainsInterface();
        iface.initialize_db();
        if iface.fetch_domain(self.parser.extract_domain_from_link(starturl)):
            print '[-] ERROR: ' + starturl + ' has already been mapped!'
            print 'Have you purged the database yet?';
            return False;

        self.requester = Strapper();
        response = self.requester.request(starturl);
        if not response:
            print '[-] ERROR: ' + starturl + ' does not exist!';
            return False;

        else:
            root_link_path = starturl;
            data = {};
            data['url'] = self.parser.extract_domain_from_link(starturl);
            data['title'] = self.parser.extract_title(response);
            if DEBUG:
                print '[!] ' + root_link_path + ' - ' + data['title'];

            iface.add_domain(data);
            links = self.parser.extract_links(response);
            for link in links:
                self._processurl(link, root_link_path + ' -> ' + link);
        

    def _processurl(self, url, linkpath):
        
        if not self.parser.is_tor_service(url):
            return False;
        dbface = DomainsInterface();
        domain = self.parser.extract_domain_from_link(url);
        if dbface.fetch_domain(domain):
            return False;
        response = self.requester.request(url);
        if not response:
            return False;
        else:
            data = {};
            data['url'] = self.parser.extract_domain_from_link(url);
            data['title'] = self.parser.extract_title(response);
            if DEBUG:
                print '[!] ' + linkpath + ' - ' + data['title'];

            dbface.add_domain(data);
            links = self.parser.extract_links(response);
            for link in links:
                try:
                    self._processurl(link, linkpath + ' -> ' + link);
                except Exception:
                    continue;






from htmlparser.parser import Parser
from domaindb.db import DomainsInterface
from stemwrapper.strapper import Strapper

class Scanner:
    def __init__(self, clear_db=False, verbosity=False):
        self.parser = Parser();
        self.requester = None;
        if clear_db:
            DomainsInterface().purge_domains();
        self.verbosity = verbosity;

    def start(self, starturl):
        if not self.parser.is_tor_service(starturl) and self.verbosity:
            print '[-] ERROR: ' + starturl + ' is not a valid tor service!'
            return False;
        iface = DomainsInterface();
        iface.initialize_db();
        if iface.fetch_domain(self.parser.extract_domain_from_link(starturl)) and self.verbosity:
            print '[-] ERROR: ' + starturl + ' has already been mapped!'
            print 'Have you purged the database yet?';
            return False;

        self.requester = Strapper();
        response = self.requester.request(starturl);
        if not response and self.verbosity:
            print '[-] ERROR: ' + starturl + ' does not exist!';
            return False;

        else:
            root_link_path = starturl;
            data = {};
            data['url'] = self.parser.extract_domain_from_link(starturl);
            data['title'] = self.parser.extract_title(response);
            if self.verbosity:
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
            if self.verbosity:
                print '[!] ' + linkpath + ' - ' + data['title'];

            dbface.add_domain(data);
            links = self.parser.extract_links(response);
            for link in links:
                try:
                    self._processurl(link, linkpath + ' -> ' + link);
                except Exception:
                    continue;






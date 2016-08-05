from bs4 import BeautifulSoup
import re

class Parser:

    """
    Contains two helper methods that:
    a.) Extract links from html using underlying BeautifulSoup & re methods
    b.) Determines whether a given service is a valid tor service
    c.) Strip trailing slashes and url information after, obtaining the domain
    """
    def __init__(self):
        pass;


    def extract_links(self, html):
        returnLinks = [];
        soup = BeautifulSoup(html, 'html.parser');
        links = soup.find_all('a');
        for link in links:
            returnLinks.append(link.get('href'));
        return returnLinks;


    def extract_title(self, html):
        soup = BeautifulSoup(html, 'html.parser');
        title = soup.title;
        if title:
            title_data = title.contents[0];
            return title_data;
        else:
            return 'Untitled';
    

    def is_tor_service(self, domainname):
        try:
            pattern = re.compile("\w+\.onion($|\/)");
            result = pattern.search(domainname);
            if not result:
                return False;
            else:
                return True;
        except TypeError:
            return False;
    def extract_domain_from_link(self, html):
        pattern = re.compile("\w+\.onion");
        result = pattern.search(html);
        return result.group();
        
###
##
###

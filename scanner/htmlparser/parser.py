from bs4 import BeautifulSoup
import re

class Parser:

    """
    Contains two helper methods that:
    a.) Extract links from html using underlying BeautifulSoup & re methods
    b.) Determines whether a given service is a valid tor service
    """
    def __init__(self):
        pass;

    def extract_links(html):
        returnLinks = [];
        soup = BeautifulSoup(htmlcode, 'html.parser');
        links = soup.find_all('a');
        for link in links:
            returnLinks.append(link.get('href'));
        return returnLinks;

    def is_tor_service(domainname):
        pattern = re.compile("\w\.onion($|\/)");
        result = pattern.search(domainname);
        if not result:
            return False;
        else:
            return True;

###
##
###

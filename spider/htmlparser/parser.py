import re

class Parser:

    """
    Contains helper methods that:
    a.) Extract links from html using re
    b.) Determines whether a given service is a valid tor service
    c.) Strip trailing slashes and url information after, obtaining the domain
    """
    def __init__(self):
        pass;


    def extract_links(self, html):
        """
        Uses regex to extract all .onion links from a page, whether bound
        in <a> tags or not.
        """
        
        link_pattern = re.compile('\w+\.onion');
        links = link_pattern.findall(html);
        uni_links = [];
        for link in links:
            uni_links.append(unicode(link));

        return uni_links;


    def extract_title(self, html):
        title_pattern = re.compile('(?<=\<title\>)(.)+(?=\<\/title\>)')
        result = title_pattern.search(html);
        if result:
            title_data = result.group();
            return unicode(title_data);
        else:
            return u'Untitled';
    

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
        return unicode(result.group());
        
###
##
###

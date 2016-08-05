from scanner import Scanner

if __name__=='__main__':
    url = raw_input('Enter a starting url from which to dig: ');
    scan = Scanner();
    scan.start(url);

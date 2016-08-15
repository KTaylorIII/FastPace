from spider.scanner import *
from views.argparser import Argparser
if __name__=='__main__':
    parser = Argparser();
    args = parser.parse();

    scanner = Scanner(clear_db=args['clear'], verbosity=args['verbosity']);
    
    if args['prompt']:
        url = raw_input('[?] Enter a .onion domain: ');
        scanner.start(url);

    

from spider.scanner import *
from views.argparser import Argparser



def main():
    parser = Argparser();
    args = parser.parse();
    
    if args['prompt']:
        url = raw_input('[?] Enter a .onion domain: ');
        Scanner(clear_db=args['clear'], verbosity=args['verbosity']).start(url);

    else:
        if not args['domain']:

            if args['verbosity']:

                print '[-] ERROR: You must specify the "prompt" flag or supply a valid .onion ID';
        else:
            scanner = Scanner(clear_db=args['clear'], verbosity=args['verbosity'])
            scanner.start(args['domain']);
if __name__=='__main__':
    main();

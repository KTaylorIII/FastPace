import argparse

class Argparser:
    
    def __init__(self):
        self.parser = argparse.ArgumentParser();
        self.parser.add_argument('-c','--clear', help='Clear database on run', action='store_true');
        self.parser.add_argument('-p','--prompt', help='Prompt the user for the initial .onion url', action='store_true');
        self.parser.add_argument('-v','--verbose', help='Adjust output verbosity', action='store_true');
        self.parser.add_argument('domain', nargs='?', help='A valid .onion domain name', default=False);

    def parse(self):
        args = self.parser.parse_args();
        returnval = {};
        returnval['clear'] = args.clear;
        returnval['prompt'] = args.prompt;
        returnval['verbosity'] = args.verbose;
        returnval['domain'] = args.domain;
        
        return returnval;
        
        
        

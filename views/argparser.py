import argparse

class Argparser:
    
    def __init__(self):
        self.parser = argpar.ArgumentParser();
        self.parser.add_argument('-c','--clear-database', help='Clear database on run', action='store_true');
        self.parser.add_argument('-p','--prompt-user', help='Prompt the user for the initial .onion url', action='store_true');

    def parse(self):
        args = self.parser.parse_args();
        return args;
        
        
        

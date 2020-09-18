"""Receive a list of files from a server.

If more than one file is to be recieved, the destination must be a directory.

Usage:
    ponyo_client SERVER PORT FILE ... DESTINATION

"""
from docopt import docopt
from pathlib import Path

def check_args(files, destination):
    if len(files) > 1:
        assert destination.endswith("/")

def main(ops):
    print(ops)

if __name__ == '__main__':
    main(docopt(__doc__))



#!/home/ubuntu/venv/tsunami-tcp/bin/python3
"""Copy files around like scp, but use tsunami-udp to do it FAST.

Usage:
    tsunami-scp [-d] FROM_PATH TO_PATH

Options:
    -d, --dry-run   Don't move anything, just say we did. Useful for checking that tsunami-scp is set up on both ends and the file(s) exist.
"""
from docopt import docopt
from pprint import pprint

def main():
    ops = docopt(__doc__)
    pprint(ops)

if __name__ == '__main__':
    main()


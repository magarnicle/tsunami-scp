#!/home/ubuntu/venv/tsunami-tcp/bin/python3
"""Copy files around like scp, but use tsunami-udp to do it FAST.

Usage:
    tsunami-scp [-d] FROM_PATH ... TO_PATH

Options:
    -d, --dry-run   Don't copy anything, just say we did. Useful for checking that tsunami-scp is set up on both ends and the file(s) exist.
"""
import sys
from docopt import docopt
from pprint import pprint

def start_server(file_name):
    """Starts the tsunami-udp server, ready to serve the file.

        file_name :: str
            The file to transfer.
        return :: int
            The port number of the server.
    """
    pass

def receive_file(file_name, port, dry_run=False):
    """Starts the tsunami-udp client, which then receives the file.

        file_name :: str
            The url - [username@][machine][:port]file_path - to send the file to.
        port :: int
            The port the server is listening on.
        dry_run :: bool
            Start the client but don't actually transfer the file.
        return :: int
            The return code of the client.
    """
    pass

def main():
    ops = docopt(__doc__)
    pprint(ops)
    for file_name in ops['TO_PATH']:
        port = start_server(ops['FROM_PATH'])
        code = receive_file(file_name, port, dry_run=ops['--dry-run']))
        if code != 0:
            return code
    return 0

if __name__ == '__main__':
    sys.exit(main())


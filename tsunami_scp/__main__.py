#!/home/ubuntu/venv/tsunami-tcp/bin/python3
"""Copy files around like scp, but use tsunami-udp to do it FAST.

Usage:
    tsunami-scp [-d] FROM_PATH ... TO_PATH

Options:
    -d, --dry-run   Don't copy anything, just say we did. Useful for checking that tsunami-scp is set up on both ends and the file(s) exist.
"""
import sys
import subprocess
import os
from docopt import docopt
from pprint import pprint

TSUNAMI_PATH = None
REMOTE_TSUNAMI_PATH = None

def start_server(file_name, timeout=None, ports=None):
    """Starts the tsunami-udp server, ready to serve the file.

        file_name :: str
            The file to transfer.
        timeout :: int
            End the subprocess after this many seconds. Necessary for testing,
            not particularly usefull otherwise.
        return :: int
            The port number of the server.

        (command)
    """
    assert os.path.exists(file_name)
    port_numbers = ports or range(46224, 47224)
    for port_number in port_numbers:
        ret_code = 0
        try:
            proc = subprocess.run([(TSUNAMI_PATH or 'tsunamid'), f'--port={port_number}'], cwd=os.path.dirname(file_name), timeout=timeout)
            ret_code = proc.returncode
        except subprocess.TimeoutExpired:
            break
    if ret_code != 0:
        raise Exception('All tsunami ports occupied')
    else:
        return port_number

def receive_file(server, destination_file_name, port, dry_run=False):
    """Starts the tsunami-udp client, which then receives the file.

        source_file_name :: str
            The file to receive.
        destination_file_name :: str
            The url - [username@][machine][:port]file_path - to send the file to.
        port :: int
            The port the server is listening on.
        dry_run :: bool
            Start the client but don't actually transfer the file.
        return :: int
            The return code of the client.

        (command)
    """
    args = [REMOTE_TSUNAMI_PATH or 'tsunami', f'--port={port_numer}', 'connect', server, 'get', destination_file_name]
    proc = subprocess.run()

    pass

def main():
    ops = docopt(__doc__)
    pprint(ops)
    for file_name in ops['TO_PATH']:
        port = start_server(ops['FROM_PATH'])
        code = receive_file(file_name, port, dry_run=ops['--dry-run'])
        if code != 0:
            return code
    return 0

if __name__ == '__main__':
    sys.exit(main())


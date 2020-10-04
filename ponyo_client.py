"""Receive a list of files from a server.

If more than one file is to be recieved, the destination must be a directory.

Usage:
    ponyo_client -s SERVER [-p PORT] DESTINATION FILE ... 

"""
import typing as ty
from docopt import docopt
from pathlib import Path
import sh
import multiprocessing

def check_args(files, destination):
    if len(files) > 1:
        assert destination.endswith("/")

def server(filenames):
    sh.tsunamid(" ".join(filenames))

def get_ssh_connection_string(server: str, username: str=None, port: int=None) -> str:
    connection_string = server
    if username:
        connection_string = f"{username}@{connection_string}"
    if port:
        connection_string = f"{connection_string}:{port}"
    return connection_string

def client(server: str, destination: str, filenames: ty.List[str], tsunami_port: int=None, ssh_username: str=None, ssh_port: int=None) -> None:
    tsunami_connection = f"{server} set port {tsunami_port}" if tsunami_port else server
    sh.ssh(get_ssh_connection_string(server, ssh_username, ssh_port), f"cd {destination} && /usr/local/bin/tsunami connect {tsunami_connection} get {' '.join(filenames)} exit")

def main(ops):
    print(ops)
    import pudb; pu.db
    server_thread = multiprocessing.Process(target=server, args=[ops["FILE"]])
    server_thread.start()
    try:
        client(ops["SERVER"], ops["DESTINATION"], ops["FILE"], ops["PORT"])
    except Exception:
        raise
    finally:
        server_thread.kill()

if __name__ == '__main__':
    main(docopt(__doc__))



"""Receive a list of files from a server.

If more than one file is to be recieved, the destination must be a directory.

Usage:
    ponyo_client -s SERVER [-p PORT] FILE DESTINATION

"""
import typing as ty
from docopt import docopt
from pathlib import Path
import subprocess

def check_args(files: ty.List[str], destination: str):
    if len(files) > 1:
        assert destination.endswith("/")

def get_server_args(filename: str) -> ty.Tuple[str, str]:
    path = Path(filename).expanduser()
    if path.is_dir():
        raise OSError(f"{filename} is a directory")
    return path.name, str(path.parent)

def get_ssh_connection_string(server: str, username: str=None, port: int=None) -> str:
    connection_string = server
    if username:
        connection_string = f"{username}@{connection_string}"
    if port:
        connection_string = f"{connection_string}:{port}"
    return connection_string

def client(server: str, filename: str, destination: str, tsunami_port: int=None, ssh_username: str=None, ssh_port: int=None) -> None:
    tsunami_connection = f"{server} set port {tsunami_port}" if tsunami_port else server
    destination_path = Path(destination)
    if not destination_path.is_dir:
        destination = str(destination_path.parent)
    subprocess.Popen([
        "/Users/Matt/Dev/tsunami-scp/client.sh",
        get_ssh_connection_string(server, ssh_username, ssh_port),
        destination,
        tsunami_connection,
        filename,
    ],
    stdin=subprocess.PIPE).wait()

def main(ops: ty.Dict[str, ty.Any]):
    print(ops)
    basename, directory = get_server_args(ops["FILE"])
    server_thread = subprocess.Popen(["tsunamid", basename], cwd=directory)
    try:
        client(ops["SERVER"], ops["FILE"], ops["DESTINATION"], ops["PORT"])
    except Exception:
        raise
    finally:
        server_thread.kill()

if __name__ == '__main__':
    main(docopt(__doc__))



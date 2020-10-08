"""Receive a list of files from a server.

If more than one file is to be recieved, the destination must be a directory.

Usage:
    ponyo_client -s SERVER [-p PORT] FILE DESTINATION

"""
import typing as ty
from docopt import docopt
from pathlib import Path
import sh
import multiprocessing
import subprocess
import threading

def check_args(files, destination):
    if len(files) > 1:
        assert destination.endswith("/")

def get_ssh_connection_string(server: str, username: str=None, port: int=None) -> str:
    connection_string = server
    if username:
        connection_string = f"{username}@{connection_string}"
    if port:
        connection_string = f"{connection_string}:{port}"
    return connection_string

def client(server: str, filename: str, destination: str, tsunami_port: int=None, ssh_username: str=None, ssh_port: int=None) -> None:
    tsunami_connection = f"{server} set port {tsunami_port}" if tsunami_port else server
    destination = Path(destination)
    if destination.is_dir:
        destination_dir = str(destination)
    else:
        destination_dir = str(Path(destination).parent)
    with open("/tmp/out.txt", "w+") as out_file:
        with open("/tmp/err.txt", "w+") as err_file:
            subprocess.Popen([
                "/Users/Matt/Dev/tsunami-scp/client.sh",
                get_ssh_connection_string(server, ssh_username, ssh_port),
                destination_dir,
                tsunami_connection,
                filename,
            ],
            #ssh_port), f"\"ls / && cd {destination_dir} && /usr/local/bin/tsunami 'connect {tsunami_connection} get {filename} exit'\""],
            stdin=subprocess.PIPE).wait()
            #sh.ssh(get_ssh_connection_string(server, ssh_username, ssh_port), f"\"cd {destination_dir} && /usr/local/bin/tsunami connect {tsunami_connection} get {filename} exit\"", _fg=True)

def main(ops):
    print(ops)
    #server_thread = threading.Thread(target=sh.tsunamid, args=[ops["FILE"]], kwargs={"cd": "/Users/Matt/Downloads"})
    #server_thread = multiprocessing.Process(target=sh.tsunamid, args=[ops["FILE"]], kwargs={"cd": "/Users/Matt/Downloads"})
    #server_thread.start()
    server_thread = subprocess.Popen(["tsunamid", ops['FILE']], cwd="/Users/Matt/Downloads")
    try:
        client(ops["SERVER"], ops["FILE"], ops["DESTINATION"], ops["PORT"])
    except Exception:
        raise
    finally:
        server_thread.kill()

if __name__ == '__main__':
    main(docopt(__doc__))



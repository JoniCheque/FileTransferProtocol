import logging
import socket
import time
import sys
import os

import protocol


def main():
    """Server main program.
    Main usage: python3 server.py [IP address], [Port number]"""
    logging.basicConfig(format='%(asctime)s: [SERVER] - %(message)s', level=logging.INFO)
    arguments = []

    logging.info('Running...')
    for argument in sys.argv:
        if not argument.__contains__('.py'):
            arguments.append(argument)

    client = arguments[0]
    port = int(arguments[1])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((client, port))
    sock.listen(5)

    try:
        while True:
            conn, addr = sock.accept()
            message = protocol.receive_message(conn)
            action, download_request = protocol.send_request(str(message))
            logging.info('Response on server are: {}'.format(action))

            if download_request:
                protocol.send_file(conn, action)

            else:
                protocol.send_message(conn, action)

    except KeyboardInterrupt:
        print('losing^')
        sock.close()



if __name__ == '__main__':
    main()


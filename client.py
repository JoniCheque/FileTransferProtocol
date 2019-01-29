import logging
import socket
import sys

import protocol


def main():
    """Client main program.
    Main usage: python3 client.py [IP address], [Port number]
    Program will launch TCP client and shows possible request."""
    logging.basicConfig(format='%(asctime)s: [CLIENT] - %(message)s', level=logging.INFO)
    arguments = []

    logging.info('Iterating over arguments.')
    for argument in sys.argv:
        if not argument.__contains__('.py'):
            arguments.append(argument)

    server = arguments[0]
    port = int(arguments[1])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))

    request = input('\nPossible request are LIST and DOWNLOAD,\n' +
            'LIST request do not take any parameters server respond with\n' +
            'LIST of files. DOWNLOAD method takes file name as parameter.\n' +
            'You can terminate FTP program with CTRL + c.\n' +
            'Please give your request: ')

    logging.info('Got request from user: {}'.format(request))

    protocol.send_message(s, request)
    protocol.handle_server_response(s, request)

    s.close()
    s = None
    logging.info('Connection closed')


if __name__ == '__main__':
    main()

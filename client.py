import logging
import socket
import sys

import protocol


def main():
    """Client main program.
    Main usage: python3 client.py [IP address], [Port number]
    Program will launch TCP client and shows possible request."""
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    arguments = []

    logging.info('Iterating over arguments.')
    for argument in sys.argv:
        if not argument.__contains__('.py'):
            arguments.append(argument)

    server = arguments[0]
    port = int(arguments[1])
    logging.info('Arguments parsed: (server: {}, port: {})'.format(server, port))

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((server, port))
                logging.info('Connected to server: {}'.format(s))

                request = input('Possible request are LIST and DOWNLOAD,\n' +
                        'LIST request do not take any parameters server respond with\n' +
                        'LIST of files. DOWNLOAD method takes file name as parameter.\n' +
                        'You can terminate FTP program with CTRL + c.\n' +
                        'Please give your request: ')

                logging.info('Got request: {}'.format(request))

                logging.info('protocol.send({}, {})'.format(s, request))
                protocol.send_message(s, request)
                received_message = protocol.receive_message(s)
                logging.info('Message received from server: {}'.format(received_message))

            except OSError as msg:
                s.close()
                s = None

        if s is None:
            print('Could not open socket (check server ip address and port)')
            sys.exit(1)

    except KeyboardInterrupt:
        print('\nBye!')
        sys.exit(0)


    # try except --> connection
    # if connection is is made use
    # with s:
    #   s.sendall(data or request)


if __name__ == '__main__':
    main()

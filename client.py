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

    if request.lower().__contains__('download'):
        f = open('./downloaded.jpeg', 'wb')
        data = s.recv(1024)

        while len(data) < 1024:
            f.write(data)
            data = s.recv(1024)
        logging.info('All data read! Closing a file')
        f.close()

    else:
        received_message = protocol.receive_message(s)
        logging.info('Message received from server: {}'.format(received_message))

    s.close()
    s = None
    logging.info('Connectin closed')

    """
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
    """

    # try except --> connection
    # if connection is is made use
    # with s:
    #   s.sendall(data or request)


if __name__ == '__main__':
    main()

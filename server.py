import logging
import socket
import time
import sys

import protocol


def main():
    """Server main program.
    Main usage: python3 server.py [IP address], [Port number]"""
    logging.basicConfig(format='%(asctime)s: [SERVER] - %(message)s', level=logging.INFO)
    arguments = []

    logging.info('Iterating arguments')
    for argument in sys.argv:
        if not argument.__contains__('.py'):
            arguments.append(argument)

    client = arguments[0]
    port = int(arguments[1])
    logging.info('Got client info: (client: {}, port: {})'.format(client, port))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info('Socket {} binded'.format(s))
    s.bind((client, port))
    logging.info('Listening sockets')
    s.listen(5)
    connection, address = s.accept()
    logging.info('Socket accepted: (connection: {}, address: {})'.format(connection, address))

    #while True:
    while True:
        logging.info('Connection status: {}'.format(connection))
        message = protocol.receive_message(connection)
        protocol.send_message(connection, 'Server got message')
        logging.info('Server send message to client')
        # Check that if these close connections is possible made 
        # in client side, then its easier to maintain amount of
        # connections.
    s.close()
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            logging.info('Socket {} binded'.format(s))
            s.bind((client, port))
            logging.info('Listening sockets')
            s.listen(5)
            connection, address = s.accept()
            logging.info('Socket accepted: (connection: {}, address: {})'.format(connection, address))

            while True:
                logging.info('Waiting client messages')
                logging.info('Connection status: {}'.format(connection))
                message = protocol.receive_message(connection)
                logging.info('Message as str: {}'.format(message))
                logging.info('Got message from client: {}'.format(message))
                protocol.send_message(connection, 'Server got message')
                logging.info('Server send message to client')
                # Check that if these close connections is possible made 
                # in client side, then its easier to maintain amount of
                # connections.
            connection.close()
            logging.info('Connection closed')

        except KeyboardInterrupt:
            print('\nBye!')
            sys.exit(0)
    """


if __name__ == '__main__':
    main()


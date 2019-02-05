import os
import socket
import logging

logging.basicConfig(format='%(asctime)s: [PROTOCOL] - %(message)s',
                    level=logging.INFO
                    )


def handle_server_response(socket, request=''):
    if request.lower().__contains__('download'):
        f = open('./downloaded.jpeg', 'wb')

        while True:
            data = socket.recv(1024)
            f.write(data)
            logging.info('Data length was: {}'.format(len(data)))
            if len(data) < 1024:
                break
        logging.info('All data read! Closing a file')
        f.close()

    else:
        received_message = receive_message(socket)
        logging.info('Message received from server: {}'.format(
                        received_message
                    ))


def handle_client_request(request=''):
    path = '../../Assignment05'

    if request.lower().__contains__('list'):
        print('LIST request got.')
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(
                path, f
                ))]

        return (files, False)

    elif request.lower().__contains__('download'):
        print('DOWNLOAD request got')
        print(request.split(" "))
        f = request.split(' ')[-1]
        return (path + '/' + f.strip("'"), True)

    else:
        print('Invalid request')


def send_request(*args):
    """Client and server both have two request each of them.
    Server request:
        - ERROR(error msg)
        - FILES(list of files)
    Client request:
        - LIST()
        - DOWNLOAD(file)
    Args:
    Return:
    """
    for arg in args:
        # Check if argument is socket instance and continue
        if isinstance(arg, socket.socket):
            sock = arg
            continue

        else:
            request = arg.lower()

        # Server statement for returning list from server to client
        if isinstance(arg, list):
            continue

        # Client statement for asking files
        if request.__contains__('list') or request.__contains__('download'):
            send_message(sock, arg)

        # Server statement for informate error which occured
        if request.__contains__('error'):
            logging.info('Contains error')

        # Server statement for files which are downloadable
        if request.__contains__('files'):
            logging.info('Contains files')


def send_file(socket, fullpath):
    """Send file to remote server
    Args:
        socket: socket which is initialized via ip address and port
        fullpath: fullpath contains path and filename which are going to sent
    Return:
    """
    f = open(fullpath, 'rb')
    data = f.read(1024)

    while data != b'':
        socket.send(data)
        data = f.read(1024)
    logging.info('Image was read successfully')


def receive_message(socket):
    """Receive data from message
    Args:
        socket: socket which is initialized via ip address and port
    Return:
        message_buffer: Content of buffer
    """
    message_buffer = ''
    message_length = receive_message_length(socket)
    received_length = 0

    while received_length < message_length:
        data = socket.recv(1024)
        message_buffer += str(data)
        received_length += len(data)

    return message_buffer


def receive_message_length(socket):
    """Gets packet full length.
    Args:
        socket: socket which is initialized via ip address and port
    Return:
        buffer_size: Size of buffer which is coming
    """
    buffer_size = ''
    while True:
        byte = socket.recv(1)
        if byte == b'':
            raise Exception('Error occured')
        if byte == b'\n':
            break
        buffer_size += str(byte)
    return len(buffer_size)


def send_data(socket, data):
    """Full message contains different parts and send_data(sock, data),
    will send only one part.
    TODO: How many parts there are after all?
    Args:
        socket: socket which is initialized via ip address and port
        data: file which is send to client machine
    Return:
    """
    total_sent = 0
    while total_sent < len(data):
        sent = socket.send(data)
        total_sent += sent


def send_message(socket, data):
    """Send full message with all parts where size is told, lists, files etc.
    Args:
        socket: socket which is initialized via ip address and port
        data: file which is send to client machine
    Return:
    """
    data_length = len(data)
    # send_data(socket, str(data_length) + '\n')
    data_as_bytes = bytes(str(data_length) + '\n', 'utf8')
    send_data(socket, data_as_bytes)
    send_data(socket, bytes(str(data), 'utf8'))

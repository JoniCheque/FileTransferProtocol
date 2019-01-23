import logging

logging.basicConfig(format='%(asctime)s: [PROTOCOL] - %(message)s', level=logging.INFO)

def send_request(**args):
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
    pass


def read_response(socket):
    """Reads answer after request.
 
    Args:
 
    Return:
    """
    pass


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
        logging.info('BYTE: {}'.format(byte))
        if byte == b'':
            raise Exception('Error occured')
        if byte == b'\n':
            break
        buffer_size += str(byte)
    
    logging.info('BUFFER SIZE: {}'.format(len(buffer_size)))
    return len(buffer_size)


def receive_message_part_lengths(socket):
    """Split whole message size to parts, file sizes is got from this.
 
    Args:
        socket: socket which is initialized via ip address and port 
    Return:
    """
    pass


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
    #send_data(socket, str(data_length) + '\n')
    data_as_bytes = bytes(str(data_length) + '\n', 'utf8')
    send_data(socket, data_as_bytes)
    send_data(socket, bytes(str(data), 'utf8'))

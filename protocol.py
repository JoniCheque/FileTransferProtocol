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


def receive_message_length(socket):
    """Gets packet full length.

    Args:
 
    Return:
    """
    pass


def receive_message_part_lengths(socket):
    """Split whole message size to parts, file sizes is got from this.
 
    Args:
 
    Return:
    """
    pass


def send_data(socket, data):
    """Full message contains different parts and send_data(sock, data),
    will send only one part.
    TODO: How many parts there are after all?
 
    Args:
 
    Return:
    """
    pass


def send_message(socket, message):
    """Send full message with all parts where size is told, lists, files etc.
 
    Args:
        
    Return:
    """
    pass

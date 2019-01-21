import socket
import sys

def main():
    """Client main program.
    Main usage: python3 client.py [IP address], [Port number]
    Program will launch TCP client and shows possible request."""
    arguments = []

    for argument in sys.argv:
        if not argument.__contains__('.py'):
            arguments.append(argument)
        
    for arg in arguments:
        print(type(arg))

    # Check that connection is established
    print('Possible request are LIST, DOWNLOAD.')
    

if __name__ == '__main__':
    main()

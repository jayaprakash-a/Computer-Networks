import socket
import sys



port = int(sys.argv[1])
address = sys.argv[0]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((address, port))

print client_socket.recv(1024)

client_socket.close()

import socket
import sys



port = int(sys.argv[2])
address = sys.argv[1]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



client_socket.connect((address, port))

while True:
	message_client = raw_input("Message to server: ")
	client_socket.send(message_client)
	print client_socket.recv(1024)

client_socket.shutdown(1)
client_socket.close()
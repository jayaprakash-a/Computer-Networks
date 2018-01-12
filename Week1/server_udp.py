import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


port = 8005

server_socket.bind(('10.64.1.173', port))

while(True):
	(message, address) = server_socket.recvfrom(1024)
	if message != None:
		print message , address
		server_socket.sendto("Received message", address)



# Author : Jayaprakash A
# Course : Computer Networks Laboratory
# Code : Echo server that can handle multiple clients concurrently



import socket
from threading import Thread


class Client_Thread(Thread):
	def __init__(self, client_connection, client_address):

		Thread.__init__(self)
		self.connection = client_connection
		self.address = client_address
 
 
	def run(self):
		while True : 
			try:
				message_client = self.connection.recv(1024) 
				print "Message from client", self.address, ": ", message_client
				if message_client == 'quit\r\n':
					self.connection.shutdown(1)
					self.connection.close()
					break
				else:
					self.connection.send(message_client)
			except socket.error:
				print "Connection error"



if __name__ == '__main__':


	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = 8001
	server_socket.bind(('127.0.0.1', port))
	server_socket.listen(1)

	while True:
			
		try:
			client_connection, client_address = server_socket.accept()
			new_client_thread = Client_Thread(client_connection, client_address)
			new_client_thread.start()
		except socket.error:
			print "Connection error"

	print "Server is exiting"
		

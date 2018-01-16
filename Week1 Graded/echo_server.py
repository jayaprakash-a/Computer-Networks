# Author : Jayaprakash A
# Course : Computer Networks Laboratory
# Code : Echo server that can handle multiple clients concurrently



import socket
import threading


class Client_Thread(Thread):
	def __init__(self, client_connection, client_address):

		Thread.__init__(self)
		self.connection = client_connection
		self.address = client_address
 
 
	def run(self):
		while True : 
			message_client = current_connection.recv(1024) 
			print "Message from client: ", message_client
			if message_client == 'quit\r\n':
				current_connection.shutdown(1)
				current_connection.close()
				break
			else:
				current_connection.send(message_client)



if __name__ == '__main__':


	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = 8005
	server_socket.bind(('10.64.13.131', port))
	server_socket.listen(1)

	list_threads = []

	while True:
			
		try:
			(client_connection, client_address) = server_socket.accept()
			new_client_thread = Client_Thread(client_connection, client_address)
			new_client_thread.start()
			list_threads.append(new_client_thread)
		except socket.error:
			print "Connection error"

	for threads in list_threads:
		threads.join()

	print "Server is exiting"
		
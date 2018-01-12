import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


port = 8005

server_socket.bind(('10.64.1.173', port))


def thread_receive(s):
	while(True):
		(message, address) = s.recfrom(1024)

def thread_read_user_message(s):
	while(True):
		message = str(input("ENTER MESSAGE")
		s.sendto("Sending message",(address,port))

thread1 = threading.Thread(target=thread_receive, args=(s,))
thread2 = threading.Thread(target=thread_read_user_message, args=(s,))

thread1.start()
thread2.start()

s.close()




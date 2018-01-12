import socket
import sys
import threading


port = int(sys.argv[1])
address = sys.argv[0]
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
def thread_receive(s):
	while(True):
		print s.recfrom(1024)

def thread_read_user_message(s):
	while(True):
		message = str(input("ENTER MESSAGE")
		s.sendto("Sending message",(address,port))



thread1 = threading.Thread(target=thread_receive, args=(s,))
thread2 = threading.Thread(target=thread_read_user_message, args=(s,))

thread1.start()
thread2.start()

s.close()


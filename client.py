import socket
c=socket.socket()
host=socket.gethostname()# if communicating in a lan change socket.gethostname() to ip address of the target computer
port=1114
c.connect((host,port))
while True:
	
	print (c.recv(1024))

	a=raw_input ("your message>>")
	c.send(a)
	


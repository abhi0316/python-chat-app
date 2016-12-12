import socket
a=socket.socket()
host=socket.gethostname()
port=1114
a.bind((host,port))

a.listen(100)
while True:
	c,addr=a.accept()
	c.send("thanks for connecting")
        while True:
		print (c.recv(1024))
		s=raw_input ("enter ur message:>>")
		c.send(s)

  
	


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(10)
n=0
while True:
	conn, addr = s.accept()
	while True:
		data = conn.recv(1024)
		n=n+1
		if not data: break
		if data == 'close':break
		conn.send(data)
	conn.close()
	if n == 11:break
print('end')	

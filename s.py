import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
n=0
print('start')
while True:
	conn, addr = s.accept()
	while True:
		data = conn.recv(1024)
		n=n+1
		if not data: break
		print('data')
		print(n)
		if data == 'close':break
		conn.send(data)
	conn.close()
	print('close')
	if n == 11:break
print('end')	

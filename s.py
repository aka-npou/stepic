import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
n=0
print('start')
while True:
	conn, addr = s.accept()
	data = conn.recv(1024)
	n=n+1
	print('data')
	print(n)
	if data == 'close':conn.close()
	conn.send(data)
	if n > 11:break
print('end')	

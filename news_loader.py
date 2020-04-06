import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    name = conn.recv(1024)
    with open(f'static/{name}', 'wb') as picture:
        while True:
            data = conn.recv(8192)
            if not data:
                break
            picture.write(data)

conn.close()

import socket

skt = socket.socket()

port = 9999
host = ''

skt.bind((host,port))
skt.listen(5)
print("socket is listening...")
conn,addr=skt.accept()

while True:
    data_receive = conn.recv(1024)
    print("Received:: %s"% (data_receive.decode()))
    data_send = str(input("Send:: "))
    conn.send(data_send.encode())
    continue


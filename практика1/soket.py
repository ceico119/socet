import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создаем сокет
listener.bind(("127.0.0.1", 6344))
listener.listen()

while True:
    socket_for_communication, addr = listener.accept()
    print("Connected by", addr)
    data = socket_for_communication.recv(1024)
    if data:
        print("received data from client: ", data)
        socket_for_communication.sendall(bytes(reversed(data)))
    else:
        print("")
    socket_for_communication.close()
listener.close()
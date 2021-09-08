import socket



while True:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_socket.bind(('', 12345))
    
    ping=1
    while ping<=5:
        message, address = server_socket.recvfrom(1024)
        message = message.upper()

        if message != '' :
            print('mesaj geldi',message)

        if (message.decode().startswith("PING")):
            server_socket.sendto("PONG".encode(), address)
        ping+=1
    server_socket.close()
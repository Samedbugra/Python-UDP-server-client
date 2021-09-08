import time
import socket


f=open("targethosts.txt","r")
i=1

while True:

    ip = f.readline().replace("\n","")
    addr = (ip , 12345)
    if addr == ('',12345):
        break
    print(f'\n{i}. HEDEF:{ip}')
    i=i+1
    for pings in range(5):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(1.0)
        message = b'PING'
        
        start = time.time()
        client_socket.sendto(message, addr)
        try:
            data, server = client_socket.recvfrom(1024)
            if data == b'PONG':
                end = time.time()
                elapsed = float("{:.2f}".format((end - start)/1000))
                print(f'{pings+1}.-> UDP:{ip} \n{pings+1}.<- RTT {elapsed} ms')
        except socket.timeout:
            print(f'{pings+1}.-> UDP:{ip} \n{pings+1}. PAKET KAYBI')
client_socket.close()
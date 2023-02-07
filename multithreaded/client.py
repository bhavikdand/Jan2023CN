import socket
import threading


def send_request(i):
    # 1 Create a socket object
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # AF_NET: ipv4 protocol
    # SOCK_STREAM: TCP and SOCK_DGRAM: UDP
    # 2 Connect to server
    server_host = '127.0.0.1'
    server_port = 8089
    client_sock.connect((server_host, server_port))  # 3-way handshake happens here
    # 3 Client sends request
    request_data = 'Hello from client #' + str(i)
    client_sock.sendall(bytes(request_data.encode('utf-8')))
    # send -> requires chopping of data into smaller parts before sending across the n/w
    # sendall -> handles the chopping part within itself
    # 4 Client gets response
    response_data = client_sock.recv(1024)
    resp_data_str = str(response_data.decode('utf-8'))
    print(resp_data_str)
    # 5 Client closes the socket
    client_sock.close()


for i in range(100):
    t = threading.Thread(target=send_request, args=(i,))
    t.start()


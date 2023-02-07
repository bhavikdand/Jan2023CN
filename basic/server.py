import socket

# Boot up the server

#1 Create socket object
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#2: Bind server_sock to host and port
server_host = '127.0.0.1'
server_port = 8089
server_sock.bind((server_host, server_port))

#3: Start listening to the port
server_sock.listen()

# Boot up is complete
print('Boot up is complete')
# For every request

#4 Accept the client connection
connection, address = server_sock.accept() # 3 way handshake happens here
print('Received a connection request from client')

#5 Server receives request from client
request_data = connection.recv(1024)
print('Received request from client')
#6 Process the request
print('Data: ' + str(request_data))

#7 Send response back to client
connection.sendall(bytes('Hello from server side'.encode('utf-8')))

#8 Close the connection
connection.close()

#9 Close the socket (Server terminates)
server_sock.close()

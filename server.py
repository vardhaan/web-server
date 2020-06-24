import socket

class TCPServer:
	host = '127.0.0.1'
	port = 8888

	'''
	We need to create a socket object to listen at address & port. 
	Then, accept a connection. Following that, receive data, then send it back.
	'''
	def start(self):
		listenSocket = socket.socket()
		listenSocket.bind((self.host, self.port))
		listenSocket.listen()

		print("Socket listening at ", listenSocket.getsockname())

		while True:

			connectSocket, connectAddress = listenSocket.accept()

			print("Connected by ", connectAddress)

			receivedData = connectSocket.recv(4096)

			print("received data: ", receivedData)

			sendStatus = connectSocket.sendall(receivedData)

			print("Send status: ", sendStatus)

			connectSocket.close()

			print("Connection closed")



if __name__ == '__main__':
    server = TCPServer()
    server.start()
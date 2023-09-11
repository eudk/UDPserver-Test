from socket import * #`Import the socket library`

serverPort = 20 #`Set the server port number to 12000`
serverSocket = socket(AF_INET, SOCK_DGRAM) #`Create a UDP socket for the server`

serverAddress = ('', serverPort) #`Set the server address to localhost and the server port number`

serverSocket.bind(serverAddress) #`Bind the socket to the server address`
print("The server is ready")#`Print the message that the server is ready`
while True:#`Loop forever`
    message, clientAddress = serverSocket.recvfrom(2048)#`Read the message from the client`
    print("Received message:" + message.decode())#`Print the received message`
    modifiedMessage = message.decode().upper()#`Convert the message to uppercase`
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)#`Send the modified message to the client`
from socket import *#`Import the socket library`

serverName = 'LOCALHOST'#`Set the server name to LOCALHOST`
serverPort = 12000#`Set the server port number to 12000`
clientSocket = socket(AF_INET, SOCK_DGRAM)#`Create a UDP socket for the client`

message = input('Input message:')#`Get the message from the user`
clientSocket.sendto(message.encode(), (serverName, serverPort))#`Send the message to the server`
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #`Receive the modified message from the server`
print((modifiedMessage.decode())) #`Print the received message`
clientSocket.close() # Close the socket
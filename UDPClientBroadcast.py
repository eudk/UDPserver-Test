from socket import *

serverName = '255.255.255.255' # Broadcast address
serverPort = 12000 #`Set the server port number to 12000`
clientSocket = socket(AF_INET, SOCK_DGRAM) #`Create a UDP socket for the client`
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) #`Set the socket option to broadcast`

message = input('Input message:') #`Get the message from the user`
clientSocket.sendto(message.encode(), (serverName, serverPort)) #`Send the message to the server`
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #`Receive the modified message from the server`
print((modifiedMessage.decode())) #`Print the received message`
clientSocket.close() # Close the socket
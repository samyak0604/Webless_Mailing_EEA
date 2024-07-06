import socket
import cv2
import pickle,struct
import imutils
from socket import *
serverName='localhost'
serverPort=5500
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
data=b""
payloadSize=struct.calcsize("Q")
while True:
	while len(data)<payloadSize:
		packet=clientSocket.recv(4096) 
		if not packet: break
		data+=packet
	packed_msgSize=data[:payloadSize]
	data=data[payloadSize:]
	msgSize=struct.unpack("Q",packed_msgSize)[0]
 
	while len(data)<msgSize:
		data+=clientSocket.recv(4096)
	frameData=data[:msgSize]
	data=data[msgSize:]
	frame=pickle.loads(frameData)
	cv2.imshow("RECEIVING VIDEO",frame)
	key=cv2.waitKey(1) & 0xFF
	if key==ord('q'):
		break
clientSocket.close()

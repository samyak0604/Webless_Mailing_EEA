import  socket
import cv2
import pickle,struct
import imutils
from socket import *
serverName='localhost'
serverPort=5500
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print("the server is ready to recieve")
while True:
	connectionSocket,addr=serverSocket.accept()
	if connectionSocket:
		vid=cv2.VideoCapture(0)
		while(vid.isOpened()):
			img,frame=vid.read()
			frame=imutils.resize(frame,width=320)
			a=pickle.dumps(frame)
			message=struct.pack("Q",len(a))+a
			connectionSocket.sendall(message)
			cv2.imshow('TRANSMITTING VIDEO',frame)
			key=cv2.waitKey(1) & 0xFF
			if key==ord('q'):
				connectionSocket.close()

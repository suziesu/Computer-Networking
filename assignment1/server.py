#import socket module
__author__ = 'Xi Su'

from socket import *
import datetime

"""
memo:
"**".join() :for loop join string and concatenate by **
date format use date.date.now.strftime() 

"""
serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
#Fill in start

serverPort = 6789
serverSocket.bind(('',serverPort))
serverSocket.listen(5)

#Fill in end
while True:
	#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	print "addr:\n", addr
	#Fill in start
	#Fill in end
	try:
		message = connectionSocket.recv(1024)#Fill in start #Fill in end 
		print "message: \n", message
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read() 
		print "outputdata:", outputdata
		now = datetime.datetime.now()
		#Fill in start #Fill in end 
		#Send one HTTP header line into socket
		#Fill in start
		first_header = "HTTP/1.1 200 OK"
		# alive ={
		# 	"timeout":10,
		# 	"max":100,
		# }
		header_info = {
			"Date": now.strftime("%Y-%m-%d %H:%M"),
			"Content-Length": len(outputdata),
			"Keep-Alive": "timeout=%d,max=%d" %(10,100),
			"Connection": "Keep-Alive",
			"Content-Type": "text/html"
		}
		
		following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
		print "following_header:", following_header
		connectionSocket.send("%s\r\n%s\r\n\r\n" %(first_header, following_header))
		# connectionSocket.send("\r\n")
		 # Date: %s\r\nKeep-Alive: timeout=10, max=100\r\n Connection: nKeep-Alive\r\n Content-Type: text/html;charset= utf-8" %(now.strftime("%Y-%m-%d %H:%m")))
		#Fill in end
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		#Fill in start 
		connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>")
		#Fill in end
		#Close client socket 
		#Fill in start 
		connectionSocket.close()
		#Fill in end
serverSocket.close()
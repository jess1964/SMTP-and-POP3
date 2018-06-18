from socket import *

import time
import sys
# Writen by Jesus Rodriguez
# I do not give consent for this program to be mis used in an illegal manner
# or to be redistributed
def SendMessage():
	msg = ""
	endmsg = "\r\n.\r\n"
	sub = ""
	#SERVER
	Emailserver = ("trig.sci.csueastbay.edu", 25) 

	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect(Emailserver)
	recv_fromServer = clientSocket.recv(1024)
	recv_fromServer = recv_fromServer.decode()#for trouble shooting

	# helo message
	heloCommand = 'HELO algebra.sci.csueastbay.edu\r\n'
	clientSocket.send(heloCommand.encode())
	recv2_fromServer = clientSocket.recv(1024)
	recv2_fromServer = recv2_fromServer.decode()#for trouble shooting 

	#Source EMail address 
	print("Your Email Address")# doesnt have to be an email address
	mailFrom = raw_input("Enter Identity Address: ")
	mailFrom = "MAIL FROM:<" + mailFrom +">\r\n"
	
	clientSocket.send(mailFrom.encode())
	recv2_fromServer = clientSocket.recv(1024)
	recv2_fromServer = recv2_fromServer.decode()# used to check status during troubleshooting 
	#destniation email address
	print("Who Would you like to Send an Email to?")
	rcptTo = raw_input("Enter Destination Address: ")	
	rcptTo = "RCPT TO:<"+ rcptTo + ">\r\n"
	
	clientSocket.send(rcptTo.encode())
	recv2_fromServer = clientSocket.recv(1024)
	recv2_fromServer = recv2_fromServer.decode()# used to check status during troubleshooting 
	#data command
	data = "DATA\r\n"
	clientSocket.send(data.encode())
	recv2_fromServer = clientSocket.recv(1024) # used to check status during troubleshooting 
	#subject message		
	sub = raw_input("Enter Subject here: ")
	message = raw_input("Enter your message here: ")
	#Body message
	msg = message + '\r\n'
	subject = "Subject: " + sub + '\r\n'
	 
	clientSocket.send(subject.encode())#send subject

	clientSocket.send(msg.encode())#send message

	clientSocket.send(endmsg.encode()) #end the message 

	return_msg = clientSocket.recv(1024) # used to check status during troubleshooting 
	#quit command 
	quit = "QUIT\r\n"
	clientSocket.send(quit.encode())
	recv2_fromServer = clientSocket.recv(1024)
	recv2_fromServer = recv2_fromServer.decode()
	if recv2_fromServer[:3] == '221':
		print("Message was sent successfully")


	clientSocket.close()

def CheckMessage():
	Emailserver = ("trig.sci.csueastbay.edu", 110)
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect(Emailserver)
	recv_fromServer = clientSocket.recv(1024)
	
        # authentication 
	
	user = raw_input("UserName: ")
	password = raw_input("Password: ")
	#user command
	user = ("USER " + user + "\r\n")
	print(user)
	clientSocket.send(user.encode())
	
	recv_fromServer = clientSocket.recv(1024)
	recv_fromServer = recv_fromServer.decode() #for troubleshooting
	print("Message returned :"+recv_fromServer)
	#pass command
	password = ("PASS "+ password +"\r\n")
	print(password)
	clientSocket.send(password.encode())
	recv_fromServer = clientSocket.recv(1024)
	recv_fromServer = recv_fromServer.decode() #for troubleshooting
	print("Message returned :"+recv_fromServer)
	
	#LIST command
	print("\n\n")
	POPList = ("LIST\r\n")
	clientSocket.send(POPList.encode())
	recv_fromServer = clientSocket.recv(1024)
	recv_fromServer = recv_fromServer.decode() #for troubleshooting
	print("Emails on Server\n"+recv_fromServer)
	
	SAnswer = raw_input('Please select an email from above')
	
	#select email with RETR command
	retr = ("RETR "+ SAnswer +"\r\n")
	clientSocket.send(retr.encode())
	recv_fromServer = clientSocket.recv(1024)
	recv_fromServer = recv_fromServer.decode() #for troubleshooting
	print("Emails on Server\n"+recv_fromServer)
	
	#delete email option
	print("\n\n Would you like to delete this email?\n")
	Answer = input("Yes: 1\n No: 2\n :")
	answer = int(Answer)
	print("\n\n")	
	if answer == 1:
		retr = ("DELE "+ SAnswer +"\r\n")
		clientSocket.send(retr.encode())
		recv_fromServer = clientSocket.recv(1024)
		recv_fromServer = recv_fromServer.decode() #for troubleshooting
		print("Emails on Server\n"+recv_fromServer)
	if answer == 2:
		retr = ("QUIT \r\n")
		clientSocket.send(retr.encode())
		recv_fromServer = clientSocket.recv(1024)
		recv_fromServer = recv_fromServer.decode() #for troubleshooting
		print("Emails on Server\n"+recv_fromServer)

#while loop to keep program running 
while(True):
	print("\n\n")	
	print("Please select from the menu")
	soption = input("1: Send Message\n2: Check Messages\n3: Terminate sessio\n :")
	option = int(soption)
	if option == 1:
		SendMessage()
		print("\n\n")
	if option == 2:
		CheckMessage()
		print("\n\n")
	if option == 3:
		sys.exit()
	

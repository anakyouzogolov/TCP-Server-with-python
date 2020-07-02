import socket

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# port 
port = 4000

""" binds the socket to a specific address """
s.bind(("",port)) 


""" Tells operating system to start listening for connections on the socket """
s.listen(5) 


while(True):
    c, a = s.accept() # Accept a new client connection ( Wait for next connection )
    print("Recived message from "+ str(a)) 
    c.send(b"Hello in server !!") # Send data to client
    c.close() # Close client connection
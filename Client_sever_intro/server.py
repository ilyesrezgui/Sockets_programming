import socket

s=socket.socket() #create a socket for the server.
# if no parameters are passed the type of ip adress is by default IPV4 and the type of connection is TCP
print("socket created")
#this socket of the server we created is what is going to accept the connections, so we have to bing this spcket to port number so it listens on it.
s.bind(('localhost',9999)) # first pass the ip adress, then the port number
s.listen(3) #I'm allowing my server to listen to up to 3 connection from 3 clients
print("waiting for connections")

while(True):
    c,addr=s.accept() # when the server accepts a socket that he recieved while listening , it will return a client socket in addition to the IP adress of the client
    name= c.recv(1024).decode()
    print("connected to client:",name,addr)
    c.send(bytes("welcome to Socket programming",'utf-8'))
    
    c.close()


import socket

IP=socket.gethostbyname(socket.gethostname()) #this will dynamically get an IP adress that is available
PORT= 4455
ADDR=(IP,PORT)

def main():
    
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("[CONNECTED]")
    client_socket.connect(ADDR)
    file=open(r"C:\Users\ilyes\OneDrive\Bureau\Sockets programming\File Transfer\data\mydata.txt",'r') 
    data=file.read()
    client_socket.send("mydata".encode("UTF-8"))
    print("[RCV]")
    message=client_socket.recv(1024).decode("UTF-8")
    print(f"[MESSAGE]{message}")
    client_socket.send(data.encode("UTF-8"))
    client_socket.close
    print("[DISCONNNECTED]")
    
if __name__=='__main__':
    main()

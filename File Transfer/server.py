import socket

IP=socket.gethostbyname(socket.gethostname()) #this will dynamically get an IP adress that is available
PORT= 4455
ADDR=(IP,PORT)
def main():
    print('[STARTING] Server is started')
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen()
    print('[LISTENING] Server is Listening')
    while True:
        conn,addr=server_socket.accept()
        filename=conn.recv(1024).decode("UTF-8")
        print(f'[New Connection] {addr} connected with {filename}')
        conn.send("[DATA] Filename Recieved".encode("UTF-8"))
        print("[RCV] Server recieved the data")
        data=conn.recv(1024).decode("UTF-8")
        
        with open(f"{filename}.txt","w") as f:
            f.write(data)
        f.close
        conn.close
        print("[DISCONNNECTED]")

    server_socket.close

        

if __name__=='__main__':
    main()

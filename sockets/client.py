import socket


def connect_to_server():
    host = str(input("Enter your host IP --> "))
    port = int(input("Port number --> "))

    skt = socket.socket()
    try:
        skt.connect((host,port))
        print("--Connection successfully established to %s / %s\n"%(host,str(port)))

        while True:
            data_send = str(input("Send:: "))
            skt.send(data_send.encode())
            print("Waiting for response...")
            data_receive = skt.recv(1024)
            print("\nResponse:: %s"%(data_receive.decode()))
            continue
    except Exception as e:
        print("Sorry something went wrong. --", e)


def view_active_connections():
    pass

print("What you want to do?\n")
services = ["Connect to server", "View active connections"]
total = len(services)

for i in range(1,total+1):
    print(i, services[i-1])
    if i==total:
        while True:
            choice = int(input("\nYour choice: "))
            if choice == 1:
                connect_to_server()
            elif choice == 2:
                view_active_connections()
            else:
                print("Invalid input. Please try agian")
                continue



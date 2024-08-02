#!/usr/bin/python3

#import socket and threading library 
import socket
import threading

def scan_port(host, port):
    #socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #timeout of 4 seconds for socket operations
    sock.settimeout(4)
    try:
        #attempt to connect to the specified host and port. It returns 0 if the connection is successfull, or an error code if it fails.
        result = sock.connect_ex((host, port))
        if result == 0:  #checks if the port is open
            print(f"Port {port}: Open")
            try:
                # Banner grabbing
                sock.send(b'Hello\r\n')#sends a hello message(bytes) to the open port.which can trigger a banner ;).
                banner = sock.recv(1024).decode().strip() #says how much data is received from the port then decodes it from bytes to a string while removing any whitespace.
                print(f"Banner: {banner}")
            except:
                print(f"Port {port}: Banner grabbing failed")
        else:
            print(f"Port {port}: Closed")
    except socket.error as e:#catches any socket-related errors and prints them.
        print(f"Error on port {port}: {e}")
    finally:
        sock.close()


def port_scanthread(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}..")
    for port in range(start_port, end_port + 1):#iterates over the range of ports from start_port to end_port (inclusive).
        thread = threading.Thread(target=scan_port, args=(host, port))#thread to run the scan_port function passing the host and port as arguments.
        thread.start()

if __name__ == "__main__":#main program execution
    host = input("Please enter the IP you want to scan: ")
    start_port = int(input("Please enter the start port you want to scan: "))
    end_port = int(input("Please enter the end port you want to scan: "))
    
    port_scanthread(host, start_port, end_port)
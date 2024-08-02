#!/usr/bin/python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(4)

host = input("Please enter the IP you want to scan")
port = int(input("Please enter the port you want to scan: "))


def portScanner(port):
    if sock.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)
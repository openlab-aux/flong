#!/usr/bin/env python 2
import threading
import socket
from time import sleep


class UserInput(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.usercmd = 2
        self.die = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", port))
        self.sock.setblocking(0)

    def run(self):
        while True:
            if self.die is True:
                return 0
            try:
                data, addr = self.sock.recvfrom(1024)
                self.usercmd = int(data)
            except socket.error:
                pass
            sleep(0.005)

    def __del__(self):
        self.sock.close()
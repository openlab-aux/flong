#!/usr/bin/python
import curses
import socket
import os
from time import sleep


def main(stdscr):

    IP = "10.11.7.56"
    PORT = 1331


    os.system("beep -f 50")
    stdscr.clear()
    os.system("beep -f 100")

    stdscr.keypad(True)
    os.system("beep -f 150")

    stdscr.nodelay(1)
    os.system("beep -f 200")
    stdscr.keypad(1)
    os.system("beep -f 250")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    os.system("beep -f 2000")
    while True:
        try:
            key = stdscr.getch()
        except:
            key = None
        if key == curses.KEY_DOWN:
            sock.sendto("1", (IP,PORT))
        if key == curses.KEY_UP:
            sock.sendto("0", (IP,PORT))
        sleep(0.1)

os.system("beep -f 20")
curses.wrapper(main)

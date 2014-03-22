#!/usr/bin/env python2
import socket
import game
from time import sleep
from server import UserInput

UDPHOST = "flipdot.ffa"
UDPPORT = 2323

WIDTH = 80
LENGTH = 16

FPS = 12.0

PARALLEL_GAMES = 1
DING = 4

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send(image):
    msg = '';
    pieces = '';
    for line in image:
        pieces += ''.join(str(x) for x in line)

    pieces = [pieces[i:i + 8] for i in range(0, len(pieces), 8)]

    for i in pieces:
        if len(i) < 8:
            i = i.ljust(8, '1')
        msg += chr(int(str(i), 2))

    sock.sendto(msg, (UDPHOST, UDPPORT))


def main():
    gameb = game.GameBoard(WIDTH, LENGTH)
    playerscores = [0, 0]
    playerthreads = [UserInput(1330), UserInput(1331)]
    try:
        playerthreads[0].start()

        playerthreads[1].start()
        while True:

            for idy in range(0, len(playerscores)):
                if playerscores[idy] is not gameb.gameobj[idy].score:
                    gameb.mk_scorebard()
                    send(gameb.get_board())
                    playerscores[idy] = gameb.gameobj[idy].score
                    sleep(3)
                    if playerscores[idy] is 9:
                        playerscores[0] = 0
                        playerscores[1] = 0
                        gameb.gameobj[0].score = 0
                        gameb.gameobj[1].score = 0
            for idx, item in enumerate(playerthreads):
                if item.usercmd is 0:
                    gameb.gameobj[idx].move(0, -1)
                    print "Player moved up"
                    item.usercmd = None
                elif item.usercmd is 1:
                    gameb.gameobj[idx].move(0, 1)
                    print "Player moved down"
                    item.usercmd = None

            gameb.mkboard()
            send(gameb.get_board())

            sleep(1.0 / FPS)
    except KeyboardInterrupt:
        playerthreads[0].die = True
        playerthreads[1].die = True
        return 0

main()

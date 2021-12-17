import socket
from _thread import *
import pickle
from game import Game

server = "192.168.0.16"  # my IPv4 Address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen()  # lets multiple clients connect (2 people)
print("Waiting for a connection")

connected = set()  # Stores id addresses of connected client
games = {}  # Store our games
idCount = 0  # Keep track of our current id


def threaded_client(conn, p, gameId):  # 1 of this function is running for every single client
    global idCount  # if someone leaves we need to subtract
    conn.send(str.encode(str(p)))  # So we know if we're player 0 or 1
    reply = ""

    while True:
        try:
            # get # get game from server
            # reset # reset game (client side)
            # move # (client side) sends move to server and updates it
            data = conn.recv(4096).decode()  # receive string data from client

            if gameId in games:  # If game still exists. Game deleted if client disconnects
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)  # Data is the move

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break

        except:
            break

    print("Lost Connection")

    try:
        del games[gamesId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


while True:  # keep looking for connections
    conn, addr = s.accept()  # accept any incoming connections and store it & the ip address
    print(f"Connected to {addr}")

    idCount += 1  # No. of people connected to server at once
    p = 0  # Current player
    gameId = (idCount - 1) // 2  # Every 2 players connected to server - incremented by 1

    if idCount % 2 == 1:  # E.g Odd no of players -  it needs a new game e.g p3
        games[gameId] = Game(gameId)
        print("Creating a new game")
    else:
        games[gameId].ready = True  # Both players connected
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))

import socket
from _thread import *
from player import Player
import pickle

server = "192.168.0.16"  # my IPv4 Address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(2)  # lets multiple clients connect (2 people)
print("Waiting for a connection")

players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))  # send player object and all it's values
    reply = ""
    while True:  # run while client still connected
        try:
            data = pickle.loads(conn.recv(2048))  # turn it into tuple
            players[player] = data  # update position

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print(f"Received: {data}")
                print(f"Sending: {reply}")

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost Connection")
    conn.close()


currentPlayer = 0

while True:  # keep looking for connections
    conn, addr = s.accept()  # accept any incoming connections and store it & the ip address
    print(f"Connected to {addr}")
    start_new_thread(threaded_client, (conn, currentPlayer))

    currentPlayer += 1  # Keep track of which player we're on

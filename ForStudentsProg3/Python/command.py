import sys
from mpi4py import MPI #mpi4py library
from dht_globals import * #global variables

def __init():
    global keys
    keys = list()

    for i in range(1000 + 1):
        keys.append(None)

def __getAll():
    global keys
    for i in range(len(keys)):
        if (keys[i] is None): continue
        MPI.COMM_WORLD.send(i, dest=0, tag=GET)
        answer = MPI.COMM_WORLD.recv(source=0, tag=RETVAL)
        print(f"val is {answer[0]}, storage id is {answer[1]}")


def commandNode():
    global keys
    __init()

    print("ADD: 2, rank: 1, ID: 20")
    MPI.COMM_WORLD.send([1, 20], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    print("ADD: 2, rank: 2, ID: 10")
    MPI.COMM_WORLD.send([2, 10], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    
    print("PUT: 0, key: 10, val: 11111")
    MPI.COMM_WORLD.send([10, 11111], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    # keys[10] = 11111

    print("GET: 10 and should get 11111")
    MPI.COMM_WORLD.send(10, dest=0, tag=GET)
    answer = MPI.COMM_WORLD.recv(source=0, tag=RETVAL)
    print(f"val is {answer[0]}, storage id is {answer[1]}")

    # print("PUT: 0, key: 25, val: 12345")
    # MPI.COMM_WORLD.send([25, 12345], dest=0, tag=PUT)
    # MPI.COMM_WORLD.recv(source=0, tag=ACK)
    # # keys[25] = 12345

    # print("Trying get 25 and should get 12345")
    # MPI.COMM_WORLD.send(25, dest=0, tag=GET)
    # answer = MPI.COMM_WORLD.recv(source=0, tag=RETVAL)
    # print(f"val is {answer[0]}, storage id is {answer[1]}")

    # print("PUT: 0, key: 15, val: 673")
    # MPI.COMM_WORLD.send([15, 673], dest=0, tag=PUT)
    # MPI.COMM_WORLD.recv(source=0, tag=ACK)
    # # keys[25] = 12345

    # print("Trying get 15 and should get 673")
    # MPI.COMM_WORLD.send(15, dest=0, tag=GET)
    # answer = MPI.COMM_WORLD.recv(source=0, tag=RETVAL)
    # print(f"val is {answer[0]}, storage id is {answer[1]}")

    # print("PUT: 0, key: 15, val: 673")
    # MPI.COMM_WORLD.send([15, 673], dest=0, tag=PUT)
    # MPI.COMM_WORLD.recv(source=0, tag=ACK)
    # keys[15] = 673

    # __getAll()

    MPI.COMM_WORLD.send(0, dest=0, tag=END)
    print("command finalizing")
    exit(0)

'''
Author: Quan Le
Class: CSC 422 - SP24
'''

import sys
from mpi4py import MPI  # mpi4py library
from dht_globals import *  # global variables

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

    print("ADDING")
    MPI.COMM_WORLD.send([3, 500], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    
    print("PUTTING")
    for i in range(250, 750 + 1, 5):
        MPI.COMM_WORLD.send([i, i], dest=0, tag=PUT)
        MPI.COMM_WORLD.recv(source=0, tag=ACK)
        keys[i] = True

    __getAll()

    print("ADDING storage id 400")
    MPI.COMM_WORLD.send([5, 400], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("PUTTING")
    for i in range(101, 451 + 1, 5):
        MPI.COMM_WORLD.send([i, i], dest=0, tag=PUT)
        MPI.COMM_WORLD.recv(source=0, tag=ACK)
        keys[i] = True

    __getAll()

    print("ADDING storage id 475")
    MPI.COMM_WORLD.send([4, 475], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("PUTTING")
    for i in range(403, 393 + 1, 5):
        MPI.COMM_WORLD.send([i, i], dest=0, tag=PUT)
        MPI.COMM_WORLD.recv(source=0, tag=ACK)
        keys[i] = True

    __getAll()

    print("REMOVING storage id 475")
    MPI.COMM_WORLD.send(475, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("ADDING storage id 50")
    MPI.COMM_WORLD.send([2, 50], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("ADDING storage id 999")
    MPI.COMM_WORLD.send([1, 999], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("PUTTING")
    for i in range(104, 904 + 1, 5):
        MPI.COMM_WORLD.send([i, i], dest=0, tag=PUT)
        MPI.COMM_WORLD.recv(source=0, tag=ACK)
        keys[i] = True

    __getAll()

    print("REMOVING storage id 999")
    MPI.COMM_WORLD.send(999, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("PUTTING")
    for i in range(954, 999 + 1, 5):
        MPI.COMM_WORLD.send([i, i], dest=0, tag=PUT)
        MPI.COMM_WORLD.recv(source=0, tag=ACK)
        keys[i] = True

    __getAll()
    
    print("ADDING storage id 999")
    MPI.COMM_WORLD.send([4, 999], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("ADDING storage id 399")
    MPI.COMM_WORLD.send([1, 399], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("REMOVING storage id 399")
    MPI.COMM_WORLD.send(399, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("ADDING storage id 401")
    MPI.COMM_WORLD.send([1, 401], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("REMOVING storage id 50")
    MPI.COMM_WORLD.send(50, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("REMOVING storage id 400")
    MPI.COMM_WORLD.send(400, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("REMOVING storage id 401")
    MPI.COMM_WORLD.send(401, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("REMOVING storage id 500")
    MPI.COMM_WORLD.send(500, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("REMOVING storage id 999")
    MPI.COMM_WORLD.send(999, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    MPI.COMM_WORLD.send(0, dest=0, tag=END)
    print("command finalizing")
    exit(0)

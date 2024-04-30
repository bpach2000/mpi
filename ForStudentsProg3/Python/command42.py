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

    # ADD
    print("ADDING")

    MPI.COMM_WORLD.send([5, 1], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    MPI.COMM_WORLD.send([4, 2], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    MPI.COMM_WORLD.send([3, 3], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    MPI.COMM_WORLD.send([2, 8], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    MPI.COMM_WORLD.send([1, 10], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    
    # PUT
    print("PUTTING")

    MPI.COMM_WORLD.send([1, 500], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[1] = True

    MPI.COMM_WORLD.send([2, 400], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[2] = True

    MPI.COMM_WORLD.send([3, 300], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[3] = True

    MPI.COMM_WORLD.send([4, 200], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[4] = True

    MPI.COMM_WORLD.send([5, 201], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[5] = True

    MPI.COMM_WORLD.send([6, 202], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[6] = True

    MPI.COMM_WORLD.send([7, 203], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[7] = True

    MPI.COMM_WORLD.send([8, 204], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[8] = True

    MPI.COMM_WORLD.send([9, 100], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[9] = True

    MPI.COMM_WORLD.send([10, 101], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[10] = True

    MPI.COMM_WORLD.send([11, 600], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[11] = True

    MPI.COMM_WORLD.send([12, 601], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[12] = True
    
    MPI.COMM_WORLD.send([999, 602], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[999] = True

    MPI.COMM_WORLD.send([1000, 603], dest=0, tag=PUT)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    keys[1000] = True

    __getAll()

    # REMOVE
    print("REMOVING storage id 2")

    MPI.COMM_WORLD.send(2, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    # REMOVE
    print("REMOVING storage id 3")
    
    MPI.COMM_WORLD.send(3, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    # ADD
    print("ADDING storage id 6")

    MPI.COMM_WORLD.send([3, 6], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    
    __getAll()

    # ADD
    print("ADDING storage id 7")

    MPI.COMM_WORLD.send([4, 7], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)
    
    __getAll()

    # REMOVE
    print("REMOVING storage id 1")

    MPI.COMM_WORLD.send(1, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    # ADD
    print("ADDING storage id 1")

    MPI.COMM_WORLD.send([5, 1], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    # REMOVE
    print("REMOVING storage id 1")

    MPI.COMM_WORLD.send(1, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    # ADD
    print("ADDING storage id 3")

    MPI.COMM_WORLD.send([5, 3], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    # REMOVE
    print("REMOVING storage id 3")

    MPI.COMM_WORLD.send(3, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    # ADD
    print("ADDING storage id 999")

    MPI.COMM_WORLD.send([5, 999], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    # REMOVE
    print("REMOVING storage id 6")
    MPI.COMM_WORLD.send(6, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("REMOVING storage id 7")
    MPI.COMM_WORLD.send(7, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("REMOVING storage id 8")
    MPI.COMM_WORLD.send(8, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()
    
    print("REMOVING storage id 10")
    MPI.COMM_WORLD.send(10, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print("REMOVING storage id 999")
    MPI.COMM_WORLD.send(999, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    MPI.COMM_WORLD.send(0, dest=0, tag=END)
    print("command finalizing")
    exit(0)

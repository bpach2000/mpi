'''
Author: Quan Le
Class: CSC 422 - SP24
'''

import sys
from mpi4py import MPI  # mpi4py library
from dht_globals import *  # global variables

def __getAll():
    print("GETTING")
    for i in range(1, 1000 + 1):
        MPI.COMM_WORLD.send(i, dest=0, tag=GET)
        answer = MPI.COMM_WORLD.recv(source=0, tag=RETVAL)
        print(f"val is {answer[0]}, storage id is {answer[1]}")

def commandNode():
    print("ADDING")
    for i in range(1, 5 + 1):
        MPI.COMM_WORLD.send([i, 150 * i], dest=0, tag=ADD)
        MPI.COMM_WORLD.recv(source=0, tag=ACK)

    print("PUTTING")
    for i in range(1, 1000 + 1):
        MPI.COMM_WORLD.send([i, i], dest=0, tag=PUT)
        MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print(f"REMOVING storage id {2 * 150}")
    MPI.COMM_WORLD.send(2 * 150, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()

    print(f"ADDING storage id {2 * 100}")
    MPI.COMM_WORLD.send([2, 2 * 100], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()
    
    print(f"REMOVING storage id {2 * 100}")
    MPI.COMM_WORLD.send(2 * 100, dest=0, tag=REMOVE)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    for i in range(1, 5 + 1):
        if (i == 2): continue
        print(f"REMOVING storage id {i * 150}")
        MPI.COMM_WORLD.send(i * 150, dest=0, tag=REMOVE)
        MPI.COMM_WORLD.recv(source=0, tag=ACK)
    
    __getAll()

    print("ADDING storage id 999")
    MPI.COMM_WORLD.send([1, 999], dest=0, tag=ADD)
    MPI.COMM_WORLD.recv(source=0, tag=ACK)

    __getAll()
    
    MPI.COMM_WORLD.send(0, dest=0, tag=END)
    print("command finalizing")
    exit(0)

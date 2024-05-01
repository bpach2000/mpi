## author: Brooke Pacheco

#!/usr/bin/env python3
import sys
from mpi4py import MPI #mpi4py library
from dht_globals import *
from command import commandNode #command node code

# on an END message, the head node is to contact all storage nodes and tell them
def headEnd():
    # tell all the storage nodes to END
    # the data sent is unimportant here, so just send a dummy value
    dummy = MPI.COMM_WORLD.recv(source=numProcesses-1, tag=END)
    for i in range(1,numProcesses-1):
        MPI.COMM_WORLD.send(dummy, dest=i, tag=END)
    MPI.Finalize()
    print("Shutdown command sent to all nodes.")
    sys.exit(0)
    
# on an END message, a storage node just calls MPI_Finalize and exits
def storageEnd(): 
    # the data is unimportant for an END
    dummy = MPI.COMM_WORLD.recv(source=0, tag=END)
    MPI.Finalize()
    sys.exit(0)

def getKeyVal(source):
    # each node has a dictionary storing key, value pairs
    global data

    #receive the GET message
    #note that at this point, we've only called MPI_Probe, which only peeks at the message
    #we are receiving the key from whoever sent us the message 
    key = MPI.COMM_WORLD.recv(source=source, tag=GET)
    
    if key <= myStorageId:

        # find the associated value (called "value") using whatever data structure you use
        # you must add this code to find it (omitted here)
        value = data.get(key)

        # allocate a tuple with two integers: the first will be the value, the second will be this storage id
        argsAdd = (value, myStorageId)
        MPI.COMM_WORLD.send(argsAdd, dest=childRank, tag=RETVAL)
    else:
        MPI.COMM_WORLD.send(key, dest=childRank,tag=GET)

def put(source):
    # get the key and value that will stored on the node
    key_value = MPI.COMM_WORLD.recv(source=source, tag=PUT)
    key, value = key_value

    # if the key is less than or equal to storage ID then put data in that node
    print(myStorageId)
    if myStorageId >= key:
        data[key] = value

        # we want to let command node know that put has been executed
        if myRank == 0:
            MPI.COMM_WORLD.send(0, dest=numProcesses-1, tag=ACK)
        else:
            MPI.COMM_WORLD.send(0, dest=childRank, tag=ACK)
        #print(f"Stored key {key} with value {value}")
    else:
        # keep fowarding put request to child node
        MPI.COMM_WORLD.send(key_value, dest=childRank, tag=PUT)

def add(source):
    global myStorageId, childRank, childId

    # get the rank and ID for the new node
    new = MPI.COMM_WORLD.recv(source=source, tag=ADD)
    newRank, newID = new

    if newID < childId:
        # save the old child rank
        oldChildRank = childRank

def handleMessages():
    status = MPI.Status()  # get a status object
    while True:
        # Peek at the message
        MPI.COMM_WORLD.probe(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)

        # Get the source and the tag - which MPI rank sent the message, and what the tag of that message was
        source = status.Get_source()
        tag = status.Get_tag()
        print(f"Source (rank): {source}, tag (command): {tag}")

        # Now take the appropriate action
        if tag == END:
            if myRank == 0:
                headEnd()
            else:
                storageEnd()
        elif tag == ADD:
            #add(source)
            data = MPI.COMM_WORLD.recv(source=source, tag=tag)
        elif tag == REMOVE:
            # Receive and handle REMOVE message
            data = MPI.COMM_WORLD.recv(source=source, tag=tag)
            # Placeholder: implement actual logic here
            print(f"Received REMOVE from {source}: {data}")
        elif tag == PUT:
            put(source)
        elif tag == GET:
            getKeyVal(source)
        elif tag == ACK: 
            # send message from rank 0 back to command node
            if myRank == 0:
                data = MPI.COMM_WORLD.recv(source=source, tag=ACK)
                MPI.COMM_WORLD.send(data, dest=numProcesses-1, tag=ACK)
                print(f"Fowarded ACK from {source}: {data}")
            else:
                # node just passes on the acknowledge
                data = MPI.COMM_WORLD.recv(source=source, tag=ACK)
                MPI.COMM_WORLD.send(data, dest=childRank, tag=ACK)
                print(f"Received RETVAL from {source}: {data}")
        elif tag == RETVAL:
            # send message from rank 0 back to command node
            if myRank == 0:
                data = MPI.COMM_WORLD.recv(source=source, tag=RETVAL)
                MPI.COMM_WORLD.send(data, dest=numProcesses-1, tag=RETVAL)
                print(f"Fowarded RETVAL from {source}: {data}")
            else:
                # node just passes on the recieve
                data = MPI.COMM_WORLD.recv(source=source, tag=RETVAL)
                MPI.COMM_WORLD.send(data, dest=childRank, tag=RETVAL)
                print(f"Received RETVAL from {source}: {data}")
        else:
            # Unknown tag received, handle error case
            print(f"ERROR: Unhandled tag {tag} received from rank {source}")
            sys.exit(1)


if __name__ == "__main__":
    global data
    data = dict()

    # get my rank and the total number of processes 
    numProcesses = MPI.COMM_WORLD.Get_size()
    myRank = MPI.COMM_WORLD.Get_rank()
    print(f"numProcesses {numProcesses} myRank {myRank}")

    # set up the head node 
    if myRank == 0:
        myStorageId = 0
        childRank = numProcesses - 2
        childId = MAX
        parentRank = None
        parentId = None
        
    # set up the last storage node
    elif myRank == numProcesses - 2:
        myStorageId = MAX
        childRank = 0
        childId = 0
        parentRank = 0
        parentId = 0
        data = {}

    # the command node is handled separately
    if myRank < numProcesses-1:
        handleMessages()
    else:
        commandNode()
    

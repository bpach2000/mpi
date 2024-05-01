global myStorageId, childRank, childId

    # get the rank and ID for the new node
    new = MPI.COMM_WORLD.recv(source=source, tag=ADD)
    newRank, newID = new

    if newID < childId:
        # save the old child rank
        oldChildRank = childRank

        # give new children to child node
        MPI.COMM_WORLD.send(new.append(myRank).append(myStorageId), dest=childRank, tag=UPDATE)

        # update the nodes child rank and ID to current node
        childRank = newRank
        childID = newID

        # the new node needs to be updated
        MPI.COMM_WORLD.send(data, dest=childRank, tag=INHERIT)

        # remove nodes that have been added to new child node
        taken = MPI.COMM_WORLD.recv(source=childRank, tag=INHERIT)
        for i in taken:
            if i in data:
                data.pop(i)
    
    # continue search to find placement of new node
    else:
        MPI.COMM_WORLD.send(new, dest=childRank, tag=ADD)

    # we made it back through the loop and need to send message to command node
    if myRank == 0:
        MPI.COMM_WORLD.send(0, dest=numProcesses-1, tag=ACK)
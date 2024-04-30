from mpi4py import MPI
import numpy as np

# globals
MAX = 1000
PUT = 0
GET = 1
ADD = 2
REMOVE = 3
END = 4
RETVAL = 5
ACK = 6

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    print(rank)

    # Process 0 will send an array
    if rank == 0:
        # Create an array of integers
        data = np.array([1, 2, 3, 4, 5], dtype='i')
        # Send data to process 1
        comm.Send([data, MPI.INT], dest=1, tag=77)
        print("Process", rank, "sent data:", data)
    
    # Process 1 will receive the array
    elif rank == 1:
        # Prepare a numpy array to receive the data
        data = np.empty(5, dtype='i')  # Ensure the datatype matches the sent data
        # Receive data from process 0
        comm.Recv([data, MPI.INT], source=0, tag=77)
        print("Process", rank, "received data:", data)

if __name__ == '__main__':
    main()

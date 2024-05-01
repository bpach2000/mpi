from mpi4py import MPI
print("Running on rank", MPI.COMM_WORLD.Get_rank(), "of", MPI.COMM_WORLD.Get_size())

# Lattice Models

1. `Vertex` class
    - Represents an individual vertex
    - Attributes:
        - `labels`: an array of labels of the vertex, starting with the "east" vertex and proceeding around clockwise.


2. `Lattice` class
    - Represents a lattice with shape and boundary conditions
    - Attributes:
        - `shape`: the shape of the lattice model; stored as an ordered pair (n,m) where n is the number of rows and m is the number of columns
        - `wts`: Boltzmann weights associated with a particular lattice; stored as a dict of (vertex: weight) pairs.
        - `model`: a 2D array of instances of the `Vertex` class
    - Methods:
        - `calculate_partition`: calculates and outputs the partition function of the lattice



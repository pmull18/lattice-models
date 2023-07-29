# Lattice Models

1. `Vertex` class
    - Represents an individual vertex
    - Attributes:
        - `east`: left edge decoration
        - `north`: top edge decoration
        - `west`: right edge decoration
        - `south`: bottom edge decoration


2. `Lattice` class
    - Represents a lattice with shape and boundary conditions
    - Attributes:
        - `shape`: the shape of the lattice model; stored as an ordered pair (n,m)
        - `top`: the boundary conditions assigned to the top of the lattice model
        - `bottom`: the boundary conditions assigned to the bottom of the lattice model
        - `left`: the boundary conditions assigned to the left side of the lattice model
        - `right`: the boundary conditions assigned to the right side of the lattice model
        - `wts`: Boltzmann weights associated with a particular lattice; stored as a dict of (vertex: weight) pairs.
        - `model`: a numpy array of instances of the `Vertex` class
    - Methods:
        - `calculate_partition`: calculates and outputs the partition function of the lattice
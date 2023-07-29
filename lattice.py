import numpy as np

class Vertex:
    def __init__(self, east, top, west, north):
        self.east = east
        self.top = top
        self.west = west
        self.north = north



class Lattice:
    def __init__(self, shape, boltzmann_wts):
        self.shape = shape
        self.wts = boltzmann_wts


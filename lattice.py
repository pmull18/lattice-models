

class Label:
    def __init__(self, name, type, level):
        self.name = name
        self.type = type
        self.level = level

class Vertex:
    def __init__(self, labels):
        self.labels = labels

empty = Vertex([])

class Lattice:
    def __init__(self, shape, boltzmann_wts):
        self.shape = shape
        self.wts = boltzmann_wts
        self.model = [[empty]*shape[0]]


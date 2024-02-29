class celula:
    def __init__(self, id, v0, v1, v2, vizinhos=None):
        self. id = id
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2
        self.vizinhos = vizinhos
        self.proximo = None
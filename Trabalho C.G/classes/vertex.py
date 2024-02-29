class vertex:
    def __init__(self, id, x, y, celula=None):
        self.id = id
        self.x = x
        self.y = y
        self.celula = celula
        self.proximo = None
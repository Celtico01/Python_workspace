class Vertex:
    def __init__(self, id, x, y, z, face=None):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.face = face
        self.proximo = None

#No do vertex
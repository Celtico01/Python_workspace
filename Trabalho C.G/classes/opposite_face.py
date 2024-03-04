class Estrutura:
    def __init__(self):
        self.primeiroVertex = None
        self.ultimoVertex = None
        self.sizeVertex = 0
        self.primeiroFace = None
        self.ultimoFace = None
        self.sizeFace = 0

    def addVertex(self, noVertex):
        if noVertex is None:
            return
        elif self.sizeVertex == 0:
            self.primeiroVertex = noVertex
            self.ultimoVertex = noVertex
            self.sizeVertex += 1
        else:
            self.ultimoVertex.proximo = noVertex
            self.ultimoVertex = noVertex
            self.sizeVertex += 1

    def addFace(self, noFace):
        if noFace is None:
            return
        elif self.sizeFace == 0:
            self.primeiroFace = noFace
            self.ultimoFace = noFace
            self.sizeFace += 1
        else:
            self.ultimoFace.proximo = noFace
            self.ultimoFace = noFace
            self.sizeFace += 1

    def defineVizinhos(self):
        faces = self.listOfFaces()
        for f1 in faces:
            v0 = f1.v0
            v1 = f1.v1
            v2 = f1.v2
            for f2 in faces:
                if f2 != f1:
                    if (f2.v0 == v0 or f2.v1 == v0 or f2.v2 == v0) and (f2.v0 == v1 or f2.v1 == v1 or f2.v2 == v1):
                        f1.vizinho1 = f2.id
                    elif (f2.v0 == v1 or f2.v1 == v1 or f2.v2 == v1) and (f2.v0 == v2 or f2.v1 == v2 or f2.v2 == v2):
                        f1.vizinho2 = f2.id
                    elif (f2.v0 == v2 or f2.v1 == v2 or f2.v2 == v2) and (f2.v0 == v0 or f2.v1 == v0 or f2.v2 == v0):
                        f1.vizinho3 = f2.id

    def exibirVertex(self):
        if self.sizeVertex == 0:
            return
        aux = self.primeiroVertex
        while aux != None:
            print("id:" + str(aux.id) + " x:" + str(aux.x) + " y:" + str(aux.y) + " z:" + str(aux.z) + " Face:" + str(aux.face))
            aux = aux.proximo

    def exibirFace(self):
        if self.sizeVertex == 0:
            return
        aux = self.primeiroFace
        while aux != None:
            print("id:" + str(aux.id) + " v0:" + str(aux.v0.id) + " v1:" + str(aux.v1.id) + " v2:" + str(aux.v2.id) + " Vizinhos:(" + str(aux.vizinho1) + ", " + str(aux.vizinho2) + ", " + str(aux.vizinho3) + ")")
            aux = aux.proximo

    def listOfVertex(self):
        if self.sizeVertex == 0:
            return []
        aux = self.primeiroVertex
        listVertex = []
        while aux != None:
            listVertex.append(aux)
            aux = aux.proximo
        return listVertex

    def listOfFaces(self):
        if self.sizeFace == 0:
            return []
        aux = self.primeiroFace
        listFace = []
        while aux != None:
            listFace.append(aux)
            aux = aux.proximo
        return listFace
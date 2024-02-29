class estrutura:
    def __init__(self):
        self.primeiroVertex = None
        self.ultimoVertex = None
        self.sizeVertex = 0
        self.vertexAtual = None
        #-------------------
        self.primeiroCelula = None
        self.ultimoCelula = None
        self.sizeCelula = 0
        self.celulaAtual = None

    def addVertex(self, noVertex):
        if noVertex == None:
            return
        elif self.sizeVertex == 0:
            self.primeiroVertex = noVertex
            self.ultimoVertex = noVertex
            self.sizeVertex += 1
        elif self.sizeVertex > 0:
            self.ultimoVertex.proximo = noVertex
            self.ultimoVertex = noVertex
            self.sizeVertex += 1

    def addCelula(self, noCelula):
        if noCelula == None:
            return
        elif self.sizeCelula == 0:
            self.primeiroCelula = noCelula
            self.ultimoCelula = noCelula
            self.sizeCelula += 1
        elif self.sizeCelula > 0:
            self.ultimoCelula.proximo = noCelula
            self.ultimoCelula = noCelula
            self.sizeCelula += 1

    #remove
    
    
    def vHasNext(self):
        if self.vertexAtual is None:
            return self.primeiroVertex is not None
        else:
            return self.vertexAtual.proximo is not None

    def nextVertex(self):
        if self.vertexAtual is None:
            self.vertexAtual = self.primeiroVertex
        else:
            self.vertexAtual = self.vertexAtual.proximo
        return "id:" + str(self.vertexAtual.id) + " x:" + str(self.vertexAtual.x) + " y:" + str(self.vertexAtual.y) + " celula:" + str(self.vertexAtual.celula) if self.vertexAtual else None
    
    def cHasNext(self):
        if self.celulaAtual is None:
            return self.primeiroCelula is not None
        else:
            return self.celulaAtual.proximo is not None
        
    def nextCelula(self):
        if self.celulaAtual is None:
            self.celulaAtual = self.primeiroCelula
        else:
            self.celulaAtual = self.celulaAtual.proximo
        return "id:" + str(self.celulaAtual.id) + " v0:" + str(self.celulaAtual.v0.id) + " v1:" + str(self.celulaAtual.v1.id) + " v2:" + str(self.celulaAtual.v2.id) + " Vizinhos:(" + str(self.celulaAtual.vizinhos[0]) + ", " + str(self.celulaAtual.vizinhos[1]) + ", " + str(self.celulaAtual.vizinhos[2]) + ")" if self.celulaAtual else None
    
    def resetIterator(self):
        self.vertexAtual = None
        self.celulaAtual = None

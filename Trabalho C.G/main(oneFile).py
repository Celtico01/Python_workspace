import numpy as np

#No do vertex
class Vertex:
    def __init__(self, id, x, y, z, face):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.face = face
        self.proximo = None


# No da face
class Face:
    def __init__(self, id, v0, v1, v2, vizinhos1, vizinhos2, vizinhos3):
        self. id = id
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2
        self.vizinho1 = vizinhos1
        self.vizinho2 = vizinhos2
        self.vizinho3 = vizinhos3
        self.proximo = None

#Estrutura
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
        while aux is not None:
            print("id:" + str(aux.id) + " x:" + str(aux.x) + " y:" + str(aux.y) + " z:" + str(aux.z) + " Face:" + str(aux.face))
            aux = aux.proximo

    def exibirFace(self):
        if self.sizeVertex == 0:
            return
        aux = self.primeiroFace
        while aux is not None:
            print("id:" + str(aux.id) + " v0:" + str(aux.v0.id) + " v1:" + str(aux.v1.id) + " v2:" + str(aux.v2.id) + " Vizinhos:(" + str(aux.vizinho1) + ", " + str(aux.vizinho2) + ", " + str(aux.vizinho3) + ")")
            aux = aux.proximo

    def listOfVertex(self):
        if self.sizeVertex == 0:
            return []
        aux = self.primeiroVertex
        listVertex = []
        while aux is not None:
            listVertex.append(aux)
            aux = aux.proximo
        return listVertex

    def listOfFaces(self):
        if self.sizeFace == 0:
            return []
        aux = self.primeiroFace
        listFace = []
        while aux is not None:
            listFace.append(aux)
            aux = aux.proximo
        return listFace


class SRU:
    def __init__(self, x, y, z, estrutura):
        self.x = x  # Define a dimensão x da matriz
        self.y = y  # Define a dimensão y da matriz
        self.z = z  # Define a dimensão z da matriz
        self.estrutura = estrutura  # Armazena a estrutura de dados dos vértices

    def criarMatriz(self):
        # cria uma matriz tridimensional de caracteres preenchida com um caractere padrão '-'
        m = np.empty((self.x, self.y, self.z), dtype=str)
        m[:] = '-'  # preenche a matriz com o caractere padrão
        return m  # retorna a matriz criada
    
    def adicionarVertexs(self, matriz):
        listOfVertex = self.estrutura.listOfVertex()
        if len(listOfVertex) != 0:
            for v in listOfVertex:
                matriz[v.x, v.y, v.z] = '*'
    
    def desenhar(self, matriz, face):
        # obtém as coordenadas x e z de cada vértice da face
        vertices = [(face.v0.x, face.v0.z), (face.v1.x, face.v1.z), (face.v2.x, face.v2.z)]
        #vira uma matriz 2D [vertices][x ou z]

        for v1, v2 in [(vertices[i], vertices[j]) for i in range(len(vertices)) for j in range(i+1, len(vertices))]:
            # desenha uma linha entre cada par de vértices na matriz
            self.criar_linhas(matriz, v1[0], v1[1], v2[0], v2[1])

    def criar_linhas(self, matriz, x0, z0, x1, z1):
        dx = abs(x1 - x0)  # calcula a distância na direção x entre os pontos
        dz = abs(z1 - z0)  # calcula a distância na direção z entre os pontos
        dirX = -1 if x0 > x1 else 1  # determina a direção do incremento de x
        dirZ = -1 if z0 > z1 else 1  # determina a direção do incremento de z
        erro = dx - dz 

        
        while x0 != x1 or z0 != z1:
            matriz[x0, 0, z0] = '*'  
            erro2 = 2 * erro  # calcula o dobro do erro
            if erro2 > -dz:  # vvrifica se o erro é maior que a distância na direção z
                erro -= dz 
                x0 += dirX  # move a coordenada na direção x
            if erro2 < dx:  # verifica se o erro é menor que a distância na direção x
                erro += dx  # atualiza o erro
                z0 += dirZ  # move a coordenada na direção z

    def adicionarFaces(self, matriz):
        listFaces = self.estrutura.listOfFaces()
        for face in listFaces:
            x = (face.v0.x + face.v1.x + face.v2.x) // 3
            y = (face.v0.y + face.v1.y + face.v2.y) // 3
            z = (face.v0.z + face.v1.z + face.v2.z) // 3
            #// é divisão inteira

            matriz[x][y][z] = face.id
        
def main():
    x = 25
    y = 1
    z = 25

    of = Estrutura()
    v0 = Vertex(0, int(x/2), int(y-1), int(z/2), 0)
    of.addVertex(v0) 
    v1 = Vertex(1, int(x * 0.64), int(y - 1), int(z * 0.32), 0)
    of.addVertex(v1) 
    v2 = Vertex(2, int(x * 0.64), int(y - 1), int(z * 0.64), 0)
    of.addVertex(v2) 
    v3 = Vertex(3, int(x/2), int(y - 1), int(z * 0.8), 1)
    of.addVertex(v3) 
    v4 = Vertex(4, int(x * 0.32), int(y - 1), int(z * 0.64), 2) 
    of.addVertex(v4) 
    v5 = Vertex(5, int(x * 0.32), int(y - 1), int(z * 0.32), 3)
    of.addVertex(v5) 
    v6 = Vertex(6, int(x/2), int(y - 1), int(z * 0.16), 4)
    of.addVertex(v6)

    f0 = Face(0, v0, v1, v2, -1, -1, -1)
    of.addFace(f0)
    f1 = Face(1, v0, v2, v3, -1, -1, -1)
    of.addFace(f1)
    f2 = Face(2, v0, v3, v4, -1, -1, -1)
    of.addFace(f2)
    f3 = Face(3, v0, v4, v5, -1, -1, -1)
    of.addFace(f3)
    f4 = Face(4, v0, v5, v6, -1, -1, -1)
    of.addFace(f4)
    f5 = Face(5, v0, v6, v1, -1, -1, -1)
    of.addFace(f5)

    # Define os vizinhos
    of.defineVizinhos()

    espacoSRU = SRU(x, y, z, of)
    matriz = espacoSRU.criarMatriz()
    espacoSRU.adicionarVertexs(matriz)
    espacoSRU.adicionarFaces(matriz)

    #criar faces
    #espacoSRU.desenhar(matriz, f0)
    #espacoSRU.desenhar(matriz, f1)
    #espacoSRU.desenhar(matriz, f2)
    #espacoSRU.desenhar(matriz, f3)
    #espacoSRU.desenhar(matriz, f4)
    #espacoSRU.desenhar(matriz, f5)

    # Exibir
    for i in range(x):
        for j in range(y):
            for k in range(z):
                print(matriz[i, j, k], end=" ")
        print()

    # Dados da estrutura
    print("Dados Pontos:")
    print("Pontos:")
    of.exibirVertex()
    print("Faces:")
    of.exibirFace()

if __name__ == "__main__":
    main()
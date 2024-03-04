import numpy as np

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




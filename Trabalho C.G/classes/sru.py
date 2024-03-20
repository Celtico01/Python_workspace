import numpy as np
from colorama import Fore, Style

class SRU:
    def __init__(self, x, y, z, estrutura):
        self.x = x  
        self.y = y  
        self.z = z  
        self.estrutura = estrutura
        self.matriz = self.criarMatriz()

    def criarMatriz(self):
        # cria uma matriz tridimensional de caracteres preenchida com um caractere padrão '-'
        m = np.empty((self.x, self.y, self.z), dtype=object)
        m[:] = item_matriz(Fore.WHITE, '-')
        for i in range(self.x):
            m[i, 0, self.z // 2] = item_matriz(Fore.RED, '—')
            m[self.x // 2, 0, i] = item_matriz(Fore.RED, '|')
        m[self.x // 2, 0, self.z // 2] = item_matriz(Fore.RED, '+')
        return m  # retorna a matriz criada
    
    def adicionarVertexs(self):
        if len(self.estrutura.listOfVertex()) != 0:
            listOfVertex = self.estrutura.listOfVertex()
            for v in listOfVertex:
                self.matriz[v.x, v.y, v.z] = item_matriz(Fore.GREEN, '*')
    
    def desenharObjeto(self):
        if len(self.estrutura.listOfFaces()) != 0:
            for face in self.estrutura.listOfFaces():
                # obtém as coordenadas x e z de cada vértice da face
                vertices = [(face.v0.x, face.v0.z), (face.v1.x, face.v1.z), (face.v2.x, face.v2.z)]
                #vira uma matriz 2D [vertices][x ou z]

                for v1, v2 in [(vertices[i], vertices[j]) for i in range(len(vertices)) for j in range(i+1, len(vertices))]:
                    # desenha uma linha entre cada par de vértices na matriz
                    self.criar_linhas(v1[0], v1[1], v2[0], v2[1])
        

    def criar_linhas(self, x0, z0, x1, z1): #adaptação do algoritmo de bresenham
        dx = abs(x1 - x0)  # calcula a distância na direção x entre os pontos
        dz = abs(z1 - z0)  # calcula a distância na direção z entre os pontos
        dirX = -1 if x0 > x1 else 1  # determina a direção do incremento de x
        dirZ = -1 if z0 > z1 else 1  # determina a direção do incremento de z
        erro = dx - dz 
        
        while x0 != x1 or z0 != z1:
            self.matriz[x0, 0, z0] = item_matriz(Fore.GREEN, '*') 
            erro2 = 2 * erro  # calcula o dobro do erro
            if erro2 > -dz:  # vvrifica se o erro é maior que a distância na direção z
                erro -= dz 
                x0 += dirX  # move a coordenada na direção x
            if erro2 < dx:  # verifica se o erro é menor que a distância na direção x
                erro += dx  # atualiza o erro
                z0 += dirZ  # move a coordenada na direção z

    def adicionarFaces(self):
        if len(self.estrutura.listOfFaces()) != 0:
            listFaces = self.estrutura.listOfFaces()
            for face in listFaces:
                x = (face.v0.x + face.v1.x + face.v2.x) // 3
                y = (face.v0.y + face.v1.y + face.v2.y) // 3
                z = (face.v0.z + face.v1.z + face.v2.z) // 3
                #// é divisão inteira

                self.matriz[x][y][z] = face.id
class item_matriz:
        def __init__(self, color, char):
            self.color = color
            self.char = char

        def __str__(self):
            return self.color + self.char + Style.RESET_ALL
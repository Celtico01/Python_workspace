from classes.vertex import Vertex
from classes.face import Face
from classes.sru import SRU
from classes.opposite_face import Estrutura

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
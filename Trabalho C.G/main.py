from classes.vertex import Vertex
from classes.face import Face
from classes.sru import SRU
from classes.opposite_face import Estrutura

def main():
    x = 49
    y = 1
    z = 49

    of = Estrutura()
    v0 = Vertex(0, int(x/2), int(y-1), int(z/2))
    of.addVertex(v0) 
    v1 = Vertex(1, int(x * 0.64), int(y - 1), int(z * 0.32))
    of.addVertex(v1) 
    v2 = Vertex(2, int(x * 0.64), int(y - 1), int(z * 0.64))
    of.addVertex(v2) 
    v3 = Vertex(3, int(x/2), int(y - 1), int(z * 0.8))
    of.addVertex(v3) 
    v4 = Vertex(4, int(x * 0.32), int(y - 1), int(z * 0.64)) 
    of.addVertex(v4) 
    v5 = Vertex(5, int(x * 0.32), int(y - 1), int(z * 0.32))
    of.addVertex(v5) 
    v6 = Vertex(6, int(x/2), int(y - 1), int(z * 0.16))
    of.addVertex(v6)

    f0 = Face(0, v0, v1, v2)
    of.addFace(f0)
    f1 = Face(1, v0, v2, v3)
    of.addFace(f1)
    f2 = Face(2, v0, v3, v4)
    of.addFace(f2)
    f3 = Face(3, v0, v4, v5)
    of.addFace(f3)
    f4 = Face(4, v0, v5, v6)
    of.addFace(f4)
    f5 = Face(5, v0, v6, v1)
    of.addFace(f5)

    # Define os vizinhos
    of.defineVizinhos()

    espacoSRU = SRU(x, y, z, of)
    espacoSRU.adicionarVertexs()
    espacoSRU.adicionarFaces()

    #criar faces
    espacoSRU.desenharObjeto()

    # Exibir
    for i in range(x):
        for j in range(y):
            for k in range(z):
                print(espacoSRU.matriz[i, j, k], end=" ")
        print()

    # Dados da estrutura
    print("Dados Pontos:")
    print("Pontos:")
    of.exibirVertex()
    print("Faces:")
    of.exibirFace()

if __name__ == "__main__": #procura e executa o metodo main ao executar
    main()
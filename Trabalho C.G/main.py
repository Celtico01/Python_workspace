from classes import vertex, celula, opposite_face, sru

def main():
    v0 = vertex.vertex(0, 1, 1)
    v1 = vertex.vertex(1, 2, 2)
    v2 = vertex.vertex(2, 3, 3)
    v3 = vertex.vertex(3, 4, 4)

    c0 = celula.celula(0, v0, v1, v2, [-1,-1,-1])
    c1 = celula.celula(1, v0, v1, v3, [-1,-1,-1])
    c2 = celula.celula(2, v3, v1, v2, [-1,-1,-1])

    estrutura = opposite_face.estrutura()

    estrutura.addVertex(v0)
    estrutura.addVertex(v1)
    estrutura.addVertex(v2)
    estrutura.addVertex(v3)

    estrutura.addCelula(c0)
    estrutura.addCelula(c1)
    estrutura.addCelula(c2)

    while estrutura.vHasNext():
        print(estrutura.nextVertex())
    while estrutura.cHasNext():
        print(estrutura.nextCelula())
    
if __name__ == "__main__":
    main()
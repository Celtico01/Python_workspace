from classes.vertex import Vertex
from classes.face import Face
from classes.sru import SRU
from classes.opposite_face import Estrutura
import numpy as np
import os
import math

def inserir_pontos(x,z, qtde_elem, of):
    meio_linha = x // 2
    meio_coluna = z // 2
    id = qtde_elem

    while True:
        try:
            print('[1] Inserir novo ponto.')
            print('[0] Volta para menu.')
            escolha = int(input('Escolha: '))
            os.system('cls')

            if escolha != 0 and escolha != 1:
                raise Exception()
        except:
            print('Escolha inválida.')
        
        if escolha == 1:
            try:
                x = int(input('X:'))
                z = int(input('Z:'))
                if (x > 12 or x < -12) or (z > 12 or z < -12):
                    raise Exception()
                vertex = Vertex(id, meio_linha + x, 0, meio_coluna - z) # parte principal
                of.addVertex(vertex)
                id += 1
                os.system('cls')
            except:
                print('Insira valores válidos. (bound (-12, 12))')
                os.system('cls')
        elif escolha == 0:
            break

def inserir_faces(qtde_elem, of):
    id = qtde_elem
    lim = len(of.listOfVertex())
    vertexs = of.listOfVertex()

    while True:
        for v in vertexs:
            print(f'ID: {v.id}, X: {v.x}, Z:{v.z}')
        try:
            print('[1] Inserir nova face.')
            print('[0] Volta para menu.')
            escolha = int(input('Escolha: '))

            os.system('cls')

            if escolha != 0 and escolha != 1:
                raise Exception()
        except:
            print('Escolha inválida.')

        if escolha == 1:
            try:
                v0 = int(input('Primeiro vertice: '))
                v1 = int(input('Segundo vertice: '))
                v2 = int(input('Terceiro vertice: '))

                if (v0 < 0 or v0 > lim) or (v1 < 0 or v1 > lim) or (v2 < 0 or v2 > lim) or (v0 == v1 or v0 == v2 or v1 == v2):
                    raise Exception()
                
                face = Face(id, vertexs[v0], vertexs[v1], vertexs[v2])
                of.addFace(face)
                id += 1
                os.system('cls')
            except:
                print('ERRO!')
                os.system('cls')
        elif escolha == 0:
            break

def exibir_sru(x, y, z, of, sru):
    for i in range(x):
        for j in range(y):  
            for k in range(z):
                print(sru.matriz[k, j, i], end=' ')
        print()
    
    # Dados da estrutura
    print("Dados Pontos:")
    print("Pontos:")
    of.exibirVertex()
    print("Faces:")
    of.exibirFace()
    input('Pressione ENTER para voltar para o menu!')
    os.system('cls')

def main():
    x = 25
    y = 1
    z = 25

    of = Estrutura()
    
    while True:
        #try:
            escolha = int(input('[1] Inserir pontos.\n[2] Inserir faces.\n[3] Exibir Matriz.\n[4] Translandar.\n[5] Rotacionar.\n[6] Animar rotação.\n[0] Sair.\nEscolha: '))
            os.system('cls')

            if escolha > 6 or escolha < 0:
                raise Exception()

            match escolha:
                case 1: 
                    inserir_pontos(x, z, len(of.listOfVertex()) if len(of.listOfVertex()) != 0 else 0, of)
                case 2:
                    inserir_faces(len(of.listOfFaces()) if len(of.listOfFaces()) != 0 else 0, of)
                    of.defineVizinhos()
                case 3:
                    espaco_sru = SRU(x, y, z, of)
                    espaco_sru.adicionarVertexs()
                    espaco_sru.adicionarFaces()
                    espaco_sru.desenharObjeto()
                    exibir_sru(x, y, z, of, espaco_sru)
                case 4:
                    m_translandar = np.zeros((1,3), dtype=np.float64)
                    while True:
                        try:
                            sx = float(input('Insira o deslocamento em relação a \'x\': '))
                            if sx == 0:
                                raise Exception()
                            
                            sz = float(input('Insira o deslocamento em relação a \'z\': '))
                            if sz == 0:
                                raise Exception()

                            m_translandar[0, 0], m_translandar[0, 1], m_translandar[0, 2] = sz, 0, sx # inverter

                            of.translacao(m_translandar)
                            break
                        except:
                            print('Tente Novamente!')
                            os.system('cls')
                case 5:
                    m_rotacao = np.zeros((3,3), dtype=np.float64)
                    while True:
                        
                        angulo = float(input('Insira o angulo: '))
                            
                        if angulo > 360:
                            angulo_rotacao = math.radians(angulo % 360)
                        else:
                            angulo_rotacao = math.radians(angulo)

                        matriz_rotacao = np.array([
                            [np.cos(angulo_rotacao), 0, -np.sin(angulo_rotacao)],
                            [0, 1, 0],
                            [np.sin(angulo_rotacao), 0,np.cos(angulo_rotacao)]])

                        of.rotacao(matriz_rotacao)
                        break  
                case 6:
                    pass
                case 0:
                    break
        #except:
            print('Escolha Inválida!')

if __name__ == "__main__": #procura e executa o metodo main ao executar
    main()


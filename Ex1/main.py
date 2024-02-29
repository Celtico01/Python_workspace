#1.  ler os limites mínimo (MIN) e máximo (MAX) de um sistema do usuário (SRU) nos eixos X e Y;
#2.  definir uma matriz quadrada com dimensão MAX para simular o seu SRU; 
#3.  ler coordenadas X e Y de pontos no SRU (leia quantos pontos você quiser, pelo menos dois);
#4.  atribuir os pontos lidos na matriz de acordo com as coordenadas dos pontos;
#5.  exibir a matriz destacando os pontos lidos (escolha um caractere para representar os pontos e outro para #representar o espaço vazio);
#6.  calcular e exibir as coordenadas normalizadas dos pontos lidos (nomeie os pontos); 
#7.  ler as dimensões máximas de um dispositivo qualquer;
#8.  apresentar as coordenadas dos pontos lidos no dispositivo definido (SRD).

import numpy as np

class pontoSRU:
    def __init__(self, nome, largura, altura, larguraMin, larguraMax, alturaMin, alturaMax):
        self.nome = nome
        self.largura = largura
        self.altura = altura
        self.larguraMin = larguraMin
        self.larguraMax = larguraMax
        self.alturaMin = alturaMin
        self.alturaMax = alturaMax
    
    def pontoNormalizado(self):
        return ndcx(x=self.largura, xMin=self.larguraMin, xMax=self.larguraMax), ndcy(y=self.altura, yMin=self.alturaMin, yMax=self.alturaMax)

    #passo 8
    def transforma_P_SRD(self, xminD, xmaxD, yminD, ymaxD):
        xN, yN = self.pontoNormalizado()
        xD = xminD + xN * (xmaxD - xminD)
        yD = yminD + yN * (ymaxD - yminD)

        return xD, yD


#passo 1
while True:
    try:
        lim_min, lim_max = int(input("Limite minimo: ")), int(input("limite maximo: "))
        if(lim_min < 0) or (lim_max < lim_min):
            raise ValueError
        else:
            break
    except:
        print("Corrija os inputs!")

sruSize = lim_max - lim_min + 1

#passo 2
SRU = np.zeros((sruSize, sruSize), dtype=np.int8)

print(SRU) #remover depois

#passo 3
opcao = 0
qtdeCoordenadas = 0

while True:
    print("[1] -> Adicionar nova coordenada.")
    print("[2] -> Encerrar.")
    try:
        opcao = int(input("Opção: "))
        if opcao == 1 and qtdeCoordenadas <= SRU.size:
            x = int(input("Insira a coordenada X: "))
            y = int(input("Insira a coordenada Y: "))
            if (x < lim_min or x > lim_max) or (y < lim_min or y > lim_max):
                raise ValueError
            #passo4
            if lim_min == 0:
                SRU[x][y] = 1
            else:
                SRU[x - lim_min][y - lim_min] = 1

            qtdeCoordenadas += 1
        elif opcao == 2 and qtdeCoordenadas >= 2:
            break
        else:
            raise ValueError
    except:
        print("Erro!")

#passo 5
print(SRU)

def ndcx(x, xMin, xMax):
    return (x - xMin) / (xMax - xMin)

def ndcy(y, yMin, yMax):
    return (y - yMin) / ( yMax - yMin)

pontos = []
contador = 1

#passo 6
for i in range(sruSize):
    for j in range(sruSize):
        if SRU[i][j] == 1:
            pontos.append(pontoSRU("P" + str(contador), i, j, lim_min, lim_max, lim_min, lim_max))
            contador += 1

for i in range(len(pontos)):
    print(pontos[i].nome + " = " + str(pontos[i].pontoNormalizado()))

#passo 7
try:
    xMinSRD, xMaxSRD, yMinSRD, yMaxSRD = 0, int(input("Coordenada x SRD: ")), 0, int(input("Coordenada y SRD: "))

    if xMaxSRD <= xMinSRD or yMaxSRD <= yMinSRD:
        raise ValueError
except:
    print("ERRO!")
    quit()

#passo 8
for ponto in pontos:
    xD, yD = ponto.transforma_P_SRD(xMinSRD, xMaxSRD, yMinSRD, yMaxSRD)
    print("No SRD: " + ponto.nome + ": (" + str(xD) + ", " + str(yD) + ")")




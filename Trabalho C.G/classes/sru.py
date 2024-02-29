import numpy as np

class sru:
    def __init__(self, x, y, estrutura):
        self.x = x
        self.y = y
        self.estrutura = estrutura

    def criarMatriz(self):
        return np.zeros((self.x, self.y), dtype=np.int8)
    
    #todo
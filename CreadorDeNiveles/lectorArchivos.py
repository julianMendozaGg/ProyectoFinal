class LectorArchivo():

    def __init__(self):
        self.data=[]
        self.matriz=[]
        self.filas = 9
        self.columnas = 9

    def leerNivel(self, path):
        f = open(path, 'r')
        for line in f.readlines():
            self.data.append(line.replace('\n', '').split(' '))
        f.close()

        return self.data

    def devolverMatriz(self,path):
        self.leerNivel(path)

        for i in range(self.filas):
            self.matriz.append([0]*self.columnas)

        for i in range(len(self.data)-1):
            for j in range(len(self.data[0])-1):
                self.matriz.append(int(self.data[i][j]))

        return self.matriz





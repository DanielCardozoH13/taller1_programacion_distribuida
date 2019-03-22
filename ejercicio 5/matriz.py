import random
from sys import *
from threading import *

class Matriz(object):
    def __init__(self, filas=None, columnas=None):

        if filas:
            self.filas =filas
        else:
            try:
                self.filas = int(input(" Ingrese número de filas"))
            except ValueError:
                print("ATENCIÓN: Debe ingresar un número entero.")
                exit()

        if columnas:
            self.columnas = columnas
        else:
            try:
                self.columnas = int(input(" Ingrese número de columnas"))
            except ValueError:
                print("ATENCIÓN: Debe ingresar un número entero.")
                exit()



    def Crear_m(self):
      self.matriz=[]
      for f in range(self.filas):
          self.matriz.append([0]*self.columnas)

    def Llenar_m(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                hilo_llenar_auto = Thread(target=self.llenar_con_hilos, args=(f, c, 2, ))
                hilo_llenar_auto.start()
                hilo_llenar_auto.join()

    def Llenar_manual(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                hilo_llenar_manual = Thread(target=self.llenar_con_hilos, args=(f, c, 1, ))
                hilo_llenar_manual.start()
                hilo_llenar_manual.join()

    def llenar_con_hilos(self, fila, colum, tipo):
        if tipo == 1:#si tipo = 1, llenado manual, de lo contrario con random
            self.matriz[fila][colum] = int(input("Ingrese pos (%d,%d): " % (fila, colum)))
        else:
            self.matriz[fila][colum] = random.randint(-10, 10)


    def Print_m(self):
        #print(self.matriz)
        for row in self.matriz:
            print(row)

    def datam(self):
        return self.matriz

    def valida_m(self,colA,filB):
        if colA != filB:
            return True
        else:
            return False

    
    def multi_m(self,matrizA,matrizB,filaB):
        for f in range(self.filas):
            for c in range(self.columnas):
                for k in range(filaB):
                    hilos_multi_m = Thread(target=self.hilos_multi_m, args=(f, c, k, ))

    def hilos_multi_m(self, fila, column, fil_b):
        self.matriz[fila][column]+=matrizA[fila][fil_b]*matrizB[fil_b][column]

    
    def multireal(self,nreal):
        for f in range(self.filas):
            hilo_filas = Thread (target=self.multireal_fila, args=(nreal, f, ))
            hilo_filas.start()

    def multireal_fila(self,nreal, fila):
        for c in range(self.columnas):
                self.matriz[fila][c] = self.matriz[fila][c] * nreal


    def valida_sumres(self,filA, colA, filB,colB):
        if (colA != colB) or (filA != filB):
            return True
        else:
            return False

    
    def sum_m(self,matrizA,matrizB):
        for f in range(self.filas):
            for c in range(self.columnas):
                hilo_sum = Thread(target=self.sum_rest_hilos, args=(f, c, 1,matrizA,matrizB, ))
                hilo_sum.start()
            hilo_sum.join()
                

    def rest_m(self,matrizA,matrizB):
        for f in range(self.filas):
            for c in range(self.columnas):
                hilo_res = Thread(target=self.sum_rest_hilos, args=(f, c, 2,matrizA,matrizB, ))
                hilo_res.start()
            hilo_res.join()	

    def sum_rest_hilos(self, fila, colum, tipo, matrizA, matrizB):
        if tipo == 1:
            self.matriz[fila][colum] = matrizA[fila][colum] + matrizB[fila][colum]
        else:
            self.matriz[fila][colum] = matrizA[fila][colum] - matrizB[fila][colum]

    def copy(self,m):
        self.result = []
        for f in m:
            self.result.append(f[:])
        return self.result

    def combinacion(self,m, i, j, e):
        n = len(m)
        for c in range(n):
            m[j][c] = m[j][c] + e * m[i][c]

    def intercambiaFilas(self,m, i, j):
        m[i], m[j] = m[j], m[i]

    def multiplicaFila(self,m, f, e):
        n = len(m)
        for c in range(n):
            m[f][c] = m[f][c] * e

    def primeroNoNulo(self,m, i):
        result = i
        while result < len(m) and m[result][i] == 0:
            result = result + 1
        return result

    def determinante(self,matr):
        m = self.copy(matr)
        n = len(m)
        det = 1
        for i in range(n):
            j = self.primeroNoNulo(m, i)
            if j == n:
                return 0
            if i != j:
                det = -1 * det
                self.intercambiaFilas(m, i, j)
            det = det * m[i][i]
            self.multiplicaFila(m, i, 1. / m[i][i])
            for k in range(i + 1, n):
                self.combinacion(m, i, k, -m[k][i])
        print(int(det))

    def cuadrada(self):
        if self.filas == self.columnas:
            return True
        else:
            return False

    def traspuesta(self,mA):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = mA[c][f]

    def simetrica(self):
        band = True
        for f in range(self.filas):
            for c in range(self.columnas):
                if (self.matriz[f][c] != self.matriz[c][f]):
                    band = False
                    break
        if (band):
            print("Matriz Simetrica")
        else:
            print("Matriz no es Simetrica")

    def identidad(self):
        for f in range(self.filas):
            hilo_identidad = Thread(target=self.ident_hilos, args=(f, ))
            hilo_identidad.start()
        hilo_identidad.join()

    def ident_hilos(self, fila):
        self.matriz[fila][fila] = 1

    def multiply(self,matriz1, matriz2,fila):
        res = []
        for f in range(fila):
            res.append([0] * fila)

        for i, row in enumerate(res):
            for j in range(0, len(row)):
                for k in range(0, len(row)):
                    res[i][j] += matriz1[i][k] * matriz2[k][j]
        return res

    def getPow(self, pow):
        powerhash = {}
        if pow in powerhash.keys():
           return powerhash[pow]
        if pow == 1:
            return self.matriz
        if pow == 2:
            powerhash[pow] = self.multiply(self.matriz, self.matriz,self.filas)
            return powerhash[pow]
        if pow % 2 == 0:
            powerhash[pow] = self.multiply(self.getPow(pow / 2), self.getPow(pow / 2),self.filas)
        else:
            powerhash[pow / 2 + 1] = self.multiply(self.getPow(pow / 2), self.matriz,self.filas)
            powerhash[pow] = self.multiply(self.getPow(pow / 2), powerhash[pow / 2 + 1],self.filas)
        return powerhash[pow]

    def transposeMatrix(self,m):
        t = []
        for r in range(len(m)):
            tRow = []
            for c in range(len(m[r])):
                if c == r:
                    tRow.append(m[r][c])
                else:
                    tRow.append(m[c][r])
            t.append(tRow)
        return t

    def getMatrixMinor(self,m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def getMatrixDeternminant(self,m):
        # base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        determinant = 0
        for c in range(len(m)):            
            determinant += ((-1) ** c) * m[0][c] * self.getMatrixDeternminant(self.getMatrixMinor(m, 0, c))
        return determinant

    def getMatrixInverse(self,m):
        determinant = float(self.getMatrixDeternminant(m))
        # special case for 2x2 matrix:
        if (determinant != 0):
            if len(m) == 2:
                return [[round(float(m[1][1] / determinant),2), round(float(-1 * m[0][1] / determinant),2)],
                        [round(float(-1 * m[1][0] / determinant),2), round(float(m[0][0] / determinant),2)]]

            # find matrix of cofactors
            cofactors = []
            for r in range(len(m)):
                cofactorRow = []
                for c in range(len(m)):
                    minor = self.getMatrixMinor(m, r, c)
                    cofactorRow.append(((-1) ** (r + c)) * float(self.getMatrixDeternminant(minor)))
                cofactors.append(cofactorRow)
            cofactors = self.transposeMatrix(cofactors)
            for r in range(len(cofactors)):
                for c in range(len(cofactors)):
                    cofactors[r][c] = round(float(cofactors[r][c] / determinant),2)
            return cofactors
        else:
            print("no se puede")
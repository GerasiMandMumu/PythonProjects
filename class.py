#Находит сопряженное комплексное число
class Complex():
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im
    def Conjugate(self):
        if self.Im < 0:
            print(self.Re + self.Im*(-1),'i')
        else:
            print(self.Re, '-', self.Im, 'i')
        
a = Complex(1,2)

  
#Матрица
class Matrix():
    def __init__(self, Matrix):
        self.Matrix = Matrix
        
    def WriteLine(self):
        for i in range(0, len(self.Matrix)):
            for j in range(0, len(self.Matrix)):
                print(self.Matrix[i][j], end =' ')
            print()
            
    def __add__(self, Matr):
        for i in range(0, len(self.Matrix)):
            for j in range(0, len(self.Matrix)):
                self.Matrix[i][j] = Matr.Matrix[i][j] + self.Matrix[i][j]
                
    '''def __mul__(self, Matr, Mult):
        for i in range(0, len(self.Matrix)):
            for j in range(0, len(self.Matrix)):
               k = 0;
               for k in range(0, len(self.Matrix)):
                   k += self.Matrix[i][k] * Matr.Matrix[k][j]
               Mult.Matrix[i][j] = k'''
                
m = [[1,2],[3,4]]
n = [[5,6],[7,8]]

b = Matrix(m)
c = Matrix(n)


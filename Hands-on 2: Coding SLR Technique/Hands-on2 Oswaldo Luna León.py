from math import sqrt
# Year  Sales(Y)  Advertising(X)
# 1     651         23
# 2     762         26
# 3     856         30
# 4     1063        34
# 5     1190        43
# 6     1298        48
# 7     1421        52
# 8     1440        57
# 9     1518        58
#[]
class dataSet():
    def __init__(self):
        self.X = [23,26,30,34,43,48,52,57,58]
        self.Y = [651, 762, 856, 1063, 1190, 1298, 1421, 1440,1518]
        self.N = 9
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def getN(self):
        return self.N

class maths():
    def __init__(self):
        self.total = 0
    def sumX(self,X):
        return sum(X)
    def sumY(self,Y):
        return sum(Y)
    def sum_x2(self,X):
        self.total = 0
        for i in range(9):
            self.total += X[i]**2
        return round(self.total,2)
    def sumXY(self,X,Y):
        self.total = 0
        for i in range(9):
            self.total += X[i] * Y[i]
        return round(self.total,2)

class linearRegression():
    def __init__(self,dataSet,maths):
        self.__beta1 = 0
        self.__beta0 = 0
        self.data = dataSet
        self.maths = maths
    def calculateB1(self):
        sumXY = self.maths.sumXY(self.data.getX(),self.data.getY())
        sumX = self.maths.sumX(self.data.getX())
        sumY = self.maths.sumY(self.data.getY())
        sum_x2 = self.maths.sum_x2(self.data.getX())
        self.__beta1 = round((self.data.getN() * sumXY - sumX * sumY) / (self.data.getN() * sum_x2 - sumX * sumX),2)
    def getB1(self):
        return self.__beta1
    def calculateB0(self):
        self.__beta0 = round((self.maths.sumY(self.data.getY()) - self.__beta1 * self.maths.sumX(self.data.getX())) / self.data.getN(),2)
    def getB0(self):
        return self.__beta0
    def equation(self):
        self.calculateB1()
        self.calculateB0()
        print("Ecuación de Regresión:","Y =", self.getB0(),"+",self.getB1(),"x")
    def prediccion(self,X):
        #print("Y =", self.getB0(), "+", self.getB1(), "(",X,")")
        Y = round(self.getB0() + (self.getB1() * X),2)
        return Y
    def coefficientDetermination(self):
        RES = 0
        TOT = 0
        yHat = []
        mediaY = round(self.maths.sumY(self.data.getY()) / self.data.getN())
        for i in range(self.data.getN()):
            yHat.append(self.prediccion(self.data.X[i]))
            RES += round((self.data.Y[i] - yHat[i])**2,2)
            TOT += round((self.data.Y[i] - mediaY)**2,2)
        return 1 - RES /TOT
    def coefficientCorrelation(self):
        return sqrt(self.coefficientDetermination())

if __name__ == "__main__":
    data = dataSet()
    math = maths()
    LR = linearRegression(data,math)
    LR.equation()
    print("Coeficiente de Determinacion:", LR.coefficientDetermination())
    print("Coeficiente de Correlacion", LR.coefficientCorrelation())

    print("Prediccion x=60:","Y = ",LR.getB0(),"+",LR.getB1(),"(60)")
    print("Y = ",LR.prediccion(60))
    print("Prediccion x=65:", "Y = ", LR.getB0(), "+", LR.getB1(), "(65)")
    print("Y = ", LR.prediccion(65))
    print("Prediccion x=70:", "Y = ", LR.getB0(), "+", LR.getB1(), "(70)")
    print("Y = ", LR.prediccion(70))
    print("Prediccion x=75:", "Y = ", LR.getB0(), "+", LR.getB1(), "(75)")
    print("Y = ", LR.prediccion(75))
    print("Prediccion x=80:", "Y = ", LR.getB0(), "+", LR.getB1(), "(80)")
    print("Y = ", LR.prediccion(80))

from numpy import *
class Dataset: #26
    def __init__(self):
        self.x = [108, 115, 106, 97, 95, 91, 97, 83, 83, 78, 54, 67, 56, 53, 61, 115, 81, 78, 30, 45, 99, 32, 25, 28, 90, 89]
        self.y = [95, 96, 95, 97, 93, 94, 95, 93, 92, 86, 73, 80, 65, 69, 77, 96, 87, 89, 60, 63, 95, 61, 55, 56, 94, 93]
    def getX(self):
        return self.x
    def getY(self):
        return self.y

class PolynomialRegression:
    def __init__(self, data, degree):
        self.data = data
        self.X = array(data.getX()).reshape(-1, 1)
        self.Y = array(data.getY()).reshape(-1, 1)
        self.degree = degree
        self.beta = []
    def calculateBetas(self):
        X_poly = ones_like(self.X)
        for i in range(1, self.degree + 1):
            X_poly = concatenate((X_poly, power(self.X, i)), axis=1)
        Q, R = linalg.qr(X_poly)
        self.beta = linalg.solve(R, dot(Q.T, self.Y))
    def equation(self,X):
        equation = "Y = "
        for i in range(self.degree + 1):
            if(i==0):
                equation += f"{self.beta[i]}"
            else:
                equation += f" + {self.beta[i]} {X}^{i}"
        return equation
    def predict(self, x):
        y = 0
        for i in range(self.degree + 1):
            if (i == 0):
                y += (self.beta[i])
            else:
                y += (self.beta[i] * (x ** i))
        return y
    def coefficientDetermination(self):
        RES = 0
        TOT = 0
        mediaY = mean(self.data.getY())
        for i in range(26):
            yHat = self.predict(self.data.x[i])
            RES += (self.data.y[i] - yHat) ** 2
            TOT += (self.data.y[i] - mediaY) ** 2
        return 1 - (RES / TOT)
    def coefficientCorrelation(self):
        return sqrt(self.coefficientDetermination())

if __name__ == "__main__":

    data = Dataset()
    linear = PolynomialRegression(data, degree=1)
    quadratic = PolynomialRegression(data, degree=2)
    cubic = PolynomialRegression(data, degree=3)

    cubic.calculateBetas()
    quadratic.calculateBetas()
    linear.calculateBetas()

    print("Ecuación de Regresión Polinomial lineal:",linear.equation("X"))
    print("Ecuación de Regresión Polinomial cuadratica:",quadratic.equation("X"))
    print("Ecuación de Regresión Polinomial cubica:",cubic.equation("X"))

    print("\n--Predicciones--")
    print("Prediccion lineal X=60 :", linear.equation(60))
    print("Y = ", linear.predict(60))
    print("Prediccion cuadratica X=60 :", quadratic.equation(60))
    print("Y = ", quadratic.predict(60))
    print("Prediccion cubica X=60 :", cubic.equation(60))
    print("Y = ", cubic.predict(60))

    print("\nPrediccion lineal X=102 :", linear.equation(102))
    print("Y = ", linear.predict(102))
    print("Prediccion cuadratica X=102 :", quadratic.equation(102))
    print("Y = ", quadratic.predict(102))
    print("Prediccion cubica X=102 :", cubic.equation(102))
    print("Y = ", cubic.predict(102))

    print("\nPrediccion lineal X=117 :", linear.equation(117))
    print("Y = ", linear.predict(117))
    print("Prediccion cuadratica X=117 :", quadratic.equation(117))
    print("Y = ", quadratic.predict(117))
    print("Prediccion cubica X=117 :", cubic.equation(117))
    print("Y = ", cubic.predict(117))

    print("\nCoeficiente de determinacion lineal:",linear.coefficientDetermination())
    print("Coeficiente de correlacion lineal:",linear.coefficientCorrelation())

    print("\nCoeficiente de determinacion cuadratica:", cubic.coefficientDetermination())
    print("Coeficiente de correlacion cuadratica:", cubic.coefficientCorrelation())

    print("\nCoeficiente de determinacion cubica:", quadratic.coefficientDetermination())
    print("Coeficiente de correlacion cubica:", quadratic.coefficientCorrelation())








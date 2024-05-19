import math
"""
Altura en centímetros) Peso(en kg) Talla de camiseta
            158	            58	        MEDIUM
            158	            59	        MEDIUM
            158	            63	        MEDIUM
            160	            59	        MEDIUM
            160	            60	        MEDIUM
            163	            60	        MEDIUM
            163	            61	        MEDIUM
            160	            64          LARGE
            163	            64	        LARGE
            165	            61	        LARGE
            165	            62	        LARGE
            165	            65          LARGE
            168	            62          LARGE
            168	            63	        LARGE
            168	            66	        LARGE
            170	            63          LARGE
            170	            64	        LARGE
            170	            68	        LARGE
"""

class dataSet:
    def __init__(self):
        self.X = [158,158,158,160,160,163,163,160,163,165,165,165,168,168,168,170,170,170]
        self.Y = [58,59,63,59,60,60,61,64,64,61,62,65,62,63,66,63,64,68]
        self.label = ['MEDIUM','MEDIUM','MEDIUM','MEDIUM','MEDIUM','MEDIUM','MEDIUM','LARGE','LARGE','LARGE','LARGE','LARGE','LARGE','LARGE','LARGE','LARGE','LARGE','LARGE']
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def getLabel(self):
        return self.label

class knn:
    def __init__(self,k,X,Y,label):
        self.k = k
        self.x = X
        self.y = Y
        self.label = label
    def euclidean(self,x1,y1,x2,y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    def predict(self,x,y):
        distances = []
        for i in range(len(self.x)):
            dist = round(self.euclidean(x,y,self.x[i],self.y[i]),2)
            distances.append((dist, self.label[i]))
        distances.sort()

        print("\nVecinos mas cercanos para Altura:",x,"Peso:",y)
        for distance in distances:
            print(distance)

        votes = {}
        for i in range(self.k):
            if distances[i][1] not in votes:
                votes[distances[i][1]] = 0
            votes[distances[i][1]] += 1
        sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
        print("\nLa predicción para altura",x,",peso",y,"con K=",self.k,"es: ",sorted_votes[0][0])


data = dataSet()
KNN = knn(5,data.getX(),data.getY(),data.getLabel())
KNN.predict(160,58)
KNN.predict(162,60)
KNN.predict(164,65)
KNN.predict(163,70)

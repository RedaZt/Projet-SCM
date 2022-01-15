import copy

class NorthWest:
    def __init__(self, couts, stocks, demandes):
        self.couts = couts
        self.stocks = stocks
        self.demandes = demandes
        self.iterations, self.resultat = self.northWest()
        self.coutFinal = self.calculateCost()

    def isValidTable(self):
        return sum(self.stocks) == sum(self.demandes)

    def northWest(self):
        resultat = []
        iterations = []
        
        for i in range(len(self.couts)):
            resultat.append([0]*len(self.couts[i]))

        for i in range(len(self.stocks)):
            for j in range(len(self.demandes)):
                if self.stocks[i] >= self.demandes[j] :
                    resultat[i][j] = self.demandes[j]
                    self.stocks[i] -= self.demandes[j]
                    self.demandes[j] = 0
                else:
                    resultat[i][j] = self.stocks[i]
                    self.demandes[j] -= self.stocks[i]
                    self.stocks[i] = 0
            iterations.append(copy.deepcopy(resultat))

        return iterations, resultat
        
    def calculateCost(self):
        coutFinal = 0

        for i in range(len(self.resultat)):
            for j in range(len(self.resultat[i])):
                coutFinal+= self.couts[i][j] * self.resultat[i][j]
        return coutFinal
        
# couts = [[11,13,17,14],[16,18,14,10],[21,24,13,10]]
# stocks = [250,300,400]
# demandes = [200,225,275,250] 
# couts = [
#     [5,2,4,3],
#     [4,8,1,6],
#     [4,6,7,5]
# ]
# stocks = [22,15,8]
# demandes = [7,12,17,9]

# Exemple = NorthWest(couts, stocks, demandes)

# print("La solution de base est :")
# for ligne in Exemple.resultat:
#     print(ligne)

# print("Cout Final =",Exemple.coutFinal)
# print(Exemple.iterations)

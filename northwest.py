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


class NorthWest:
    def __init__(self, couts, stocks, demandes):
        self.couts = couts
        self.stocks = stocks
        self.demandes = demandes
        self.resultat = self.northWest()
        self.coutFinal = self.calculateCost()

    def isValidTable(self):
        return sum(self.stocks) == sum(self.demandes)

    def northWest(self):
        resultat = []
        for i in range(len(self.stocks)):
            f = []
            for j in range(len(self.demandes)):
                if self.stocks[i] >= self.demandes[j] :
                    f.append(self.demandes[j])
                    self.stocks[i] -= self.demandes[j]
                    self.demandes[j] = 0
                else:
                    f.append(self.stocks[i])
                    self.demandes[j] -= self.stocks[i]
                    self.stocks[i] = 0
            resultat.append(f)
        
        return resultat
        
    def calculateCost(self):
        coutTotal = 0

        for i in range(len(self.resultat)):
            for j in range(len(self.resultat[i])):
                coutTotal+= self.couts[i][j] * self.resultat[i][j]
        return coutTotal

# Exemple = NorthWest(couts, stocks, demandes)

# print("La solution de base est :")
# for ligne in Exemple.resultat:
#     print(ligne)

# print("Cout Final =",Exemple.coutFinal)

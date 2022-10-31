import copy

class NorthWestCorner:
    def __init__(self, couts, stocks, demandes):
        self.couts = couts
        self.stocks = stocks
        self.demandes = demandes
        self.iterations, self.resultat = self.northWest()
        self.coutFinal = self.calculateCost()

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

#TODO : Find a better method to choosing the minimal cost

import copy

class CoutMinimal:
    def __init__(self, couts, stocks, demandes):
        self.couts = couts
        self.stocks = stocks
        self.demandes = demandes
        self.iterations, self.resultat = self.coutMinimal()
        self.coutFinal = self.calculateCost()

    def isValidTable(self):
        return sum(self.stocks) == sum(self.demandes)

    def coutMinimal(self):
        iterations = []
        resultat = []

        for i in range(len(self.couts)):
            resultat.append([0]*len(self.couts[i]))

        d = []
        for x in self.couts: d+=x

        while any(x != 0 for x in self.stocks):
            index = d.index(min(d))
            if d.count(min(d)) > 1 :
                for i in range(len(d)):
                    if d[i] == min(d) and self.demandes[i % len(self.demandes)] > self.demandes[index % len(self.demandes)] : index = i

            indexLigne = index // len(self.demandes)
            indexColonne = index % len(self.demandes)
            
            if self.stocks[indexLigne] >= self.demandes[indexColonne] :
                resultat[indexLigne][indexColonne] = self.demandes[indexColonne]
                self.stocks[indexLigne] -= self.demandes[indexColonne]
                self.demandes[indexColonne] = 0
            else:
                resultat[indexLigne][indexColonne] = self.stocks[indexLigne]
                self.demandes[indexColonne] -= self.stocks[indexLigne]
                self.stocks[indexLigne] = 0
                
            if iterations != [] :
                if iterations[-1] != resultat : iterations.append(copy.deepcopy(resultat))
            else : iterations.append(copy.deepcopy(resultat))
            d[index] = max(d)+1

        return iterations, resultat

    def calculateCost(self):
        coutFinal = 0
        for i in range(len(self.couts)):
            for j in range(len(self.couts[i])):
                coutFinal += self.couts[i][j] * self.resultat[i][j]
        return coutFinal
        
# couts = [[5,4,11,5,11,8],[7,2,18,11,4,5],[10,7,11,17,8,12],[11,7,15,15,11,16]]
# stocks = [120,300,410,250]
# demandes = [100,210,200,250,200,120] 

# exemple = CoutMinimal(couts, stocks, demandes)
# print(exemple.resultat)
# print(exemple.iterations)
# print(exemple.coutFinal)
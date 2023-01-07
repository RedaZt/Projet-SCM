import copy

class LeastCost:
    def __init__(self, couts, stocks, demandes):
        self.couts = couts
        self.stocks = stocks
        self.demandes = demandes
        self.iterations, self.resultat = self.coutMinimal()
        self.coutFinal = self.calculateCost()

    def coutMinimal(self):
        iterations = []
        resultat = []

        for i in range(len(self.couts)):
            resultat.append([0] * len(self.couts[i]))

        d = sum(self.couts,[])

        while any(x != 0 for x in self.stocks):
            index = d.index(min(d))
            if d.count(min(d)) > 1:
                for i in range(len(d)):
                    if d[i] == min(d) and self.demandes[i % len(self.demandes)] > self.demandes[index % len(self.demandes)]: 
                        index = i

            indexL = index // len(self.demandes)
            indexC = index % len(self.demandes)
            
            if self.stocks[indexL] >= self.demandes[indexC]:
                resultat[indexL][indexC] = self.demandes[indexC]
                self.stocks[indexL] -= self.demandes[indexC]
                self.demandes[indexC] = 0
            else:
                resultat[indexL][indexC] = self.stocks[indexL]
                self.demandes[indexC] -= self.stocks[indexL]
                self.stocks[indexL] = 0
                
            if iterations != []:
                if iterations[-1] != resultat: 
                    iterations.append(copy.deepcopy(resultat))
            else: 
                iterations.append(copy.deepcopy(resultat))
            d[index] = max(d) + 1

        return iterations, resultat

    def calculateCost(self):
        coutFinal = 0
        for i in range(len(self.couts)):
            for j in range(len(self.couts[i])):
                coutFinal += self.couts[i][j] * self.resultat[i][j]
        return coutFinal
#TODO : Fix the when there is two max values in "regret"s list

import copy

class RegretMax:
    def __init__(self, couts, stocks, demandes):
        self.couts = couts
        self.stocks = stocks
        self.demandes = demandes
        self.iterations, self.resultat = self.regretMax()
        self.coutFinal = self.calculateCost()

    def isValidTable(self):
        return sum(self.stocks) == sum(self.demandes)
    
    def regretMax(self):
        iterations = []
        resultat = []
        for i in range(len(self.couts)):
            resultat.append([0]*len(self.couts[i]))

        while any(x != 0 for x in self.stocks):
            regretsL=[]
            regretsC=[]
            for i in range(len(self.couts[0])):
                if self.demandes[i] != 0 :
                    d=[]
                    for j in range(len(self.couts)) : 
                        if self.stocks[j] !=0 : d.append(self.couts[j][i])
                        else : d.append(9**50)
                    d.sort()
                    regretsC.append(d[1]-d[0])
                else : regretsC.append(0)

            for i in range(len(self.couts)):
                if self.stocks[i] != 0 :
                    d=[]
                    for j in range(len(self.couts[i])):
                        if self.demandes[j] != 0 : d.append(self.couts[i][j])
                        else : d.append(9**50)
                    d.sort()
                    regretsL.append(d[1]-d[0])
                else : regretsL.append(0)
            
            
            if max(regretsC) > max(regretsL) :
                indexC = regretsC.index(max(regretsC))
                indexL = regretsL.index(max(regretsL))
                for i in range(len(self.couts)):
                    if self.couts[i][indexC] < self.couts[indexL][indexC] and self.stocks[i] != 0 : 
                        indexL = i

                if regretsC.count(max(regretsC)) > 1 :
                    for i in range(len(regretsC)) :
                        if regretsC[i] == max(regretsC) :
                            for j in range(len(self.couts)) :
                                if self.couts[j][i] < self.couts[indexL][indexC] and self.stocks[j] != 0 :
                                    indexC = i
                                    indexL = j

            elif max(regretsC) == max(regretsL) :
                indexL = regretsL.index(max(regretsL))
                indexC = regretsC.index(max(regretsC))
                f = indexL
                
                minCoutL = self.couts[indexL][indexC]
                minCoutC = self.couts[indexL][indexC]

                for j in range(len(self.couts[indexL])):
                    if self.couts[indexL][j] < minCoutL and self.demandes[j] != 0 : 
                        minCoutL = self.couts[indexL][j]

                for i in range(len(self.couts)):
                    if self.couts[i][indexC] < minCoutC and self.stocks[i] != 0 : 
                        minCoutC = self.couts[i][indexC]
                        f = i
                
                if minCoutL < minCoutC :
                    indexC = self.couts[indexL].index(minCoutL)
                
                if minCoutL > minCoutC :
                    indexL = f
            
            elif max(regretsC) < max(regretsL) :
                indexL = regretsL.index(max(regretsL))
                indexC = regretsC.index(max(regretsC))

                for j in range(len(self.couts[indexL])):
                    if self.couts[indexL][j] < self.couts[indexL][indexC] and self.demandes[j] != 0 :
                        indexC = j

                if regretsL.count(max(regretsL)) > 1 :
                    for i in range(len(regretsL)) :
                        if regretsL[i] == max(regretsL) :
                            if min(self.couts[i]) < self.couts[indexL][indexC] and self.stocks[regretsL.index(min(self.couts[i]))] != 0 :
                                indexL = i
                                indexC = regretsL.index(min(self.couts[i]))

            if self.stocks[indexL] >= self.demandes[indexC] :
                resultat[indexL][indexC] = self.demandes[indexC]
                self.stocks[indexL] -= self.demandes[indexC]
                self.demandes[indexC] = 0
            else:
                resultat[indexL][indexC] = self.stocks[indexL]
                self.demandes[indexC] -= self.stocks[indexL]
                self.stocks[indexL] = 0
            
            iterations.append(copy.deepcopy(resultat))

        return iterations, resultat
        

    def calculateCost(self):
        coutFinal = 0

        for i in range(len(self.couts)):
            for j in range(len(self.couts[i])):
                coutFinal+= self.couts[i][j] * self.resultat[i][j]
        return coutFinal
        
# couts = [[10,6,3,5,25],[5,2,6,12,5]]
# stocks = [49,30]
# demandes = [15,20,5,25,14]

# couts = [[7,12,1,5,9],[15,3,12,6,14],[8,16,10,12,7],[18,8,17,11,16]]
# stocks = [12,11,14,8]
# demandes = [10,11,15,5,4]
# resultat=[]
# s=0

# couts = [
#     [21,11,84,49,13],
#     [27,52,43,29,42],
#     [11,47,14,80,93],
#     [52,94,76,74,54]
#     ]
# stocks = [896,782,943,928]
# demandes = [800,439,50,790,1470]

# exemple = RegretMax(couts, stocks, demandes)
# print(exemple.resultat)
# print(exemple.iterations)
# print(exemple.coutFinal)

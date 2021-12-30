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
# resultat=[]
# s=0

class RegretMax:
    def __init__(self, couts, stocks, demandes):
        self.couts = couts
        self.stocks = stocks
        self.demandes = demandes
        self.resultat = self.regretMax()
        self.coutFinal = self.calculateCost()
    
    def regretMax(self):
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

            if max(regretsC) == max(regretsL) :
                indexL = regretsL.index(max(regretsL))
                indexC = regretsC.index(max(regretsC))
                f = indexL
                

                minIndexL = indexL
                minIndexC = indexC
                
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
            
            if max(regretsC) < max(regretsL) :
                indexL = regretsL.index(max(regretsL))
                indexC = regretsC.index(max(regretsC))

                for j in range(len(self.couts[indexL])):
                    if self.couts[indexL][j] < self.couts[indexL][indexC] and self.demandes[j] != 0 :
                        indexC = j

            if self.stocks[indexL] >= self.demandes[indexC] :
                resultat[indexL][indexC] = self.demandes[indexC]
                self.stocks[indexL] -= self.demandes[indexC]
                self.demandes[indexC] = 0
            else:
                resultat[indexL][indexC] = self.stocks[indexL]
                self.demandes[indexC] -= self.stocks[indexL]
                self.stocks[indexL] = 0

        return resultat
        

    def calculateCost(self):
        coutTotal = 0

        for i in range(len(self.couts)):
            for j in range(len(self.couts[i])):
                coutTotal+= self.couts[i][j] * self.resultat[i][j]
        return coutTotal

# exemple = RegretMax(couts, stocks, demandes)
# print(exemple.resultat)
# print(exemple.coutFinal)
# for i in range(len(couts)):
#     resultat.append([0]*len(couts[i]))

# while any(x != 0 for x in stocks):
#     regretsL=[]
#     regretsC=[]
#     for i in range(len(couts[0])):
#         if demandes[i] != 0 :
#             d=[]
#             for j in range(len(couts)) : 
#                 if stocks[j] !=0 : d.append(couts[j][i])
#                 else : d.append(9**50)
#             d.sort()
#             regretsC.append(d[1]-d[0])
#         else : regretsC.append(0)

#     for i in range(len(couts)):
#         if stocks[i] != 0 :
#             d=[]
#             for j in range(len(couts[i])):
#                 if demandes[j] != 0 : d.append(couts[i][j])
#                 else : d.append(9**50)
#             d.sort()
#             regretsL.append(d[1]-d[0])
#         else : regretsL.append(0)
    
    
#     if max(regretsC) > max(regretsL) :
#         indexC = regretsC.index(max(regretsC))
#         indexL = regretsL.index(max(regretsL))
#         for i in range(len(couts)):
#             if couts[i][indexC] < couts[indexL][indexC] and stocks[i] != 0 : 
#                 indexL = i

#     if max(regretsC) == max(regretsL) :
#         indexL = regretsL.index(max(regretsL))
#         indexC = regretsC.index(max(regretsC))
#         f = indexL
        

#         minIndexL = indexL
#         minIndexC = indexC
        
#         minCoutL = couts[indexL][indexC]
#         minCoutC = couts[indexL][indexC]

#         for j in range(len(couts[indexL])):
#             if couts[indexL][j] < minCoutL and demandes[j] != 0 : 
#                 minCoutL = couts[indexL][j]

#         for i in range(len(couts)):
#             if couts[i][indexC] < minCoutC and stocks[i] != 0 : 
#                 minCoutC = couts[i][indexC]
#                 f = i
        
#         if minCoutL < minCoutC :
#             indexC = couts[indexL].index(minCoutL)
        
#         if minCoutL > minCoutC :
#             indexL = f
    
#     if max(regretsC) < max(regretsL) :
#         indexL = regretsL.index(max(regretsL))
#         indexC = regretsC.index(max(regretsC))

#         for j in range(len(couts[indexL])):
#             if couts[indexL][j] < couts[indexL][indexC] and demandes[j] != 0 :
#                 indexC = j

#     if stocks[indexL] >= demandes[indexC] :
#         resultat[indexL][indexC] = demandes[indexC]
#         stocks[indexL] -= demandes[indexC]
#         demandes[indexC] = 0
#     else:
#         resultat[indexL][indexC] = stocks[indexL]
#         demandes[indexC] -= stocks[indexL]
#         stocks[indexL] = 0
    
# for x in resultat : print(x)

# for i in range(len(resultat)):
#     for j in range(len(resultat[i])):
#         s+= couts[i][j] * resultat[i][j]
# print(s)
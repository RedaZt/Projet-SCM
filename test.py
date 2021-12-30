from northwest import NorthWest
from regretmax import RegretMax


couts = [[5,4,11,5,11,8],[7,2,18,11,4,5],[10,7,11,17,8,12],[11,7,15,15,11,16]]
stocks = [120,300,410,250]
demandes = [100,210,200,250,200,120] 

couts = [[0,0,0,0],[0,0,0,0]]
stocks = [0,0]
demandes = [0,0,0,0] 

test = RegretMax(couts, stocks, demandes)

print(test.resultat)
print(test.coutFinal)
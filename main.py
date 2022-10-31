import sys
from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui
from algorithms.NorthWestCorner import NorthWestCorner
from algorithms.LeastCost import LeastCost
from algorithms.BalasHammerAlgorithm import BalasHammerAlgorithm

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle(self.tr('Supply Chain Management Project By Reda Zitouni'))

        self.n = 0 

        self.mainTable = QtWidgets.QTableWidget(3, 4, self)
        self.setHeadersForMainTable()
        fillTableWithZeros(self.mainTable)
        self.textbox = QtWidgets.QLineEdit()
        
        self.buttonAddRow = QtWidgets.QPushButton('Add a line', self)
        self.buttonRemoveRow = QtWidgets.QPushButton('Delete a line', self)
        self.buttonAddColumn = QtWidgets.QPushButton('Add a column', self)
        self.buttonRemoveColumn = QtWidgets.QPushButton('Delete a column', self)
        self.buttonNorthWestCorner = QtWidgets.QPushButton('NorthWest Corner', self)
        self.buttonLeastCost = QtWidgets.QPushButton('Least Cost', self)
        self.buttonBalasHammerAlgorithm = QtWidgets.QPushButton('Balas-Hammer', self)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.buttonAddRow, 0, 0, 1, 2)
        self.layout.addWidget(self.buttonRemoveRow, 0, 2, 1, 2)
        self.layout.addWidget(self.buttonAddColumn, 0, 4, 1, 2)
        self.layout.addWidget(self.buttonRemoveColumn, 0, 6, 1, 2)
        self.layout.addWidget(self.mainTable, 1, 0, 1, 8)
        self.layout.addWidget(self.buttonNorthWestCorner, 2, 1, 1, 2)
        self.layout.addWidget(self.buttonLeastCost, 2, 3, 1, 2)
        self.layout.addWidget(self.buttonBalasHammerAlgorithm, 2, 5, 1, 2)

        self.buttonAddRow.clicked.connect(self.addRow)
        self.buttonRemoveRow.clicked.connect(self.removeRow)
        self.buttonAddColumn.clicked.connect(self.addColumn)
        self.buttonRemoveColumn.clicked.connect(self.removeColumn)
        self.buttonNorthWestCorner.clicked.connect(lambda: self.calculateResults(NorthWestCorner))
        self.buttonLeastCost.clicked.connect(lambda: self.calculateResults(LeastCost))
        self.buttonBalasHammerAlgorithm.clicked.connect(lambda: self.calculateResults(BalasHammerAlgorithm))

    def addRow(self):
        self.mainTable.insertRow(self.mainTable.rowCount())
        for col in range(self.mainTable.columnCount()):
            item = QtWidgets.QTableWidgetItem('0')
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.mainTable.setItem(self.mainTable.rowCount() - 1, col, item)
        self.setHeadersForMainTable()

    def removeRow(self):
        if  self.mainTable.rowCount() > 0 :
            self.mainTable.removeRow(self.mainTable.rowCount() - 1)
        
        self.setHeadersForMainTable()

    def addColumn(self):
        self.mainTable.insertColumn(self.mainTable.columnCount())
        for row in range(self.mainTable.rowCount()):
            item = QtWidgets.QTableWidgetItem('0')
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.mainTable.setItem(row, self.mainTable.columnCount() - 1, item)
        self.setHeadersForMainTable()

    def removeColumn(self):
        if  self.mainTable.columnCount() > 0 :
            self.mainTable.removeColumn(self.mainTable.columnCount() - 1)

        self.setHeadersForMainTable()

    def setHeadersForMainTable(self):
        rowsHeaders = ''.join(f"S{row+1}|" for row in range(self.mainTable.rowCount()-1))
        rowsHeaders += f"Demands"

        columnsHeaders = ''.join(f"D{column+1}|" for column in range(self.mainTable.columnCount()-1))
        columnsHeaders += f"Stocks"

        self.mainTable.setHorizontalHeaderLabels(columnsHeaders.split('|'))
        self.mainTable.setVerticalHeaderLabels(rowsHeaders.split('|'))

    def readInputs(self):
        nrows = self.mainTable.rowCount()
        ncells = self.mainTable.columnCount()
        couts = []
        demandes = []
        stocks = []

        for row in range(nrows):
            d = []
            for cell in range(ncells):
                item = self.mainTable.item(row, cell)
                itemText = int(item.text())
                if row == nrows - 1 : demandes.append(itemText)
                elif cell == ncells - 1 : stocks.append(itemText)
                else : d.append(itemText)
            if d != [] : couts.append(d)
        demandes = demandes[:-1]

        return couts, stocks, demandes

    def calculateResults(self, childFunction):
        couts, stocks, demandes = self.readInputs()
        self.solution = childFunction(couts, stocks, demandes)
        self.printResults()

    def printResults(self):
        x = self.mainTable.rowCount() - 1
        y = self.mainTable.columnCount() - 1
        
        self.resultTable = QtWidgets.QTableWidget(x, y, self)
        setHeaders(self.resultTable)
        fillTable(self.resultTable, self.solution.resultat)
        self.buttonResult = QtWidgets.QPushButton(f"Total Cost = {self.solution.coutFinal}", self)
        self.buttonShowIterations = QtWidgets.QPushButton('Show iterations', self)
        
        self.layout.addWidget(self.resultTable, 3, 0, 5, 8)
        self.layout.addWidget(self.buttonResult, 8, 0, 2, 8)
        self.layout.addWidget(self.buttonShowIterations, 11, 0, 1, 8)

        self.buttonShowIterations.clicked.connect(self.showIterations)
        self.n += 1
    
    def showIterations(self) : 
        x = self.mainTable.rowCount() - 1
        y = self.mainTable.columnCount() - 1

        self.oTabWidget = QtWidgets.QTabWidget()

        self.iterationTables = []
        nIterations = len(self.solution.iterations)
        if nIterations > 5 : nIterations = 5
        for i in range(nIterations):
            self.iterationTables.append(QtWidgets.QTableWidget(x, y, self))
            setHeaders(self.iterationTables[i])
            fillTable(self.iterationTables[i], self.solution.iterations[i])
            self.oTabWidget.addTab(self.iterationTables[i],f"Iteration {i+1}")
        self.oTabWidget.setWindowTitle("Iterations")
        self.oTabWidget.resize(640, 240)
        self.oTabWidget.show()
       
def fillTableWithZeros(table):
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = QtWidgets.QTableWidgetItem('0')
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                table.setItem(row, col, item)

def fillTable(table, data):
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = QtWidgets.QTableWidgetItem(str(data[row][col]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                table.setItem(row, col, item)

def setHeaders(table):
    rowsHeaders = ''.join(f"S{row+1}|" for row in range(table.rowCount()-1))
    columnsHeaders = ''.join(f"D{column+1}|" for column in range(table.columnCount()-1))

    table.setHorizontalHeaderLabels(columnsHeaders.split('|'))
    table.setVerticalHeaderLabels(rowsHeaders.split('|'))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())
import sys
from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui
from northwest import NorthWest
from coutminimal import CoutMinimal
from regretmax import RegretMax

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle(self.tr('Projet Supply Chain Management'))
        # self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.table = QtWidgets.QTableWidget(3, 4, self)
        self.setHeadersForMainTable()
        fillTableWithZeros(self.table)
        self.textbox = QtWidgets.QLineEdit()
        
        self.buttonAddRow = QtWidgets.QPushButton('Add Row', self)
        self.buttonRemoveRow = QtWidgets.QPushButton('Remove Row', self)
        self.buttonAddColumn = QtWidgets.QPushButton('Add Column', self)
        self.buttonRemoveColumn = QtWidgets.QPushButton('Remove Column', self)
        self.buttonNorthWest = QtWidgets.QPushButton('Nord-Ouest', self)
        self.buttonCoutMinimal = QtWidgets.QPushButton('Cout Minimal', self)
        self.buttonRegretMax = QtWidgets.QPushButton('Regret Maximal', self)

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.buttonAddRow, 0, 0, 1, 2)
        self.layout.addWidget(self.buttonRemoveRow, 0, 2, 1, 2)
        self.layout.addWidget(self.buttonAddColumn, 0, 4, 1, 2)
        self.layout.addWidget(self.buttonRemoveColumn, 0, 6, 1, 2)
        self.layout.addWidget(self.table, 1, 0, 1, 8)
        self.layout.addWidget(self.buttonNorthWest, 2, 1, 1, 2)
        self.layout.addWidget(self.buttonCoutMinimal, 2, 3, 1, 2)
        self.layout.addWidget(self.buttonRegretMax, 2, 5, 1, 2)

        self.buttonAddRow.clicked.connect(self.addRow)
        self.buttonRemoveRow.clicked.connect(self.removeRow)
        self.buttonAddColumn.clicked.connect(self.addColumn)
        self.buttonRemoveColumn.clicked.connect(self.removeColumn)
        self.buttonNorthWest.clicked.connect(self.northWest)
        self.buttonCoutMinimal.clicked.connect(self.coutMinimal)
        self.buttonRegretMax.clicked.connect(self.regretMax)

    def northWest(self):
        couts, stocks, demandes = self.readInputs()
        self.solution = NorthWest(couts, stocks, demandes)
        self.printResults()

    def coutMinimal(self):
        couts, stocks, demandes = self.readInputs()
        self.solution = CoutMinimal(couts, stocks, demandes)
        self.printResults()

    def regretMax(self):
        couts, stocks, demandes = self.readInputs()
        self.solution = RegretMax(couts, stocks, demandes)
        self.printResults()

    def readInputs(self):
        nrows = self.table.rowCount()
        ncells = self.table.columnCount()
        couts = []
        demandes = []
        stocks = []

        for row in range(nrows):
            d = []
            for cell in range(ncells):
                item = self.table.item(row, cell)
                itemText = int(item.text())
                if row == nrows - 1 : demandes.append(itemText)
                elif cell == ncells - 1 : stocks.append(itemText)
                else : d.append(itemText)
            if d != [] : couts.append(d)
        demandes = demandes[:-1]

        return couts, stocks, demandes

    def addRow(self):
        self.table.insertRow(self.table.rowCount())
        for col in range(self.table.columnCount()):
            item = QtWidgets.QTableWidgetItem('0')
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(self.table.rowCount() - 1, col, item)
        self.setHeadersForMainTable()

    def removeRow(self):
        if  self.table.rowCount() > 0 :
            self.table.removeRow(
                self.table.rowCount() - 1
            )
        self.setHeadersForMainTable()

    def addColumn(self):
        self.table.insertColumn(self.table.columnCount())
        for row in range(self.table.rowCount()):
            item = QtWidgets.QTableWidgetItem('0')
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row, self.table.columnCount() - 1, item)
        self.setHeadersForMainTable()

    def removeColumn(self):
        if  self.table.columnCount() > 0 :
            self.table.removeColumn(
                self.table.columnCount() - 1
            )
        self.setHeadersForMainTable()

    def setHeadersForMainTable(self):
        rowsHeaders = ""
        for row in range(self.table.rowCount()-1):
            rowsHeaders += f"S{row+1}|"
        rowsHeaders += f"Demandes"

        columnsHeaders = ""
        for column in range(self.table.columnCount()-1):
            columnsHeaders += f"D{column+1}|"
        columnsHeaders += f"Stocks"

        self.table.setHorizontalHeaderLabels(
            columnsHeaders.split('|'))
        self.table.setVerticalHeaderLabels(
            rowsHeaders.split('|')
        )

    def printResults(self):
        x = len(self.solution.resultat)
        y = len(self.solution.resultat[0])
        
        self.table2 = QtWidgets.QTableWidget(x, y, self)
        setHeaders(self.table2)
        self.buttonResult = QtWidgets.QPushButton(f"Cout Final = {self.solution.coutFinal}", self)
        self.buttonShowIterations = QtWidgets.QPushButton('Afficher les iterations', self)

        for row in range(self.table2.rowCount()):
            for col in range(self.table2.columnCount()):
                item = QtWidgets.QTableWidgetItem(str(self.solution.resultat[row][col]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table2.setItem(row, col, item)
        
        self.layout.addWidget(self.table2, 3, 0, 4, 8)
        self.layout.addWidget(self.buttonResult, 8, 0, 2, 8)
        self.layout.addWidget(self.buttonShowIterations, 11, 0, 1, 8)
        self.buttonShowIterations.clicked.connect(self.showIterations)
    
    def showIterations(self) : 
        self.buttonShowResult = QtWidgets.QPushButton("Afficher resultat final", self)
        self.table3 = QtWidgets.QTableWidget(2, 4, self)
        setHeaders(self.table3)
        fillTableWithZeros(self.table3)
        self.table4 = QtWidgets.QTableWidget(2, 4, self)
        setHeaders(self.table4)
        fillTableWithZeros(self.table4)
        self.layout.addWidget(self.table3, 3, 0, 4, 8)
        self.layout.addWidget(self.table4, 7, 0, 4, 8)
        self.layout.addWidget(self.buttonShowResult, 11, 0, 1, 8)
        self.buttonShowResult.clicked.connect(self.bringBackResult)

    def bringBackResult(self) :
        self.layout.removeWidget(self.table3)
        self.table3.deleteLater()
        self.layout.removeWidget(self.table4)
        self.table4.deleteLater()
        self.layout.removeWidget(self.buttonShowResult)
        self.buttonShowResult.deleteLater()
        self.printResults()
       
def fillTableWithZeros(table):
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = QtWidgets.QTableWidgetItem('0')
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                table.setItem(row, col, item)

def setHeaders(table):
    rowsHeaders = ""
    for row in range(table.rowCount()):
        rowsHeaders += f"S{row+1}|"

    columnsHeaders = ""
    for column in range(table.columnCount()):
        columnsHeaders += f"D{column+1}|"

    table.setHorizontalHeaderLabels(
        columnsHeaders.split('|'))
    table.setVerticalHeaderLabels(
        rowsHeaders.split('|')
    )

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())

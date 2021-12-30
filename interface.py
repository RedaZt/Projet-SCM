import sys
from PyQt5 import QtWidgets, QtCore, QtPrintSupport, QtGui
from northwest import NorthWest
from coutminimal import CoutMinimal
from regretmax import RegretMax


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle(self.tr('Projet'))
        self.table = QtWidgets.QTableWidget(0, 0, self)

        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = QtWidgets.QTableWidgetItem('0')
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(row, col, item)

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
        self.layout.addWidget(self.buttonNorthWest, 2, 1, 1, 2)
        self.layout.addWidget(self.buttonCoutMinimal, 2, 3, 1, 2)
        self.layout.addWidget(self.buttonRegretMax, 2, 5, 1, 2)
        self.layout.addWidget(self.table, 1, 0, 1, 8)

        self.buttonAddRow.clicked.connect(self.addRow)
        self.buttonRemoveRow.clicked.connect(self.removeRow)
        self.buttonAddColumn.clicked.connect(self.addColumn)
        self.buttonRemoveColumn.clicked.connect(self.removeColumn)
        self.buttonNorthWest.clicked.connect(self.northWest)
        self.buttonCoutMinimal.clicked.connect(self.coutMinimal)
        self.buttonRegretMax.clicked.connect(self.regretMax)

    def northWest(self):
        couts, stocks, demandes = self.gatherInputs()
        self.solution = NorthWest(couts, stocks, demandes)
        self.printResults()

    def coutMinimal(self):
        couts, stocks, demandes = self.gatherInputs()
        self.solution = CoutMinimal(couts, stocks, demandes)
        self.printResults()

    def regretMax(self):
        couts, stocks, demandes = self.gatherInputs()
        self.solution = RegretMax(couts, stocks, demandes)
        self.printResults()

    def gatherInputs(self):
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
        self.setHeaders()

    def removeRow(self):
        if  self.table.rowCount() > 0 :
            self.table.removeRow(
                self.table.rowCount() - 1
            )
            self.setHeaders()

    def addColumn(self):
        self.table.insertColumn(self.table.columnCount())
        for row in range(self.table.rowCount()):
            item = QtWidgets.QTableWidgetItem('0')
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row, self.table.columnCount() - 1, item)
        self.setHeaders()

    def removeColumn(self):
        if  self.table.columnCount() > 0 :
            self.table.removeColumn(
                self.table.columnCount() - 1
            )
        self.setHeaders()

    def setHeaders(self):
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
        self.buttonResult = QtWidgets.QPushButton(f"Cout Final = {self.solution.coutFinal}", self)

        for row in range(self.table2.rowCount()):
            for col in range(self.table2.columnCount()):
                item = QtWidgets.QTableWidgetItem(str(self.solution.resultat[row][col]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table2.setItem(row, col, item)
        
        self.layout.addWidget(self.table2, 3, 0, 3, 8)
        self.layout.addWidget(self.buttonResult, 7, 0, 1, 8)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())
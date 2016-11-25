# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

"""
In this example, we create a skeleton
of a calculator using a QtGui.QGridLayout.
"""

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        title = QtGui.QLabel('Result')
        result_line = QtGui.QLineEdit()

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        grid.addWidget(title,0,0)
        grid.addWidget(result_line,0,1,1,3)

        positions = [(i,j) for i in range(5) for j in range(4)]

        for i, j in positions:
            name = names[j+4*i]
            if name == '':
                continue
            button = QtGui.QPushButton(name)
            grid.addWidget(button, i+1,j)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
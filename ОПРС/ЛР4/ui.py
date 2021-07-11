from PyQt5.QtWidgets import *
import linal
import form


class MainWindow(QMainWindow, form.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.transpose.clicked.connect(self.transp)
        self.plus.clicked.connect(self.sum)
        self.scalar.clicked.connect(self.scal)
        self.matrix.clicked.connect(self.mat)
        self.vector.clicked.connect(self.vec)
        self.inverse.clicked.connect(self.inv)
        self.det.clicked.connect(self.determ)

        self.k_mul.clicked.connect(self.mul_k)
        self.k_n.clicked.connect(self.n_k)
        self.k_norm.clicked.connect(self.norm_k)
        self.k_rot.clicked.connect(self.rot_k)
        self.k_sum.clicked.connect(self.sum_k)
        self.k_vec_mul.clicked.connect(self.mul_vec_k)

        self.length.clicked.connect(self.len)
        self.radioButton.clicked.connect(self.rb)
        self.radioButton_2.clicked.connect(self.rb2)
        self.setWindowOpacity(0.999)
        self.radioButton.setChecked(True)
        self.rb()

    def mul_k(self):
        pass

    def n_k(self):
        pass

    def norm_k

    def rb(self):
        for i in range(self.gridLayout_7.rowCount()):
            for j in range(self.gridLayout_7.columnCount()):
                if i != 0:
                    self.gridLayout_7.itemAtPosition(i, j).widget().setReadOnly(False)
                    self.gridLayout_7.itemAtPosition(i, j).widget().setStyleSheet('background-color: black')
        for i in range(self.gridLayout_8.rowCount()):
            for j in range(self.gridLayout_8.columnCount()):
                if j != 0:
                    self.gridLayout_8.itemAtPosition(i, j).widget().setReadOnly(False)
                    self.gridLayout_8.itemAtPosition(i, j).widget().setStyleSheet('background-color: black')
        self.vector.setDisabled(True)
        self.vector.setStyleSheet('color: rgb(60, 60, 60)')
        self.scalar.setDisabled(True)
        self.scalar.setStyleSheet('color: rgb(60, 60, 60)')
        self.length.setDisabled(True)
        self.length.setStyleSheet('color: rgb(60, 60, 60)')

        self.transpose.setDisabled(False)
        self.transpose.setStyleSheet('color:white')
        self.plus.setDisabled(False)
        self.plus.setStyleSheet('color:white')
        self.matrix.setDisabled(False)
        self.matrix.setStyleSheet('color:white')
        self.inverse.setDisabled(False)
        self.inverse.setStyleSheet('color:white')
        self.det.setDisabled(False)
        self.det.setStyleSheet('color:white')

    def rb2(self):
        for i in range(self.gridLayout_7.rowCount()):
            for j in range(self.gridLayout_7.columnCount()):
                if i != 0:
                    self.gridLayout_7.itemAtPosition(i, j).widget().setReadOnly(True)
                    self.gridLayout_7.itemAtPosition(i, j).widget().setStyleSheet('background-color: rgb(30, 30, 30)')
        for i in range(self.gridLayout_8.rowCount()):
            for j in range(self.gridLayout_8.columnCount()):
                if j != 0:
                    self.gridLayout_8.itemAtPosition(i, j).widget().setReadOnly(True)
                    self.gridLayout_8.itemAtPosition(i, j).widget().setStyleSheet('background-color: rgb(30, 30, 30)')
        self.vector.setDisabled(False)
        self.vector.setStyleSheet('color: white')
        self.scalar.setDisabled(False)
        self.scalar.setStyleSheet('color: white')
        self.length.setDisabled(False)
        self.length.setStyleSheet('color: white')

        self.transpose.setDisabled(True)
        self.transpose.setStyleSheet('color:rgb(60, 60, 60)')
        self.plus.setDisabled(True)
        self.plus.setStyleSheet('color:rgb(60, 60, 60)')
        self.matrix.setDisabled(True)
        self.matrix.setStyleSheet('color:rgb(60, 60, 60)')
        self.inverse.setDisabled(True)
        self.inverse.setStyleSheet('color:rgb(60, 60, 60)')
        self.det.setDisabled(True)
        self.det.setStyleSheet('color:rgb(60, 60, 60)')

    def transp(self):
        if self.tabWidget_2.currentIndex() == 0:
            m = linal.Matrix(self.take_values(self.gridLayout_7))
            matrix = m.transpose()
            print(0)
        else:
            m = linal.Matrix(self.take_values(self.gridLayout_8))
            matrix = m.transpose()
            print(1)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if self.tabWidget_2.currentIndex() == 0:
                    self.gridLayout_7.itemAtPosition(i, j).widget().setText(str(matrix[i][j]))
                else:
                    self.gridLayout_8.itemAtPosition(i, j).widget().setText(str(matrix[i][j]))

    def sum(self):
        m = linal.Matrix(self.take_values(self.gridLayout_7))
        matrix = m + self.take_values(self.gridLayout_8)
        self.tableWidget.setColumnCount(len(matrix))
        self.tableWidget.setRowCount(len(matrix[0]))

        for i in range(len(matrix)):
            self.tableWidget.setColumnWidth(i, 560/len(matrix))
            for j in range(len(matrix[i])):
                self.tableWidget.setRowHeight(j, 650/len(matrix[i]))
                self.tableWidget.setItem(i, j, QTableWidgetItem(matrix[i][j]))

    def scal(self):
        self.lineEdit_19.setText(str(linal.scalar_product(self.take_values_vec1(), self.take_values_vec2())))

    def mat(self):
        m = linal.Matrix(self.take_values(self.gridLayout_7))
        matrix = m * self.take_values(self.gridLayout_8)
        self.tableWidget.setColumnCount(len(matrix))
        self.tableWidget.setRowCount(len(matrix[0]))

        for i in range(len(matrix)):
            self.tableWidget.setColumnWidth(i, 560 / len(matrix))
            for j in range(len(matrix[i])):
                self.tableWidget.setRowHeight(j, 650 / len(matrix[i]))
                self.tableWidget.setItem(i, j, QTableWidgetItem(matrix[i][j]))

    def vec(self):
        v = linal.Vector(self.take_values_vec1())
        vec = v * self.take_values_vec2()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)

        for i in range(len(vec)):
            self.tableWidget.setColumnWidth(i, 560 / len(vec))
            self.tableWidget.setRowHeight(0, 200)
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(vec[i])))

    def inv(self):
        if self.tabWidget_2.currentIndex() == 0:
            m = linal.Matrix(self.take_values(self.gridLayout_7))
            matrix = m.inverse()
        else:
            m = linal.Matrix(self.take_values(self.gridLayout_8))
            matrix = m.inverse()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if self.tabWidget_2.currentIndex() == 0:
                    self.gridLayout_7.itemAtPosition(i, j).widget().setText(str(
                        round(matrix[i][j], int(self.lineEdit.text()))))
                else:
                    self.gridLayout_8.itemAtPosition(i, j).widget().setText(str(
                        round(matrix[i][j], int(self.lineEdit.text()))))

    def determ(self):
        if self.tabWidget_2.currentIndex() == 0:
            m = linal.Matrix(self.take_values(self.gridLayout_7))
            self.lineEdit_19.setText(str(m.determinant()))
        else:
            m = linal.Matrix(self.take_values(self.gridLayout_8))
            self.lineEdit_19.setText(str(m.determinant()))

    def len(self):
        if self.tabWidget_2.currentIndex() == 0:
            v = linal.Vector(self.take_values_vec1())
            self.lineEdit_19.setText(str(v.length()))
        else:
            v = linal.Vector(self.take_values_vec2())
            self.lineEdit_19.setText(str(v.length()))

    def take_values(self, layout):
        matrix = []
        for i in range(layout.rowCount()):
            row = []
            for j in range(layout.columnCount()):
                if self.gridLayout_7.itemAtPosition(i, j).widget().text() != '':
                    row.append((layout.itemAtPosition(i, j).widget().text()))
            if self.gridLayout_7.itemAtPosition(i, 0).widget().text() != '':
                matrix.append(row)
        return matrix

    def take_values_vec1(self):
        vector = []
        for i in range(self.gridLayout_7.rowCount()):
            for j in range(self.gridLayout_7.columnCount()):
                if self.gridLayout_7.itemAtPosition(i, j).widget().text() != '' \
                        and self.gridLayout_7.itemAtPosition(i, j).widget().isReadOnly() is False:
                    vector.append((float(self.gridLayout_7.itemAtPosition(i, j).widget().text())))
        return vector

    def take_values_vec2(self):
        vector = []
        for i in range(self.gridLayout_8.rowCount()):
            for j in range(self.gridLayout_8.columnCount()):
                if self.gridLayout_7.itemAtPosition(i, j).widget().text() != '' \
                        and self.gridLayout_8.itemAtPosition(i, j).widget().isReadOnly() is False:
                    vector.append((float(self.gridLayout_8.itemAtPosition(i, j).widget().text())))
        return vector

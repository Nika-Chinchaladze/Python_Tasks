from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(983, 582)
        MainWindow.setStyleSheet("background-color: rgb(253, 253, 253);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.task1 = QtWidgets.QPushButton(self.centralwidget)
        self.task1.setGeometry(QtCore.QRect(110, 510, 91, 51))
        self.task1.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.task1.setObjectName("task1")
        
        self.task2 = QtWidgets.QPushButton(self.centralwidget)
        self.task2.setGeometry(QtCore.QRect(240, 510, 91, 51))
        self.task2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.task2.setObjectName("task2")

        self.task3 = QtWidgets.QPushButton(self.centralwidget)
        self.task3.setGeometry(QtCore.QRect(370, 510, 91, 51))
        self.task3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.task3.setObjectName("task3")
        
        self.task4 = QtWidgets.QPushButton(self.centralwidget)
        self.task4.setGeometry(QtCore.QRect(500, 510, 91, 51))
        self.task4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.task4.setObjectName("task4")

        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(630, 510, 91, 51))
        self.clear.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.clear.setObjectName("clear")
        
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(760, 510, 91, 51))
        self.exit_button.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.exit_button.setObjectName("exit_button")
        
        self.first = QtWidgets.QLabel(self.centralwidget)
        self.first.setGeometry(QtCore.QRect(20, 5, 941, 45))
        self.first.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.first.setFrameShape(QtWidgets.QFrame.Box)
        self.first.setMidLineWidth(0)
        self.first.setText("")
        self.first.setObjectName("first")
        
        self.second = QtWidgets.QLabel(self.centralwidget)
        self.second.setGeometry(QtCore.QRect(20, 60, 941, 45))
        self.second.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.second.setFrameShape(QtWidgets.QFrame.Box)
        self.second.setMidLineWidth(0)
        self.second.setText("")
        self.second.setObjectName("second")
        
        self.third = QtWidgets.QLabel(self.centralwidget)
        self.third.setGeometry(QtCore.QRect(20, 115, 941, 45))
        self.third.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.third.setFrameShape(QtWidgets.QFrame.Box)
        self.third.setMidLineWidth(0)
        self.third.setText("")
        self.third.setObjectName("third")
        
        self.fourth = QtWidgets.QLabel(self.centralwidget)
        self.fourth.setGeometry(QtCore.QRect(20, 172, 941, 45))
        self.fourth.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.fourth.setFrameShape(QtWidgets.QFrame.Box)
        self.fourth.setMidLineWidth(0)
        self.fourth.setText("")
        self.fourth.setObjectName("fourth")
        
        self.fifth = QtWidgets.QLabel(self.centralwidget)
        self.fifth.setGeometry(QtCore.QRect(20, 230, 450, 130))
        self.fifth.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.fifth.setFrameShape(QtWidgets.QFrame.Box)
        self.fifth.setMidLineWidth(0)
        self.fifth.setText("")
        self.fifth.setObjectName("fifth")
        
        self.sixth = QtWidgets.QLabel(self.centralwidget)
        self.sixth.setGeometry(QtCore.QRect(500, 230, 460, 130))
        self.sixth.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.sixth.setFrameShape(QtWidgets.QFrame.Box)
        self.sixth.setMidLineWidth(0)
        self.sixth.setText("")
        self.sixth.setObjectName("sixth")
        
        self.seventh = QtWidgets.QLabel(self.centralwidget)
        self.seventh.setGeometry(QtCore.QRect(245, 370, 460, 135))
        self.seventh.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.seventh.setFrameShape(QtWidgets.QFrame.Box)
        self.seventh.setMidLineWidth(0)
        self.seventh.setText("")
        self.seventh.setObjectName("seventh")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# ------------------------------------------- LOGIC -------------------------------------------- #
        # call functions from here:
        self.task1.clicked.connect(self.First_task)
        self.task2.clicked.connect(self.Second_task)
        self.task3.clicked.connect(self.Third_task)
        self.task4.clicked.connect(self.Fourth_task)
        self.clear.clicked.connect(self.Clear_text)
        self.exit_button.clicked.connect(MainWindow.close)

    # define first_task method:
    def First_task(self):
        first = np.random.randint(1, 51, size = 50)
        even = first[first % 2 == 0]
        div_5 = first[first % 5 == 0]
        self.first.setText(f'Source Array: {first}')
        self.second.setText(f'Array of Even Numbers: {even}')
        self.third.setText(f'Array of Numbers, that are divisible by 5: {div_5}')
        self.fourth.setText("")
        self.fifth.setText("")
        self.sixth.setText("")
        self.seventh.setText("")
    
    # define second_task method:
    def Second_task(self):
        first = np.random.randint(1, 51, size = 50)
        second = np.random.randint(51, 101, size = 50)

        jami = first + second
        sxvaoba = first - second
        namravli = first * second
        ganayofi = first / second
        together = np.concatenate((first, second))
        together = np.reshape(together, (5, 20))

        self.first.setText(f'First Array {first}')
        self.second.setText(f'Second Array {second}')
        self.third.setText(f'Sum of First and Second Arrays {jami}')
        self.fourth.setText(f'Sub of First and Second Arrays {sxvaoba}')
        self.fifth.setText(f'Multiplication of First and Second Arrays {namravli}')
        self.sixth.setText(f'Division of First and Second Arrays {ganayofi}')
        self.seventh.setText(f'Concatination of First and Second Arrays {together}')
    
    # define third_task method:
    def Third_task(self):
        number = np.random.randint(10, 11)
        new = np.random.randint(40, 60, size = number)
        more = new[new > 50]
        less = new[new < 50]

        if len(more) > len(less):
            difference = len(more) - len(less)
            zero = np.zeros(difference, dtype="int")
            less = np.concatenate((less, zero))

        elif len(more) < len(less):
            difference = len(less) - len(more)
            zero = np.zeros(difference, dtype="int")
            more = np.concatenate((more, zero))
        joined = more + less

        self.first.setText(f'Random Number - Size of Source Array is {number}')
        self.second.setText(f'Source Array {new}')
        self.third.setText(f'More than 50 {more}')
        self.fourth.setText(f'Less than 50 {less}')
        self.fifth.setText(f'Sum of More and Less Arrays {joined}')
        self.sixth.setText("")
        self.seventh.setText("")
    
    # define Fouth_task method:
    def Fourth_task(self):
        elements = np.random.randint(10, 30, size = 20)
        number = np.random.randint(0, len(elements))
        deleted = np.delete(elements, number)

        self.first.setText(f'Source Array {elements}')
        self.second.setText(f'Index of Number, which will be deleted: {number}')
        self.third.setText(f'Number, that will be deleted: {elements[number]}')
        self.fourth.setText(f'Deleted Array {deleted}')
        self.fifth.setText("")
        self.sixth.setText("")
        self.seventh.setText("")
    
    # define clear method:
    def Clear_text(self):
        self.first.setText("")
        self.second.setText("")
        self.third.setText("")
        self.fourth.setText("")
        self.fifth.setText("")
        self.sixth.setText("")
        self.seventh.setText("")
    


# -------------------------------------------- END --------------------------------------------- #
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.task1.setText(_translate("MainWindow", "task_1"))
        self.task2.setText(_translate("MainWindow", "task_2"))
        self.task4.setText(_translate("MainWindow", "task_4"))
        self.task3.setText(_translate("MainWindow", "task_3"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.exit_button.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

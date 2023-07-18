################################################################################
##
## BY: Ahmed Ashraf
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Validation import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.Submit.clicked.connect(
            self.handle_button_click)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##



    def handle_button_click(self):
        # Retrieve input values
        Equation = self.findChild(QLineEdit, "Equation_input").text()
        domain = [self.findChild(QLineEdit, "Start_x_input").text(), self.findChild(QLineEdit, "End_x_input").text()]
        Excepted_x_input = self.findChild(QLineEdit, "Excepted_x_input").text()

        validation= ValidationAndPloting(Equation, domain, Excepted_x_input)
        Equation_valid, Domain_valid, Excepted_x_valid = validation.Get_Result()
        
        if not Equation_valid:
            self.findChild(QLineEdit, "Equation_input").setStyleSheet(
                "border: 2px solid red; ; background-color: rgb(255, 255, 255);")
            # Change the stylesheet of the label
            self.ui.error_equation.setStyleSheet("color: red; ")
            # Change the height of the label
            self.ui.error_equation.setFixedHeight(30)
            # Change the text of the label
            self.ui.error_equation.setText("Invalid Eqution please try again")

            self.findChild(QLineEdit, "Start_x_input").setStyleSheet(
                "border: 2px solid white; ; background-color: rgb(255, 255, 255);")
            self.findChild(QLineEdit, "End_x_input").setStyleSheet(
                "border: 2px solid white; ; background-color: rgb(255, 255, 255);")
            self.ui.error_domain.setFixedHeight(0)

            self.findChild(QLineEdit, "Excepted_x_input").setStyleSheet(
                "border: 2px solid white; ; background-color: rgb(255, 255, 255);")
            self.ui.error_except.setFixedHeight(30)



        elif not Domain_valid:

            self.findChild(QLineEdit, "Start_x_input").setStyleSheet(
                "border: 2px solid red; ; background-color: rgb(255, 255, 255);")
            self.findChild(QLineEdit, "End_x_input").setStyleSheet(
                "border: 2px solid red; ; background-color: rgb(255, 255, 255);")
            
            # Change the stylesheet of the label
            self.ui.error_domain.setStyleSheet("color: red; ")
            # Change the height of the label
            self.ui.error_domain.setFixedHeight(30)
            # Change the text of the label
            self.ui.error_domain.setText("Invalid domain please try again")

            self.findChild(QLineEdit, "Equation_input").setStyleSheet(
                "border: 2px solid white; ; background-color: rgb(255, 255, 255);")
            self.ui.error_equation.setFixedHeight(30)

            self.ui.error_except.setFixedHeight(30)



        elif Excepted_x_valid != None and Excepted_x_valid == False:
            self.findChild(QLineEdit, "Excepted_x_input").setStyleSheet(
                "border: 2px solid red; ; background-color: rgb(255, 255, 255);")

            # Change the stylesheet of the label
            self.ui.error_except.setStyleSheet("color: red; ")
            # Change the height of the label
            self.ui.error_except.setFixedHeight(30)
            # Change the text of the label
            self.ui.error_except.setText(
                "Invalid Excepted Points please try again")
            
        else :
            self.plot_equation(Equation.replace("^", "**"),
                               Domain_valid, Excepted_x_valid)




    # Plot the equation in the frame

    def plot_equation(self, expression, domain, excepted_Points):
        x = sp.Symbol('x')
        equation = sp.sympify(expression)
        function = sp.lambdify(x, equation, 'numpy')

        x_values = np.linspace(domain[0], domain[1], 100)
        y_values = function(x_values)

        
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        ax.clear()
        # Plot the equation

        if excepted_Points:
            for point in excepted_Points:
                ax.plot(point, function(point), 'o',
                        markerfacecolor='white', markersize=8)
                
        
        ax.plot(x_values, y_values)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Plot of Equation')
        ax.grid(True)

        # Create a FigureCanvas for the figure
        canvas = FigureCanvas(fig)
        layout = QVBoxLayout(self.ui.Matplotlip_Image)
        layout.addWidget(canvas)










if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

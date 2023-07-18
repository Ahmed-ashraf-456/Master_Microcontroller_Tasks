from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide2 import QtCore
import numpy as np
import matplotlib.pyplot as plt


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Plot Example")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout to hold the plot and button
        layout = QVBoxLayout(central_widget)

        # Create a plot widget
        self.plot_widget = plt.figure().canvas

        # Create a button to trigger the data update
        button = QPushButton("Update Data")

        # Connect the button's clicked signal to a slot function
        button.clicked.connect(self.update_plot_data)

        # Add the plot widget and button to the layout
        layout.addWidget(self.plot_widget)
        layout.addWidget(button)

    def update_plot_data(self):
        # Generate new data
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)

        # Clear the previous plot
        self.plot_widget.figure.clear()

        # Plot the new data
        ax = self.plot_widget.figure.add_subplot(111)
        ax.plot(x, y)

        # Trigger a redraw of the plot widget
        self.plot_widget.draw()


if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()

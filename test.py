
import PyQt5 as QtWidgets
from PyQt5 import QtCore, QtGui
import PyQt5.QtWidgets as QtWidgets
import numpy as np
def chatgpt():
    app = QtWidgets.QApplication([])

    # Create a main window
    main_window = QtWidgets.QMainWindow()
    main_window.setWindowTitle("PyQt5 Example")

    # Create a central widget
    central_widget = QtWidgets.QWidget()
    main_window.setCentralWidget(central_widget)

    # Create a layout
    layout = QtWidgets.QVBoxLayout(central_widget)

    # Create a label
    label = QtWidgets.QLabel("Hello, PyQt5!")
    layout.addWidget(label)

    # Show the main window
    main_window.show()

    app.exec_()
if __name__ == "__main__":
    chatgpt()
    print(np.__version__)
    print(QtWidgets.__version__)
    print("Hello, world!")
    print("This is a test script for PyQt5 and NumPy.")
    print("This script is running successfully.")
    print("You can modify this script to add more functionality.")
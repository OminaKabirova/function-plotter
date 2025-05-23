
import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

class FunctionPlotter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Function Plotter")

        layout = QVBoxLayout()

        self.label = QLabel("Type a function like: x**2 or np.sin(x)")
        layout.addWidget(self.label)

        self.input_box = QLineEdit()
        layout.addWidget(self.input_box)

        self.plot_button = QPushButton("Plot")
        layout.addWidget(self.plot_button)

        self.plot_button.clicked.connect(self.plot_function)

        self.setLayout(layout)

    def plot_function(self):
        expr = self.input_box.text()  
        x = np.linspace(-10, 10, 400)  
        try:
            y = eval(expr, {"x": x, "np": np})  
            plt.plot(x, y)
            plt.title(f"y = {expr}")
            plt.grid(True)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.show()
        except Exception as e:
            self.label.setText(f"❌ Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec())

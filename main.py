# Imports
# Terminal: pip install pyqt6
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys

class BmiCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        grid = QGridLayout()

        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        height_label = QLabel("Height in meters:")
        self.height_line_edit = QLineEdit()

        weight_label = QLabel("Weight in kg:")
        self.weight_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate BMI")
        calculate_button.clicked.connect(self.calculate_bmi)
        self.output_label = QLabel("")

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(height_label, 1, 0)
        grid.addWidget(self.height_line_edit, 1, 1)
        grid.addWidget(weight_label, 2, 0)
        grid.addWidget(self.weight_line_edit, 2, 1)
        grid.addWidget(calculate_button, 3, 0, 1, 2)
        grid.addWidget(self.output_label, 4, 0, 1, 2)

        self.setLayout(grid)

    def calculate_bmi(self):
        height = float(self.height_line_edit.text())
        weight = int(self.weight_line_edit.text())
        bmi = weight / (height * height)
        bmi_rounded = int(bmi)
        self.output_label.setText(f"{self.name_line_edit.text()}, your BMI is: {bmi_rounded}")

app = QApplication(sys.argv)
bmi_calculator = BmiCalculator()
bmi_calculator.show()
sys.exit(app.exec())
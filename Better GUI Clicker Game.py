import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
)
from PyQt6.QtGui import QFont, QPalette, QColor
from PyQt6.QtCore import Qt

class ClickerGame(QWidget):
    def __init__(self):
        super().__init__()

        # Game logic
        self.score = 0
        self.click_value = 1
        self.upgrade_cost = 10

        # Setup UI
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("🌟 Clicker Hero - Python Edition")
        self.setFixedSize(500, 400)  # Fixed window size (game-like)

        # Dark game-like background
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#1e1e2f"))  # Dark navy blue
        self.setPalette(palette)

        # Global layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Score display
        self.score_label = QLabel(f"Score: {self.score}")
        self.score_label.setFont(QFont("Consolas", 24, QFont.Weight.Bold))
        self.score_label.setStyleSheet("color: #ffffff;")
        main_layout.addWidget(self.score_label)

        # Button layout (horizontal)
        button_layout = QHBoxLayout()

        # Click button
        self.click_button = QPushButton("🖱 Click Me!")
        self.click_button.setFont(QFont("Verdana", 16))
        self.click_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: dark white;
                padding: 12px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.click_button.clicked.connect(self.handle_click)
        button_layout.addWidget(self.click_button)

        # Upgrade button
        self.upgrade_button = QPushButton(f"⚙ Upgrade (+1) - Cost: {self.upgrade_cost}")
        self.upgrade_button.setFont(QFont("Verdana", 14))
        self.upgrade_button.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #138496;
            }
        """)
        self.upgrade_button.clicked.connect(self.buy_upgrade)
        button_layout.addWidget(self.upgrade_button)

        main_layout.addLayout(button_layout)

        # Set final layout
        self.setLayout(main_layout)

    def handle_click(self):
        self.score += self.click_value
        self.update_ui()

    def buy_upgrade(self):
        if self.score >= self.upgrade_cost:
            self.score -= self.upgrade_cost
            self.click_value += 1
            self.upgrade_cost *= 2
        self.update_ui()

    def update_ui(self):
        self.score_label.setText(f"Score: {self.score}")
        if self.score >= self.upgrade_cost:
            self.upgrade_button.setText(f"⚙ Upgrade (+1) - Cost: {self.upgrade_cost}")
        else:
            self.upgrade_button.setText(f"⛔ Need {self.upgrade_cost} to Upgrade")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClickerGame()
    window.show()
    sys.exit(app.exec())

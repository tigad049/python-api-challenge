import sys
import controller
from PyQt6.QtGui import QPalette, QColor, QPixmap, QFont
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
)

def clamp(n, min_value, max_value):
    return max(min_value, min(n, max_value))
    
# Hey Mr. Winikka, I really hope you don't mind me using some of your code in this project ~dt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        image_id, image_url = controller.get_image()
        controller.download_image(image_id, image_url)

        self.setWindowTitle("Shibe Generator")
        self.setContentsMargins(24, 24, 24, 24)

        layout = QGridLayout()

        # Title
        title_label = QLabel("Shibe Generator")
        title_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font: bold 30pt Verdana")

        # Shibe Image
        self.image_label = QLabel(self)
        pixmap = QPixmap(f"cache/{image_id}.jpg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Get Shibe button
        self.get_shibe_button = QPushButton("Get a Shibe")
        self.get_shibe_button.setStyleSheet("font: 15pt Verdana")

        self.get_shibe_button.clicked.connect(self.new_image)

        # Add widgets to the layout
        layout.addWidget(title_label)
        layout.addWidget(self.image_label)
        layout.addWidget(self.get_shibe_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setFixedSize(QSize(720, 720))
    
    def new_image(self):
        image_id, image_url = controller.get_image()
        controller.download_image(image_id, image_url)
        pixmap = QPixmap(f"cache/{image_id}.jpg")
        self.image_label.setPixmap(pixmap)


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
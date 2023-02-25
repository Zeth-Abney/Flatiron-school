import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window size, title, and allow it to accept drops
        self.setWindowTitle("Coffee Classifier")
        self.resize(1000, 1000)
        self.setAcceptDrops(True)

        # Set up the main layout
        mainLayout = QVBoxLayout()

        # Create the top image label and add it to the layout
        self.photoViewer = ImageLabel()
        self.photoViewer.setFixedSize(1000,500)
        mainLayout.addWidget(self.photoViewer)

        # Create the bottom label for the file path and add it to the layout
        self.pathLabel = QLabel()
        mainLayout.addWidget(self.pathLabel)

        # Set the layout for the window
        self.setLayout(mainLayout)

    def dragEnterEvent(self, event):
        # Check if the event has image data and accept it if it does
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        # Check if the event has image data and accept it if it does
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        # Check if the event has image data and set the image if it does
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)
            # Set the text of the file path label to the dropped image's file path
            self.pathLabel.setText(file_path)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        # Set the pixmap for the top image label using the dropped image's file path
        self.photoViewer.setPixmap(QPixmap(file_path))

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
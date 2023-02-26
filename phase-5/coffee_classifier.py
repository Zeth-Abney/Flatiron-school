import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import load_model

coffee_vision = load_model('data/final_model.h5')

def classify_bean(filepath:str):
    """
    Classifies the roast level of a coffee bean image.

    Args:
        filepath (str): The file path of the coffee bean image to classify.

    Returns:
         string: the predicted label as a string: "Green", "Light", "Medium" or "Dark".

    Raises:
        ValueError: If the input image is not a valid file or if the input image shape is not 224x224.
    """

    if not os.path.isfile(filepath):
        print("Error: {} is not a valid file path.".format(filepath))
        return

    else:
        # Load image and resize to model input shape
        img = load_img(filepath, target_size=(224, 224))

        # Convert image data to numpy array
        img_array = img_to_array(img)

        # Convert the image to grayscale
        img_array = np.dot(img_array, [0.2989, 0.5870, 0.1140])

        # Normalize the image array
        img_array /= 255.0

        # Expand dimensions to match the input shape of the model
        input_array = np.expand_dims(img_array, axis=0)
        input_array = np.expand_dims(input_array, axis=-1)

        # Make predictions
        predictions = coffee_vision.predict(input_array)
        predicted_label = np.argmax(predictions)

        label_dict = {0:"Green",1:"Light",2:"Medium",3:"Dark"}

        return label_dict[predicted_label]


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

        # Create the label for the predicted label and add it to the layout
        self.label = QLabel()
        mainLayout.addWidget(self.label)

        # Set the layout for the window
        self.setLayout(mainLayout)

    def classify_image(self, file_path):
        try:
            predicted_label = classify_bean(file_path)
            self.label.setText("Predicted label: " + predicted_label)
        except ValueError as e:
            self.label.setText("Error: " + str(e))

    def dragEnterEvent(self, event):
        # Check if the event has image data and accept it if it does
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

   
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
            self.classify_image(file_path)
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
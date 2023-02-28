"""
The Coffee Classifier application is a GUI (Graphical User Interface) designed to classify coffee bean images into one of four roast levels: Green, Light, Medium, or Dark. The application uses a pre-trained deep learning model (located at 'data/final_model.h5') to predict the label for each image. The images should be in .jpg, .jpeg, or .png format and must have a size of 224x224 pixels.

The classify_bean function takes a file path string as input, loads the image at that path, resizes it to 224x224 pixels, converts it to grayscale, and normalizes the pixel values before passing it through the pre-trained model. It returns the predicted label as a string (Green, Light, Medium, or Dark). If the file path is invalid or if the image is not 224x224 pixels, a ValueError is raised.

The AppDemo class inherits from the QWidget class and creates the GUI. The GUI has three labels: photoViewer, pathLabel, and label. photoViewer is a QLabel that displays the image dropped onto the GUI. pathLabel is a QLabel that displays the file path of the image. label is a QLabel that displays the predicted roast level for the image.

The AppDemo class has four methods:

classify_image() takes a file path as input, calls the classify_bean function to predict the roast level of the image, and sets the predicted label in the label QLabel.

set_image() takes a file path as input and sets the image in the photoViewer QLabel.

dragEnterEvent(), dragMoveEvent(), and dropEvent() are methods that allow the GUI to accept image files that are dragged and dropped onto it. When a file is dropped onto the GUI, the set_image() method is called to set the image in the photoViewer QLabel, and the classify_image() method is called to predict the roast level of the image and display it in the label QLabel.

Overall, this application can be used to classify single coffee bean images into one of four roast levels by simply dragging and dropping the image onto the GUI. The application can be modified to classify other types of images as well by training a new model and adjusting the classify_bean() function accordingly.
"""

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
    """
    QLabel subclass for displaying images.

    This class provides a QLabel widget that can display images. It is used to show the
    image dropped onto the application window and set the image in the widget.

    Attributes:
        None

    Methods:
        setPixmap(image): Sets the pixmap of the label to the specified image.
    """
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
    """
    A PyQt5 widget that allows the user to classify the roast level of a coffee bean image by dragging and dropping an image onto the widget.
    """
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
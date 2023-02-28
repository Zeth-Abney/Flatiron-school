"""
This module includes several functions for evaluating and visualizing a machine learning model's performance, specifically for image classification tasks. It includes the following functions:

evaluate_model: This function takes in a Keras model and an ImageDataGenerator object that generates batches of images and their labels, and returns the loss, accuracy, confusion matrix, and classification report of the model's performance. It also returns the prediction and test labels.

viz_training_history: This function visualizes the model's training and validation accuracy and loss as a function of epochs. It takes in the History object that stores the history of the model training, and a title string.

viz_class_balance_comparison: This function takes in two 1D numpy arrays, the true labels and the predicted labels, creates a dataframe of the class balance of each set, and plots the class balance as a stacked barchart. It returns the dataframe used to plot the class balance of the true labels and predictions.

viz_confusion_matrix: This function visualizes a confusion matrix, taking in a numpy array of the confusion matrix and a title string.

Note that this module requires the following libraries: os, numpy, pandas, PIL, matplotlib, sklearn.
"""

import os
import numpy as np
import pandas as pd

from PIL import Image

import matplotlib.pyplot as plt
import matplotlib.colors as colors
cmap = plt.cm.copper

from sklearn.metrics import confusion_matrix, classification_report

## Model Evaluation tools: 

# calculate loss, accuracy, confusion matrix, and create a classification report
def evaluate_model(model,data_generator):
    """
    Evaluates the performance of a Keras model using an ImageDataGenerator object.
    
    Args:
        model (keras.Model): A compiled Keras model object.
        data_generator (keras.preprocessing.image.ImageDataGenerator): A Keras 
            ImageDataGenerator object that generates batches of images and their labels.
    
    Returns:
        - loss, accuracy (tuple of floats)
        - classification report (str)
        - confusion matrix (numpy.ndarray of shape (num_classes, num_classes))
        - prediction and test labels (tuple of 1D numpy arrays)
    
    Raises:
        TypeError: If either `model` or `data_generator` is not a Keras object.
    """
    
    # declare X and y data arrays
    batch_count = len(data_generator)

    X_test_arr, y_test_hot = data_generator[0]

    for i in range(1,batch_count):
        X_batch, y_batch = data_generator[i]

        X_test_arr = np.concatenate((X_test_arr,X_batch),axis=0)
        y_test_hot = np.concatenate((y_test_hot,y_batch),axis=0)

    # insantiate test prediction
    y_pred_hot = np.round(model.predict(X_test_arr))

    y_test = np.argmax(y_test_hot,axis=1)
    y_pred = np.argmax(y_pred_hot,axis=1)

    # evaluate KPIs
    loss, accuracy = model.evaluate(X_test_arr,y_test_hot)

    # calculate the confusion matrix and classification report
    matrix = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test_hot,y_pred_hot)
    
    print("Done!")
    return (np.round(accuracy,4), np.round(loss,2)), report, matrix, (y_test, y_pred)

# visualizes loss and accuracy throughout training epochs
def viz_training_history(model_history,title:str):
    """
    Visualize the model's training and validation accuracy and loss as a function of epochs.

    Parameters:
        model_history : keras.callbacks.History object
            The object that stores the history of the model training.
        suffix : str
            A string suffix that identifies the specific model being visualized.

    Returns:
        None

    Notes:
        This function generates two subplots: one for the accuracy and one for the loss.
        The training data is plotted as a dot while the test data is plotted as a solid line.
    """

    acc = model_history.history['accuracy']
    val_acc = model_history.history['val_accuracy']

    loss = model_history.history['loss']
    val_loss = model_history.history['val_loss']

    epochs = range(len(acc))

    # Create subplots with 1 row and 3 columns
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))

    # Adjust the spacing between the plots
    plt.subplots_adjust(wspace=.1)

    # Plot the accuracy
    ax1.plot(epochs, acc, 'bo', label='Train',c=cmap(0.4))
    ax1.plot(epochs, val_acc, 'b', label='Test',c=cmap(0.6))
    ax1.set_title('Accuracy')
    ax1.legend()

    # Plot the loss
    ax2.plot(epochs, loss, 'bo', label='Train',c=cmap(0.4))
    ax2.plot(epochs, val_loss, 'b', label='Test',c=cmap(0.6))
    ax2.set_title('Loss')
    ax2.legend()

    # Show the plots
    fig.suptitle(title)
    plt.show()

# visualizes the class balance of the true labels and predictions
def viz_class_balance_comparison(labels,title:str):
    """"
    Takes in two 1d arrays, the true labels and the predicted labels
    creates a dataframe of the class balance of each set 
    plots the class balance as a stacked barchart

    Parameters:
        - labels: tuple of two 1d arrays, the true labels and the predicted labels
        - title: str, title of the plot to display

    Returns:
        - balance_comparison_df: pandas dataframe, dataframe used to plot the class balance of the true labels and predictions

    Displays:
        - a stacked barchart of the class balance of the true labels and predictions
    """

    y_test = labels[0]
    y_pred = labels[1]

    # format summary stats as a dictionary
    class_balance_dict = {"Test":[np.count_nonzero(y_test == i) for i in range(4)],
                          "Prediction":[np.count_nonzero(y_pred == i) for i in range(4)]
                          }

    # format dictionary as a dataframe with custom indeces
    balance_comparison_df = pd.DataFrame(class_balance_dict,index=['Green','Light','Medium','Dark'])

    # plot stacked bar chart
    balance_comparison_df.T.plot(kind='barh', stacked=True, color=[cmap(1.0), cmap(0.75), cmap(0.5), cmap(0.25)])

    plt.legend(loc='center right')
    plt.title(title)
    plt.show()

    return balance_comparison_df

# visualizes a confusion matrix
def viz_confusion_matrix(confusion_matrix_array:np.array,title:str):
    """
    Visualizes a confusion matrix as a heatmap using matplotlib.
    Takes in a numpy array that represents the confusion matrix,
    where each row represents the true labels and each column represents the predicted labels.
    The array must have only 4 elements since it is a confusion matrix.
    
    Parameters:
        - confusion_matrix_array : np.array
             A 2D numpy array representing the confusion matrix.
        - title : str
             The title of the plot.
    
    Returns:
        None
    """
    # Confusion matrix as a 2D array
    cm = confusion_matrix_array

    # Normalize the confusion matrix
    cm = np.round(cm/np.sum(cm),2)

    # Create a figure and a subplot
    fig, ax = plt.subplots()

    # Plot the confusion matrix as a heatmap
    im = ax.imshow(cm, cmap='copper',vmin=0,vmax=1)

    # Add labels to the plot
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title(title)

    # Add a colorbar to the plot
    fig.colorbar(im)

    # Set the tick marks for the x and y axes
    ax.set_xticks(np.arange(4))
    ax.set_yticks(np.arange(4))
    ax.set_xticklabels([0, 1, 2, 3])
    ax.set_yticklabels([0, 1, 2, 3])

    # Loop over the data dimensions and create text annotations
    for i in range(4):
        for j in range(4):
            text = ax.text(j, i, f'{cm[i, j]:.2f}', ha='center', va='center', color='w')

    # Show the plot
    plt.show()

## new data preprocessing tools:

def resize_image(im_path:str, new_width:int):
    """
    Resizes a PIL image object while preserving its aspect ratio.

    Args:
        im (PIL.Image): The image to resize.
        new_width (int): The desired width of the resized image.

    Returns:
        PIL.Image: The resized image with the specified width and proportional height.
    """

    im = Image.open(im_path)

    width,height = im.size
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_image = im.resize((new_width,new_height))

    return resized_image

def preprocess_new_image(source_dir:str, target_dir:str,debug_mode=False):
    """
    Preprocesses all the image files in a directory by resizing them to a fixed
    width and saving them as PNG files in a new directory.

    Args:
        source_dir (str): Path to the source directory containing the image files.
        target_dir (str): Path to the target directory where the resized images
                          will be saved.
        debug_mode (bool, optional): If True, the function will only print the new
                                     target file paths without saving the files.
                                     Defaults to False.

    Returns:
        None.

    Raises:
        IOError: If either the source or target directory does not exist.

    Example:
        To preprocess all image files in a directory 'data/train' and save the
        resized images in a new directory 'data/processed/train', use:

        >>> preprocess_new_image('data/train', 'data/processed/train')

        To print the new target file paths without actually saving the files, use:

        >>> preprocess_new_image('data/train', 'data/processed/train', debug_mode=True)

    """
    
    i = 1

    for file in os.listdir(source_dir):
    
        # file path for the current image
        source_file_path = source_dir+'/'+file

        # prepare new target filepath
        sub_dir = source_dir.split('/')[-1]
        new_file_name = sub_dir.split()[-1].lower()+f' ({i}).png'
        target_path = target_dir+'/'+new_file_name
        
        i+=1

        # invoke resize file function
        file_resized = resize_image(source_file_path,224)

        if debug_mode:
            # if debug mode is on (True), only print the new target file path
            print(target_path)

        else:
            # save resized file in the target location
            file_resized.save(target_path)
            print(new_file_name+' saved at: ',target_path)

# list available functions
def toolkit_list():
    """
    Prints a list of all the user-facing functions
    Args:
        None
    Returns:
        None
    """
    mylist = [
              "evaluate_model(model,data_generator)",
              "viz_training_history(model_history,title)",
              "viz_class_balance_comparison(y_test,y_pred)",
              "viz_confusion_matrix(confusion_matrix_array,title)"
             ]

    print(mylist)
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.colors as colors

from sklearn.metrics import confusion_matrix, classification_report


# calculate loss, accuracy, recall, and a confusion matrix array
def evaluate_model_performance(model,data_generator):
    """
    Takes in a keras model object and ImageDataGenerator object
    Converts dataset from generator into a 3D numpy array
    Calcultes key performance indicators (KPIs) 
    Returns recall and loss (tuple of floats), classification report, a confusion matrix (2d array), and the prediction and test labels (tuple of 1d arrays)
    """
    
    # declare X and y data arrays
    batch_count = len(data_generator)

    X_test_arr, y_test_arr = data_generator[0]

    for i in range(batch_count):
        X_batch, y_batch = data_generator[i]

        X_test_arr = np.concatenate((X_test_arr,X_batch),axis=0)
        y_test_arr = np.concatenate((y_test_arr,y_batch),axis=0)

    # insantiate test prediction
    y_pred = np.round(model.predict(X_test_arr))

    # evaluate KPIs
    loss, accuracy, recall = model.evaluate(X_test_arr,y_test_arr)

    # calculate the confusion matrix and classification report
    matrix = confusion_matrix(y_test_arr, y_pred)
    report = classification_report(y_test_arr,y_pred)
    
    print("Done!")
    return (np.round(recall,4), np.round(loss,2)), report, matrix, (y_pred, y_test_arr)

# visualizes recall, loss and accuracy accross throughout training history
def viz_training_history(model_history,recall_num:None):
    """ 
    Visualizes the model's accuracy, loss, and recall as it evolves through training epochs.
    Training data is represented as a dot plot while test data is visualized as a line plot
    Takes two positional arguments:
        - a model history object 
        - a suffix generated by keras as a string (i.e. "_int")
            running this notebook sequentially without rerunning cells where models are compiled should allow for cells wher this function
            is called to be run as is. However if there is an error, check that this parameter is the same suffix as that used in the verbose
            print out from the cell where the relevant model is trained (i.e. some_model_results = some_model.fit()). This suffix is contained
            in memory and is an artifact of what order the model was compiled relative to the others in the active kernal, meaning if the kernal 
            is reset, so are these suffixes.     
    """
    acc = model_history.history['acc']
    val_acc = model_history.history['val_acc']
    loss = model_history.history['loss']
    val_loss = model_history.history['val_loss']
    recall = model_history.history['recall'+recall_num]
    val_recall = model_history.history['val_recall'+recall_num]
    epochs = range(len(acc))

    # Create subplots with 1 row and 3 columns
    fig, (ax3, ax2, ax1) = plt.subplots(1, 3, figsize=(16,4))

    # Adjust the spacing between the plots
    plt.subplots_adjust(wspace=.1)

    # Plot the recall
    ax3.plot(epochs, recall, 'bo', label='Training recall')
    ax3.plot(epochs, val_recall, 'b', label='Test recall')
    ax3.set_title('Training and Test recall')
    ax3.legend()

    # Plot the loss
    ax2.plot(epochs, loss, 'bo', label='Training loss')
    ax2.plot(epochs, val_loss, 'b', label='Test loss')
    ax2.set_title('Training and Test loss')
    ax2.legend()

    # Plot the accuracy
    ax1.plot(epochs, acc, 'bo', label='Training acc')
    ax1.plot(epochs, val_acc, 'b', label='Validation acc')
    ax1.set_title('Training and validation accuracy')
    ax1.legend()

    # Show the plots
    plt.show()

# visualizes the class balance of the true labels and predictions
def viz_class_balance_comparison(y_test,y_pred):
    """
    Takes in two 1d arrays, the true labels and the predicted labels
    creates a dataframe of the class balance of each set 
    plots the class balance as a stacked barchart

    returns the dataframe used to plot therefore...
    displays plot *if* assigned to a variable
    displays plot followed be dataframe if not assigned to a variable
    """

    # get summary stats for test labels
    test_unique, test_counts = np.unique(y_test, return_counts=True)
    pred_unique, pred_counts = np.unique(y_pred, return_counts=True)

    # format summary stats as a dictionary
    balance_comparison_dict = {"Test":test_counts,"Prediction":pred_counts}

    # format dictionary as a dataframe with custom indeces
    balance_comparison_df = pd.DataFrame(balance_comparison_dict,index=["Normal","Pneumonia"])
    
    # plot stacked bar chart
    blues = plt.cm.Blues
    balance_comparison_df.T.plot(kind='barh', stacked=True, color=[blues(0.5), blues(0.4)])
    plt.show()

    return balance_comparison_df

# visualizes a confusion matrix
def viz_confusion_matrix(confusion_matrix_array:np.array):
    """
    Takes in a numpy array (must be 2D, with only 4 elements (i.e. a confusion matrix))
    normalizes each element in the array to be a percentage 
    plots the normalized values as a confusion matrix using matplotlib
    returns no values, uses .show() method to dispaly the figure
    """
    # Confusion matrix as a 2D array
    cm = confusion_matrix_array

    # Normalize the confusion matrix
    cm = np.round(cm/np.sum(cm),2)

    # Create a figure and a subplot
    fig, ax = plt.subplots()

    # Plot the confusion matrix as a heatmap
    im = ax.imshow(cm, cmap='winter',vmin=0,vmax=1)

    # Add labels to the plot
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title('Confusion Matrix')

    # add lines between quadrants for more contrast
    ax.axvline(x=0.5, color='k', linestyle='solid', linewidth=3, alpha=0.5)
    ax.axhline(y=0.5, color='k', linestyle='solid', linewidth=3, alpha=0.5)

    # Add a colorbar to the plot
    fig.colorbar(im)

    # Set the tick marks for the x and y axes
    ax.set_xticks(np.arange(2))
    ax.set_yticks(np.arange(2))
    ax.set_xticklabels([0, 1])
    ax.set_yticklabels([0, 1])

    # Loop over the data dimensions and create text annotations
    for i in range(2):
        for j in range(2):
            text = ax.text(j, i, f'{cm[i, j]:.2f}', ha='center', va='center', color='w')

    # Show the plot
    plt.show()

# list available functions
def toolkit_list():
    mylist = [
              "evaluate_model_performance(model,data_generator)",
              "viz_training_history(model_history,recall_num:None)",
              "viz_class_balance_comparison(y_test,y_pred)",
              "viz_confusion_matrix(confusion_matrix_array:np.array)"
             ]

    print(mylist)
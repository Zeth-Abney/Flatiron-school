import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt
import matplotlib.colors as colors

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report


def dataframe_from_generator(generator,batch_size:16,verbose:True):
    """
    Takes in an ImageDataGenerator object (keras)
    Converts and reshapes data into 2D arrays, then into DataFrames
    Concatenates DataFrames together into a single DataFrame 
    Returns gen_df, a Dataframe containing the entire image dataset in a structured, numerical format. 
    """
    # asign dataset to a concise variable, count of batches in dataset
    data = generator
    batch_count = len(data)

    #instantiate empty dataframe to concatenate later
    gen_df = pd.DataFrame()

    # iterate through however many batches occur in the dataset
    for i in range(batch_count):
        # asign X and y variables to features and labels
        X_batch,y_batch = data[i]

        # make y array vertical
        vertical_y = zip(*[y_batch])
        vertical_y = np.array([list(tuple) for tuple in vertical_y])
        
        # if verbose:
        #     print(f"y batch {i}/{batch_count} now has shape: ",vertical_y.shape)

        # flatten X, so each row in a 2D array represents a single image
        flat_X = X_batch.reshape(batch_size,-1)
        
        # if verbose:
        #     print(f"X batch {i}/{batch_count} now has shape: ",flat_X.shape)

        # convert arrays to dataframes
        y_batch_df = pd.DataFrame(vertical_y, columns=['label'])
        X_batch_df = pd.DataFrame(flat_X)

        # concatenate batch dataframes horizontally 
        batch_df = pd.concat([y_batch_df, X_batch_df], axis=1)

        # concatenate batch dataframe to generator dataframe vertically
        gen_df = pd.concat([gen_df,batch_df],axis=0)

        if verbose:
            print("----------------------------------")
            print(f"\nbatch {i}/{batch_count} complete")

    return gen_df


def evaluate_model_performance(model,data_generator,verbose=True):
    """
    Takes in a keras model object and ImageDataGenerator object
    Samples a batch from the data generator
    Calcultes key performance indicators (KPIs)
    Prints loss and classification_report, and plots a confusion matrix
    If not verbose, returns loss, classification_report and confusion_matrix
    """
    
    # declare evaluation sample
    X_test, y_test = data_generator.next()

    # insantiate test prediction
    y_pred = np.round(model.predict(X_test))

    # evaluate KPIs
    loss, accuracy = model.evaluate(X_test,y_test)

    # calculate the confusion matrix and classification report
    matrix = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test,y_pred)

    # create a ConfusionMatrixDisplay object
    disp = ConfusionMatrixDisplay(matrix)

    # design plot aesthetics
    plot_color_list = ["lightblue","blue","orange","yellow"]
    plot_cmap = colors.ListedColormap(plot_color_list) 
    # plot the confusion matrix, print the classification report
    plt.matshow(matrix,cmap=plot_cmap)

    # Add a color bar to the plot
    plt.colorbar()

    # Add labels to the quadrants
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            plt.text(x=j, y=i, s=matrix[i, j], ha="center", va="center")

    # Add axis labels
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")

    # Display the plot
    print(report)
    plt.show()
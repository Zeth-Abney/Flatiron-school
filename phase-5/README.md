# Project Overview
This project aims to build a convolutional neural network that can classify images of coffee beans into one of four categories representing various stages of the roasting process: raw, light, medium, and dark. The model will take jpeg images of coffee beans as an input, analyze the image using convolutional layers, and make a prediction about the roast stage.

This project is important to pursue because it demonstrates how artificial intelligence (AI) can be used to improve processes and outcomes in the coffee industry. By leveraging the power of machine learning, coffee roasters can achieve greater consistency in their roasts, which can lead to higher quality coffee and increased customer satisfaction. Additionally, this project is just the tip of the iceberg when it comes to the potential for innovation in the coffee industry utilizing AI technology. There are many other applications of machine learning in the coffee industry, such as predicting consumer preferences, optimizing supply chain logistics, and improving the efficiency of coffee farming. As such, this project represents an exciting opportunity to explore the possibilities of AI in the coffee industry and beyond.  

The project can be broken down into the following steps:  
- Collect a dataset of labeled images of coffee beans in the four roast level categories.    
- Preprocess the images (resize, crop, normalize, etc.) to make them suitable for training the model.  
- Iterate over various versions of network architecture, hyperparameters and training protocols.   
- Evaluate the performance of each model version on a test dataset to determine accuracy and other key performance indicators (KPI)  
- Deploy the model to a system that can accept jpeg images as input, classify them, and alert workers when the desired roast is achieved. 

# Business Use Case

This project has the potential to significantly improve the coffee roasting process in terms of quality control, labor efficiency, and profitability. By using a camera positioned above the roasting bin to periodically capture images and analyze the roast level of the beans, the system can help coffee roasters achieve greater consistency in their roasts. This can lead to higher quality coffee and increased customer satisfaction.  

In addition, this system can help reduce waste by alerting workers when the beans are overcooked or undercooked, thereby minimizing the amount of coffee that must be discarded. This reduction in waste can have a significant impact on a roaster's bottom line, as it reduces the cost of materials and increases profitability.  

Furthermore, this system can help workers be more productive by allowing them to focus on other tasks while the roasting process is underway. Since the system can monitor the roasting process and alert workers when the desired roast level is achieved, workers do not need to pay as close attention to each roasting bin. This can free up time and resources that can be directed towards other areas of the business, further increasing efficiency and profitability.
Overall, this project represents a powerful tool for coffee roasters looking to improve their operations and achieve greater success in the highly competitive coffee industry. By utilizing AI technology to improve quality control, reduce waste, and increase labor efficiency, coffee roasters can deliver a better product to their customers and increase their bottom line.

# Data Understanding 
The dataset used in this project comes from kaggle.com and consists of 1200 training images and 400 test images. Each sample is equally distributed between the four classes, with 300 images per class in the training set and 100 images per class in the test set. All the images are of a single coffee bean and are of size 224x224 pixels. The dataset's class labels are (Dark, 0), (Green, 1), (Light, 2), and (Medium, 3). The images were captured using an iPhone 12 mini, which means that the images are of high quality and consistent.
To further test the model and the dataset's limitations, I will also create a small validation dataset using our own iPhone 13 pro camera. This dataset will include images of both single coffee beans, like the training and test data, as well as images of multiple beans. By doing so, I hope to evaluate the model's performance in detecting the stage of the roasting process of both individual and multiple beans.
Overall, I believe that this dataset provides a good representation of the different stages of coffee bean roasting, and I am confident that our model can successfully classify coffee bean images.  

# Data Preparation
To prepare the image data for modeling, I utilized the ImageDataGenerator class from Keras to read in the JPEG files and directly access the image data as matrices. This method makes it easy to load in and preprocess large datasets. The ImageDataGenerator objects were set to normalize the pixel values to a scale of 0-1 using the rescale argument. I also set the color_mode argument to grayscale since I only need to work with a single channel for these images.

Normalizing the pixel values and setting to grayscale are standard practices for image classification tasks. Normalizing the pixel values scales down the pixel values to a range that is better suited for machine learning algorithms, while setting the images to grayscale removes color as a variable in the analysis, simplifying the model's learning process.

# Modeling Methods 

# Evaluation Methods 

# Project Scope and Limitations

# Recomendations and Conclusion

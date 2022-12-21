# Overview
The goal of this project is to develop a convolutional neural network (CNN) designed to view images of chest x-ray scans and classify if the image shows symptoms of pneumonia or not. If succesful, the resulting model would be used to augment medical professionals diagnostic efforts, *not replace them*. This project aims to develop a tool that can be added to the medical proffesionals tool bag and help make diagnosing Pneumonia much speedier. 

# Business Use Case
Pneumonia is a infection of the lung that is quite prominent in the US today despite having some of the best medical care available. Pneumonia is the leading cause of death wordlwide for children under 5 and is the most common cause for hospital admissions in the US, save for pregnancy<sup>[1](https://www.thoracic.org/patients/patient-resources/resources/top-pneumonia-facts.pdf)</sup>.  

It is clear that there is much room for innovation in the way we handle the scourge Pneumonia, however the medical care *system* is notoriously complex and slow to evolve workflows. Instead of reinventing a wheel that would never be fully deployed, it is best to leverage technology that already exists in the diagnostic workflows that capture Pneumonia among other diseases. Due to the ubiquitious use of x-ray technology aroudn pneumonia and other diseases of the chest and torso, a wealth of image data is available that demonstrates quality examples of both healthy (or at least without pneumonia) respiratory tracts and those, in fact, with pneumonia.  

A computer vision based machine learning model (ML), once properly trained and optimized, could easily be folded into the afformentioned existing diagnostic workflow. By partnering with the software providers behind the existing technology used to capture, view and store x-ray data, said ML could easily be incorporated into the software and its *opinion* be provided to the medical profesional at their discretion. So long as clear and concise documentation is provided to the medical profesionals regarding how best to utilize and interpret this new AI feature of their pre-existing software this could potentially expedite the diagnostic timeline and provide the care provider with greater confidence in their own diagnosese.

# Data Overview
This project utilizes a dataset of several thousand chest x-ray images. The primary origin of this dataset come from [Mendeley Data](https://data.mendeley.com/datasets/rscbjbr9sj/2) and it was directly sourced for this project from [Kaggle.com](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) as the kaggle API on the command line. The original kaggle post describes the dataset as follows:

> The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal). Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care. For the analysis of chest x-ray images, all chest radiographs were initially screened for quality control by removing all low quality or unreadable scans. The diagnoses for the images were then graded by two expert physicians before being cleared for training the AI system. In order to account for any grading errors, the evaluation set was also checked by a third expert.

The above description of how the data come pre-split for training, test, and validation and the proportions of these samples are consistent with what is found in the [EDA notebook](eda.ipynb). 

# Data Preparation
As mentioned above the data comes already sampled for training and validation. Additional the originators of the data have already performed quality control and binary class labeling by qualified professionals. Therefore the only data preparations steps left were to prepare the image files to be "readable" to a CNN (utilizing the [Keras](https://keras.io/about/) API available in Python).  

To achieve this I used [ImageDataGenerator](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator) objects for each sample of the split. One key advantage to this method is that this allows the X and y data to be contained in a single variable while still being properly interpreted by other Keras objects (such as a fit function). The generator objects all share the same parameters; the color mode is set to grayscale, reducing unnecessary volume and complexity of the input data, the class mode is set to binary, reflecting the binary classification requirements of this project, images are resized to 150 by 150 pixels, pixel values are rescaled from 0 - 255 to a scale of 0 - 1 in an effert to normalize the data, and the batch size was originally 16 but then reduced to 8 in the interest of the models learning performance. 

For more details on the data and the preprocessing steps take please review the [EDA notebook](eda.ipynb) 

# Modeling Methods
The modeling process, demonstrated in detail in the [Modeling notebook](modeling.ipynb), consisted of first building a baseline model, and then measuring more complex and sophisticated iterations against the initial basline model.  

## Model Architecture
The first major iteration was experimenting with the models architecture itself. This was iterated on later throught the model development process and it was eventually decided on that a relatively simple model archtecture was the best direction to take. 

## Model Training Protocol
The next major iteration was experimenting with more robust training paramets (specifically within .fit() function). Various arrangements of steps per epochs, total number of epochs and validation steps per epoch were all experimented with. Eventually it was discoverd that the model tends to learn extremely fast, so the final model was trained on a relatively small amount of epochs (while also using an early stoppage technique) and a moderate amount of steps per epoch. 

## Network Regularization
The third major phase of model development was experimenting with various regularization techniques. The least effective of which was dropout regularization (dropping out random nodes from certain layers), this technique made the key performance indicators (KPIs) extremely eradic and not obviously converging on any values or approaching any limits (i.e. lots of zig zigs, not a lot of curves). Hoever L2 regularization showed clear benefits and after some experimentation a weight of 0.005 showed to be the most optimal.  

## Optimization Algorithm
The fourth major iteration was experimenting with various optimization algorithms. Up until this point in the project there had been none specified and keras was using whatever default algorithm it assigns (I have so far been unable to find documentation specifying exactly what algorithm that is). After testing three different algorithms, [stochastic gradient descent](https://keras.io/api/optimizers/sgd/), [adaptive momentum estimation](https://keras.io/api/optimizers/adam/), and [adaptive delta](https://keras.io/api/optimizers/adadelta/), it was discoverd that Adam (adaptive moment estimation) was the best algorithm for this model and this project.

## Learning Rate
The fifth and final iteratation of model development was experimenting with various learning rates of the Adam optimization algorithm. After some experimentation it was determined that the optimal learning rate using adam is .01. Examples of each learning rate tested are not available in the modeling notebook, I essentially re-ran the exact same at various learning rates and took note of the KPIs, this was in the interest of the readibility of the notebook. The learning rate parameter can be easiliy located in the "Learning Rate and Early Stopage" section of the modeling notebook and can be easily changed and re-ran if you are so-inclined. 

# Model Evaluation
The key performance indicators utilized for this project are (in order of priority) recall, loss, and accuracy. Accuracy itself is not used for interpretation so much as it helps provide context to the relationship between recall and loss. In the medical industry it is prefered to havea high risk of fals positives and low risk of false negatives, and because of this recall is the main KPI that I sought to improve throughout the project.  

The model -at every iteration- has a tendency to overfit, made evident by results such as 1.0 recall and 7.84 loss, and an accuracy of  0.6. A result like this I interpreted as an indication that the model is correctly classifying all the cases of pneumonia but also miss classifying *a lot* of truly negative cases as positive. 

In essence this is okay for the end user (medical profesionals and care providers) to need to only sift out some false positives by cross examing the models results with other diagnostic tools, however if let go too far this may create and undue burden to the end user have more false positives to sift through than true positives there actually are. 

So my efforts throught the iterative process were focused on analyzing these KPIs and taking further steps to reduce the loss function as much as possible while mainting the recall as close to 1.0 as possible. In the end, the final model yielded a recall at almost exactly 1.0, and accuracy of 63%, and a loss of 0.69. This still has a lot of room for improvement, but compared to the previous evolutions of the model certainly moves in the direction of this projects goals and, more or less, achieves what it was meant to.

# Conclusion 

The model definitely captures almost all the true cases of pneumonia, however at the cast of many false positive "diagnoses". This dynamic is expected, and even par for the course within the medical industry. So despite the need for futher improvement upon the model I consider this project a success and a legitimate proof-of-concept. 

I would be confident in deploying this model to full production, however I believe it is appropriate at this point to release it for beta testing so we can see the real impact of the false positive rate on end user workload, the models diagnostic ability to actually aid the end user, and troubleshoot how to deploy the model to existing softwares. 

Some improvements can be made as is, but it is best to gather more data not only of the x-ray scans themselves but the impact the tool will really have in a production setting. This information is neccessary to perfect this model as a serviceable tool within a timely manner.

The next steps should be to a) find a medical software provider willing to partner with us b) work with said partenr to deploy the tool to a select number of medical offices relevant to this projects goals c) gather data from these participating offices on both the models performance and the tools impact on workflow d) in an ongoing manner, utilize this newly gathered data to further the projects goals and perfect the product.
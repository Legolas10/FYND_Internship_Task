# FYND_Internship_Task 

-Multi-Class Classification Task

APPROACH:
After web scraping data from the URL’s, I saw the data was Imbalanced.The ‘zipper’ class is major class and ‘buckle’ is minor class.
Then I reshaped the images data into an array of 4-dimensions(including all-channels) and normalized all values to common units, and saw that the target variable was imbalanced, so decided to apply SMOTe analysis.

So I used Under Sampling to get 250 images of each class,totaling 250*6=1535 images for Train dataset
Similarly in Test dataset 100 images of each class, 100*6=600 images.
Then I Augmented the images in the datasets to increase the number of images to 4506 images in Train and 1800 images Test dataset.

Since data was small and large training was not feasible for me, I applied TRANSFER LEARNING to get transform the image features, using the VGG16 network.
After processing the images( hist normalizing), I passed the x_train and x_test through a custom-built MLP. 
After training for 30 epochs with an output layer dimension of 6 nodes for 6 classes, I managed to get pretty good results for this multi-class classification problem.

HYPER-PARAMETER SELECTIONS:
After some calculations, I was convinced with the following parameters:
-Input layer nodes=25088
-Optimizer= SGD
-Learning rate=0.0021
- No. of Epochs=30
-Loss= categorical_crossentropy
-Activation func=Relu(hidden layers), Softmax(Output layer)
-Total Trainable Parameters=56,932,950,000

TIME TAKEN:
Time taken to train was 60-80 mins.(on vgg16 + custom ann).

OPTIMIZATIONS:
To avoid Overfitting and to slightly improve the validation accuracy, I added the following:
-Regularizer=L1 (0.00001) for 3 layers
-L2(0.00001) for other 2 layers 
Added one more Hidden layer, total of 6 layers.

FINAL RESULTS:
Mean validation accuracy of 68%
Recall score=0.81


HOW CAN I IMPROVE:
I did not use the given dataset images FULLY. 
If I could have been able to download and use the remaining data, the accuracy could have increased to 70-75%.
Also, a Deeper neural network would have increased the accuracy.

DEMO RUN:
Please, refer the folder for fynd_task.ipynb for codes and explanations. 
Run the classifier.py file to make predictions on any CSV, and get the resulting predicted CSV in the same folder. 

  

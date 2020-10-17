# Multilayer-Perceptron-for-Adult-Income-Classification


There are multiple files in this repository:

The main notebook contains most of the functions (except for verbose_print(), pie_chart(), and binary_bar_chart(), which were outsourced for quick visualization of the raw data and not written by me). These functions are not necessary for my neural network and were simply for data visualization. 

All neccessary functions for the neural network have been defined in the main notebook. The 2 other Python's contain custom classes I created in PyTorch for the Multilayer Perceptron (MLP) model and data loading. 

----- About the project -----

Objective: Train a MLP neural network to make a binary prediction on multiple adults' incomes, based on provided features to train on. 

Problem to Solve: The raw dataset can be accessed through the adult.csv file. Based on all the samples, train the network to predict ">50K" or "<=50K" based on other features. Train the network until a good validation accuracy is obtained. This is defined as anything above 0.8.

Visualize the Data: matplotlib and various print outs was used to visualize the results. 

Choose your own Parameters: 

- Activation Functions: ReLU, Sigmoid, tanh 

- Number of Epochs 

- Learning Rate 

- Random Seed 

- Hidden Layer Size (default set to 64 in model.py) 

- Batch size 

- N (number of batches to run through before printing loss/accuracy)

----- Results -----

- Highest validation accuracy achieved was 0.8316 

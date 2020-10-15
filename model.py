import torch
import torch.nn as nn
import torch.nn.functional as F


class MultiLayerPerceptron(nn.Module):

    def __init__(self, input_size): #input_size should be #features (103)?

        super(MultiLayerPerceptron, self).__init__()

        ######
        # 4.3 YOUR CODE HERE
        self.fc1 = nn.Linear(input_size,64) #layer 1 (hidden) <-- bwn size of input and size of output (8 arbitrary)
        self.fc2 = nn.Linear(64,1) #layer 2 (output) <-- 2 output neurons (high-income or low-income)
        
        ##### Underfitting 
        #self.fc1 = nn.Linear(input_size,1)
        
        ###### Overfitting 
        #self.fc1 = nn.Linear(input_size, 64) #hidden layer 1
        #self.fc2 = nn.Linear(64, 64) #hidden layer 2
        #self.fc3 = nn.Linear(64,64) #hidden layer 3
        #self.fc4 = nn.Linear(64, 1) #output layer                 

    def forward(self, features):

        #pass
        ######

        # 4.3 YOUR CODE HERE
        features1 = F.relu(self.fc1(features)) #relu activation function to first layer
        features2 = torch.sigmoid(self.fc2(features1)) #sigmoid activation function to output layer (so its a 1 or 0)
        
        return features2
        
        ##### Underfitting 
        #feature1 = torch.sigmoid(self.fc1(features))
        #return feature1                  

        ###### Overfitting 
        #features1 = F.relu(self.fc1(features)) #relu activation function to first layer
        #features2 = F.relu(self.fc2(features1)) 
        #features3 = F.relu(self.fc3(features2)) 
        #features4 = torch.sigmoid(self.fc4(features3))            

        #return features4            

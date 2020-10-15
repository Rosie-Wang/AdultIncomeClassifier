import torch.utils.data as data


class AdultDataset(data.Dataset):

    def __init__(self,X, y): #X and Y 

        #pass
        ######
        # 4.1 YOUR CODE HERE
        self.X = X
        self.y = y
        ######

    def __len__(self):
        
        return len(self.X)

    def __getitem__(self, index): #get the (i)th sample 
        #pass
        
        ######
        # 4.1 YOUR CODE HERE
        item = self.X[index,:],self.y[index] #extract (i)th sample row and label for that sample
                
        return item 
        
        ######
        

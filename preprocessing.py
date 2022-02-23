'''
This module contains the preprocessing functions required to scale our dataset.
This module can be used to perform scaling or standardization of dataset. 
'''
from math import sqrt

class MinMax:
    
    def minMaxMatrix(self, data):
        '''
        Min-Max Scaler is used to transform the values of the dataset to a 0-1 range. 
        '''
        minmax = []
        for i in range(len(data[0])):   # Iterating over the columns of the dataset
            col = [row[i] for row in data]          # Saving the column values in a list to find min and max
            col_max = max(col)
            col_min = min(col)
            minmax.append([col_min, col_max])
            
        return minmax
    
    def normalize(self, data, mm):
        '''
        Arguments;
        data: The dataset to transform
        mm: The Min-Max matrix containing the min and max value of all numeric columns
        '''
        for row in data:
            for i in range(len(row)):
                row[i] = (row[i] - mm[i][0] ) / (mm[i][1] - mm[i][0])       # Using the min-max scaling mathematical formula
        
    
    def transform(self, data):
        mm = self.minMaxMatrix(data)
        self.normalize(data, mm )
        return (data)
               



class Standardization:
    '''
    We use this function to convert our data into a normal distribution or a Gaussian Distribution.
    Such a distribution is centered around zero and has standard deviation of 1.
    '''      

    
    def col_means(self,d ):
        means = [ 0 for i in range(len(d[0]))]
        for i in range(len(d[0])):
            col = [row[i] for row in d]
            means[i] = sum(col) / len(col) 
        return means
    
    def col_std(self, d, means):
        
        std = [0 for i in range(len(d[0])) ]
        
        for i in range(len(d[0])):
            variance = sum([pow(row[i]- means[i], 2) for row in d]) / float(len(d)-1)
            std[i] = sqrt (variance)
            
        return std

    def transform(self, data):
        means = self.col_means(data) 
        std = self.col_std(data, means)
        
        for row in data:
            for  i in range(len(row)):
                row[i] = (row[i] - means[i]) / std[i]
                
        return data
    
    
    
        
s = Standardization()

dataset = [[50, 30], [20, 90], [30, 50]]
print(s.transform(dataset))
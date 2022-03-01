'''
In order to train our models we need to split our data into train and test data. This can be done in several ways.
This module implements some of the most commonly used evaluation techniques. 
'''

from math import ceil
from random import randrange
from re import L
from tkinter import E
from turtle import clear

def train_test_split (dataset, split = 0.6):
    '''
    One of the simplest form of sampling is spliting the dataset into two parts for training and testing.
    We use a perecentage of split passed as argument to the function. 
    '''
    train_set = []
    test_set = dataset.copy()
    
    if split <= 1:
        train_size = int(len(test_set) * split)
    else:
        raise ValueError("Invalid split percentage. Requires a value between 0-1") 
    
    while len(train_set) < train_size:
        i = randrange(len(test_set))
        train_set.append(test_set.pop(i))
    
    return train_set, test_set



def cross_validation_split(dataset,folds=2 ):
    '''
    k-fold cross validation split is a technique to sampling the dataset into k groups of equal size.
    It is important that the number of fold is divisible by the number of observation in the dataset or else we
    will have remainder rows.
    '''
    
    train_set = []
    d = dataset.copy()
    
    fold_size = int (len(d) / folds)
    
    for f in range(folds):
        fold = []
        
        while len(fold) < fold_size:        # Loopin until we have the number of sample required in a fold
            i = randrange(len(d))
            fold.append(d.pop(i))
            
        train_set.append(fold)          # Adding the fold to the train set
        
    
    return train_set
    

def stratified_split (dataset, labels, split=.6):
    '''
    It is a form of random sampling that ensure the proportions of class in classification 
    problems is maintained. This is done by dividing each class into a strata and then sampling in the proportion of the
    occurrence.
    '''
    if len(dataset) != len(labels):
        raise ValueError("The features and labels do not have the same number of rows.")
    
    # Getting unique classes in the labels
    strata_label = []
    for label in labels:
        if label not in strata_label:
            strata_label.append(label)
    
    # Finding proportions of class label in dataset
    strata_prop = []
    for i in strata_label:
        strata_size = len([x for x in labels if x == i])
        strata_prop.append(strata_size / len(dataset))
    
    if split <= 1: #Testing for valid split
        train_size = int(len(dataset) * split)
    else:
        raise ValueError("Invalid split percentage. Requires a value between 0-1") 
    

    strata = [[] for x in range(len(strata_label))]
    
    for i in range(len(labels)):
        strata[strata_label.index(labels[i])].append(dataset[i])
    print(strata)
    
    
    train_set = []
    test_set = []
    
    for s in strata:
        
        
        s_train = []
        class_size = int(round (len(s) * split ))
        
        while len(s_train) < class_size:
            index =  randrange(len(s))
            s_train.append(s.pop(index))
            
        train_set.extend(s_train)
        test_set.extend(s)

            
    # print(strata_label)  
    # print (strata_prop)

    
    return train_set, test_set

    
    
    
    
    
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
labels = [0,1,1,0,1,1,0,0,0,0]

print (stratified_split(dataset, labels, 0.6))
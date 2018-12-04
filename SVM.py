import csv
import numpy as np

headers = []
trainData = []
with open("adult.train.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for i, row in enumerate(reader): # each row is a list
        if i!=0:
            trainData.append(row)
        else:
            headers = row

print('Headers : ')
print(headers)
print('\n')
print('Training Data : ')
trainData = np.asarray(trainData)
print(trainData)
print('\n')
print('Testing Data : ')
testData = []
with open("adult.test.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for i, row in enumerate(reader): # each row is a list
        if i!=0:
            testData.append(row)

testData = np.asarray(testData)
print(testData)

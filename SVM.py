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

print(headers)
print(trainData[1:3])
#print(results)

testData = []
with open("adult.test.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for i, row in enumerate(reader): # each row is a list
        if i!=0:
            testData.append(row)

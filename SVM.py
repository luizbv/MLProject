import csv
import numpy as np

headers = []
trainData = []
with open("adult.train.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    header = reader[0]
    for row reader[1:]: # each row is a list
        if i!=0:
            trainData.append(row)
        else:
            headers = row

print(headers)
print(trainData[1][1])
#print(results)

testData = []
with open("adult.test.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        if i!=0:
            testData.append(row)



import csv
import numpy as np
import matplotlib.pyplot as plt

def getLikelikehood(header, yValue):
    return 1

def probability50k(header, label, yValue):
    return 1

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

testData = []
with open("adult.test.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for i, row in enumerate(reader): # each row is a list
        if i!=0:
            testData.append(row)

print('\n')
print('Testing Data : ')
testData = np.asarray(testData)
print(testData)

print('\n\n')
# Average for each feature independently: workclass, education, marital-status, occupation, relationship, race, sex,
# native-country
avgList = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'earnings'][]
avgs =  {}

# creates dictionary, each containing the header as a key with the value as an array of possible characteristics
for i, item in enumerate(trainData.T):
    if headers[i] in avgList:
        avgs[headers[i]] = []
        for info in item:
            if info not in avgs[headers[i]]:
                avgs[headers[i]].append(info)

probs = {}

# creates a dictionary, each containing a header as a key with an array of dictionaries as the values
# these inner dictionaries contain possible headers as keys and probabilities of making 50k or more as values
#for i, key in enumerate(avgs.keys()):
for item in trainData.T:

    if item in avgs.keys():
        probs[item] = []
        for key in avgs.keys()[avgs.keys()==item]:
            probs[item].append(probability50k(item, key, len(trainData.T))})

    else:
        probs[item] = []
        probs[item].append(getLikelihood(item, len(trainData)))

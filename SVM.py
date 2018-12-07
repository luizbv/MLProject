import csv
import numpy as np
import matplotlib.pyplot as plt

def getLikelihood(train, header, yValue):
    return 1

def probability50k(train, header, label, yValue):
    trueSum = 0
    falseSum = 0

    for item in train.T[train.T[0]==header]==label:

        if item == '>50K':
            trueSum += 1

        else:
            falseSum += 1

    return trueSum/(trueSum+falseSum)

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
avgList = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'earnings']
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

    if item[0] in avgs.keys():

        probs[item[0]] = []

        for key in avgs.keys()[avgs.keys()==item[0]]:
            probs[item[0]].append(probability50k(trainData, item[0], key, len(trainData.T)))

    else:
        probs[item[0]] = []
        probs[item[0]].append(getLikelihood(trainData, item[0], len(trainData)))

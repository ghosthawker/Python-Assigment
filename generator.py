#!/usr/bin/python3
import sys, time, os
#PRINT TIME 
sys.stdout = open("output.txt", "w")
print (time.asctime( time.localtime(time.time())))
with open(sys.argv[1], 'r') as f:
    file_contents = [x.split('\t')[2:5] for x in f.readlines()]
    #Set the variables for average and total for cities
total = 0

def printDivider(len=57):
    print('='*57)

for line in file_contents:
    total += float(line[2])    
avg = total/len(line[0])
print("The total sales of", line[0] + " is {0:.2f}".format(total))
categories = set()
for line in file_contents:
    categories.add(line[1])
    noUniqueCategories = len(categories)


if(noUniqueCategories > 3):
    categories = set()
    for line in file_contents:
        categories.add(line[1])
        noUniqueCategories = len(categories)
        avg = round(total / noUniqueCategories, 2)
    print('The avg sale from {0} item categories is: {1:.2f}\n'.format(noUniqueCategories,avg))

    dictionary = {}
    for line in file_contents:
        try:
            dictionary[line[1]] += float(line[2])
        except KeyError:
            dictionary[line[1]] = float(line[2])
    sortDict = (sorted(dictionary, key=dictionary.get))
    print('Top Three Item Categories\n')
    printDivider()

    for k in range(3):
        print('{0:<45}{1:.2f}'.format(sortDict[-k-1], dictionary[sortDict[-k-1]]))
    printDivider()

    print('Bottom Three Item Categories \n')
    printDivider()
    for l in range(3):
        print('{0:<45}{1:.2f}'.format(sortDict[l], dictionary[sortDict[l]]))
    printDivider
else:

    dictionary = {}
    for line in file_contents:
        try:
            dictionary[line[1]] = float(line[2])
        except KeyError:
            dictionary[line[1]] += value
    sortDict = (sorted(dictionary, key=dictionary.get))
    printDivider()
    print('The average Sale from {0} Item Categories: {1:2f}\n'.format(noUniqueCategories, avg))
    printDivider()
    for k in range(3):
        print('{0:<45}{1:.2f}'.format(sortDict[k], dictionary[sortDict[k]]))
printDivider()


f.close()
print (time.asctime( time.localtime(time.time())))
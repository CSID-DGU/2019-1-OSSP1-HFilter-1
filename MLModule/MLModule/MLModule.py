#Copyright 2019. Jeongwon Her. All rights reserved.
#Last modified 19/04/14

import numpy as np

# Make Label by txt
# Return List
def makeLabel(path, ignore=1):

    # Dictionary
    labels = {}

    # Open file
    try:
        file = open(path, 'r', encoding='utf8')
    except:
        print("Invalid path")
        return np.array([])
    
    # Read file
    while True:
        line = file.readline()
        if not line:
            break

        # Remove Newline character
        line = line.replace("\n", "")

        # Jump name and id
        if "검색 결과" in line or "Likes" in line:
            continue

        if line not in labels:
            # it's first appearance
            labels[line] = 1
        else:
            # Add 1 using the line as a key
            labels[line] += 1
    # End of while

    # Close file
    file.close

    # Sort
    sortLabels = sorted(labels.items(), key=lambda x: x[1], reverse=True)

    # Slice
    for i in range(0, len(sortLabels)):
        if((int)(sortLabels[i][1])<ignore): break
    sliced = np.array(sortLabels[:i])

    return sliced
# End of makeLabel


# Draw Histogram with numpyArray
# Args = ["title", "xLabel", "yLabel", lowVal]
def makeHistogram(listArray, args=None):

    # Histogram lib
    import matplotlib.pyplot as plt

    # Making Histogram...
    # Font setting
    plt.rc('font', family="Malgun Gothic");

    # Make title, xLabel, yLabel
    if args == None or len(args) != 4:
        args = []
        args.append("title")
        args.append("xLabel")
        args.append("yLabel")
        args.append(0)
    # Histogram tilte
    plt.title(args[0])
    # x, y label name
    plt.xlabel(args[1])
    plt.ylabel(args[2])

    # Make x y list
    x=listArray[:,0].tolist()
    y=listArray[:,1].astype(float)
    # Insert data
    plt.bar(x, y)
    # Set range
    plt.ylim((int)(args[3])-2, y[0]+2)
    plt.show()
# End of makeHistogram


# Liner learning model
def learningModule(listA, listB, ignore, learnCnt=10, hst=False):

    # Get labels
    originA=makeLabel(listA, ignore)
    originB=makeLabel(listB, ignore)
    if originA.size == 0 or originB.size == 0:
        return 1

    # Make different set of labels and init weight
    weightA = {}
    weightB = {}
    labelA = np.array(np.setdiff1d(originA[:,0], originB[:,0]))
    for i in range(0,labelA.size):
        weightA[labelA[i]]=1.0
    labelB = np.array(np.setdiff1d(originB[:,0], originA[:,0]))
    for i in range(0,labelB.size):
        weightB[labelB[i]]=1.0

    # Make individual data(dictionary)
    indivA=makeIndiv(listA)
    indivB=makeIndiv(listB)
    if len(indivA) == 0 or len(indivB) == 0:
        return 1

    # Learning
    for cnt in range(0,learnCnt):

        # Wrong guesses union
        # Positive False, Negative True
        pf, nt = {}, {}

        # In positive list
        for i in range(0, len(indivA)):
            tmp = np.array((list)(indivA.values())[i])
            intsec = np.intersect1d(tmp, np.array((list)(weightA.keys())))
            weight = 0
            # Calculate weight
            for j in range(0, intsec.size):
                weight += weightA[intsec[j]]
            # When positive false
            # Threshold 1.0
            if weight < 1.0:
                for j in range(0, tmp.size):
                    if tmp[j] not in pf:
                        # it's first appearance
                        pf[tmp[j]] = 1
                    else:
                        # Add 1 using the indivA[i][j] as a key
                        pf[tmp[j]] += 1
        # End of for

        # Weight adjustment
        for i in range(0, len(pf)):
            if list(pf.keys())[i] in weightA:
                weightA[(list)(pf.keys())[i]] = (float)(list(pf.values())[i]) / ignore + (float)(weightA[list(pf.keys())[i]])
            else:
                weightA[(list)(pf.keys())[i]] = (float)(list(pf.values())[i]) / ignore

        # In negative list
        for i in range(0, len(indivB)):
            tmp = np.array((list)(indivB.values())[i])
            intsec = np.intersect1d(tmp, np.array((list)(weightA.keys())))
            weight = 0
            # Calculate weight
            for j in range(0, intsec.size):
                weight += weightA[intsec[j]]
            # When negative true
            # Threshold 1.0
            if weight > 1.0:
                for j in range(0, tmp.size):
                    if tmp[j] not in nt:
                        # it's first appearance
                        nt[tmp[j]] = 1
                    else:
                        # Add 1 using the indivB[i][j] as a key
                        nt[tmp[j]] += 1
        # End of for

        # Weight adjustment
        for i in range(0, len(nt)):
            if list(nt.keys())[i] in weightA:
                weightA[(list)(nt.keys())[i]] = -(float)(list(nt.values())[i]) / 10 + (float)(weightA[list(nt.keys())[i]])
            else:
                weightA[(list)(nt.keys())[i]] = -(float)(list(nt.values())[i]) / 10
    # End of learning

    # Sort
    weightAList = sorted(weightA.items(), key=lambda x: x[1], reverse=True)

    # Print Learning module(weight)
    import FileRW
    outPath = FileRW.makePathStr(listA, 'module.txt')
    FileRW.writeFileByList(outPath, np.array(weightAList))

    # Make Histogram positive prediction(weight)
    if hst:
        # Weight by id dictionary
        print={}
        # In positive list
        for i in range(0, len(indivA)):
            tmp = np.array((list)(indivA.values())[i])
            intsec = np.intersect1d(tmp, np.array((list)(weightA.keys())))
            weight = 0
            for j in range(0, intsec.size):
                weight += weightA[intsec[j]]
            print[(list)(indivA.keys())[i]]=weight
        printList = sorted(print.items(), key=lambda x: x[1], reverse=True)
        makeHistogram(np.array(printList))

    return 0
# End of learningModule


# Make Individual data with txt
# Return Dictionary
def makeIndiv(path):

    # Open file
    try:
        file = open(path, 'r', encoding='utf8')
    except:
        print("Wrong Path.")
        return {}
    
    # Read file
    line = file.readline()

    # Dictionary
    indiv={}

    while line:
        # Jump name
        if "검색 결과" in line:
            line = file.readline()
            continue

        # Add tuple
        # It has 3type: "검색 결과", "Likes", data
        if "Likes" in line:
            # Get id
            id = line[:15]

            # List
            data = []

            # Read data
            while True:
                line = file.readline()
                # Jump if not data
                if not line or "검색 결과" in line or "Likes" in line:
                    break
                data.append(line.replace("\n", ""))
            # End of while

            # Not insert Empty element
            if len(data) != 0:
                indiv[id]=np.array(data)
        # End of if

    # End of while

    # Close file
    file.close

    return indiv
# End of MakeIndiv


# Determination by learned weight
def dtrHuman(hList, wDiction):
    intsec = np.intersect1d(np.array(hList), np.array((list)(wDiction.keys())))
    weight = 0
    for i in range(0, intsec.size):
        weight += wDiction[intsec[i]]

    return weight
# End of dtrHuman


# Make Module with txt
# Return Dictionary
def makeModule(path):
        # Dictionary
    weight = {}

    # Open file
    try:
        file = open(path, 'r', encoding='utf8')
    except:
        print("Invalid path")
        return {}
    
    # Read file
    while True:
        line = file.readline()
        if not line:
            break

        # Remove Newline character
        line = line.replace(" \n", "")

        # Parsing
        ptr=line.rfind(' ')

        # Add dictionary
        weight[line[:ptr]] = (float)(line[ptr+1:])
    # End of while

    # Close file
    file.close

    return weight
# End of makeModule



#                               #
# Lagacy codes in old version   #
#                               #

# !! Legacy code !!
# Read txt in path and sort intersection in descending order
# Write txt
# Return output path
def makeLabelWrite(path):
    # Dictionary
    labels = {}

    # Open file
    try:
        file = open(path, 'r', encoding='utf8')
    except:
        print("잘못된 경로입니다.")
        return None
    
    # Read file
    while True:
        line = file.readline()
        if not line:
            break

        # Remove Newline character
        line = line.replace("\n", "")

        # Jump name and id
        if "검색 결과" in line or "Likes" in line:
            continue

        if line not in labels:
            # it's first appearance
            labels[line] = 1
        else:
            # Add 1 using the line as a key
            labels[line] += 1
    # End of while

    # Make output path
    name=path
    while name.find('\\') != -1:
        name = name[name.find('\\')+1:]
    name=name[:name.find('.')]
    outPath = path[:path.find(name)] + name + "output.txt"

    # Open output file
    output = open( outPath, 'w', encoding='utf8')
    if output is None:
        print("경로 생성 실패.")
        return None

    # Sort
    sortLabels = sorted(labels.items(), key=lambda x: x[1], reverse=True)

    # Write
    for i in range(0, len(sortLabels)):
        output.write(str(sortLabels[i][0]) + " " + str(sortLabels[i][1]) + "\n")

    file.close
    output.close
    return outPath
# End of makeLabelByTxt

# !! Legacy code !!
# Draw Histogram with sorted txt
def makeHistogramByTxt(path, xLabel="items", yLabel="nums", ignore=10):
    # Histogram lib
    import matplotlib.pyplot as plt 
    #import NamGyunSWTeam as hst

    # Open file
    file = open(path, 'r', encoding='utf8')
    if file is None:
        print("잘못된 경로입니다.")
        return None
    
    # Dictionary
    labels = {}

    # Read file
    while True:
        line = file.readline()
        if not line:
            break

        # Remove Newline character
        line = line.replace(" \n", "")

        # Parsing
        ptr=line.rfind(' ')

        # Remove low values
        if (int)(line[ptr+1:]) < ignore:
            break

        # Add dictionary
        labels[line[:ptr]] = (int)(line[ptr+1:])
    # End of while

    # Close file
    file.close

    # Make name of graph
    title=path
    while title.find('\\') != -1:
        title = title[title.find('\\')+1:]
    title = title[:len(title)-10]

    #hst.fontSettings()

    # Making Histogram...
    # Font setting
    plt.rc('font', family="Malgun Gothic");
    # Histogram tilte
    plt.title(title)
    # x, y label name
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    # Make x, y
    x = (list)(labels.keys())
    y = (list)(labels.values())
    # Insert data
    plt.bar(x, y)
    # Set range
    plt.ylim(ignore-2, y[0]+2)
    plt.show()
# End of makeHistogramByTxt

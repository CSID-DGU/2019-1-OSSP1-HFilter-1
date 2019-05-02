#Copyright 2019.  Jeongwon Her.  All rights reserved.
#Last modified 19/04/14
import numpy as np

# Make Label by txt
# Return List
def makeLabel(path, ignore=1):
    """path:input path  ignore:label will be ignored under integer"""

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
        if((int)(sortLabels[i][1]) < ignore): break
    sliced = np.array(sortLabels[:i])

    return sliced
# End of makeLabel


# Draw Histogram with numpyArray
def makeHistogram(listArray, args=None):
    """listArray:nd array   args:["title", "xLabel", "yLabel", lowVal]"""

    # Histogram lib
    import matplotlib.pyplot as plt

    # Making Histogram...
    # Font setting
    plt.rc('font', family="Malgun Gothic")

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
    x = listArray[:,0].tolist()
    y = listArray[:,1].astype(float)
    # Insert data
    plt.bar(x, y)
    # Set range
    plt.ylim((int)(args[3]) - 2, y[0] + 2)
    plt.show()
# End of makeHistogram


# Liner learning model
def learningModule(listA, listB, ignore, learnCnt=10, hst=False):

    # Get labels
    originA = makeLabel(listA, ignore)
    if originA.size == 0:
        return 1
    originB = makeLabel(listB, ignore)
    if originB.size == 0:
        return 1

    # Make different set of labels and init weight
    weightA = {}
    labelA = np.array(np.setdiff1d(originA[:,0], originB[:,0]))
    for i in range(0,labelA.size):
        weightA[labelA[i]] = 1.0

    # Make individual data(dictionary)
    indivA = makeIndiv(listA)
    if len(indivA) == 0:
        return 1
    indivB = makeIndiv(listB)
    if len(indivB) == 0:
        return 1

    # Learning
    for cnt in range(0,learnCnt):
        gap = ignore
        if gap<1: gap=1
        
        print("Learning " + str(cnt + 1), end='')

        # Wrong guesses union
        # Positive False, Negative True
        pf, nt = {}, {}
        pfSum, ntSum = 0, 0

        # In positive list
        for i in range(0, len(indivA)):
            aList = list(indivA.values())[i]
            
            # Calculate weight
            weight = 0
            for j in range(0, len(aList)):
                if aList[j] in weightA:
                    weight += weightA[aList[j]]

            # When positive false
            # Threshold 1.0
            if weight < 1.0:
                pfSum+=1
                for j in range(0, len(aList)):
                    if aList[j] not in pf:
                        # it's first appearance
                        pf[aList[j]] = 1
                    else:
                        # Add 1 using the aList[j] as a key
                        pf[aList[j]] += 1
        # End of for

        pfKeys=(list)(pf.keys())
        pfVals=(list)(pf.values())

        # Weight adjustment
        for i in range(0, len(pf)):
            if pfKeys[i] in weightA:
                weightA[pfKeys[i]] = (float)(pfVals[i]) / gap + (float)(weightA[pfKeys[i]])
            else:
                weightA[pfKeys[i]] = (float)(pfVals[i]) / gap

            if weightA[pfKeys[i]]==0:
                del weightA[pfKeys[i]]

        # In negative list
        for i in range(0, len(indivB)):
            bList = list(indivB.values())[i]

            # Calculate weight
            weight = 0
            for j in range(0, len(bList)):
                if bList[j] in weightA:
                    weight += weightA[bList[j]]
            # When negative true
            # Threshold 1.0
            if weight > 1.0:
                ntSum+=1
                for j in range(0, len(bList)):
                    if bList[j] not in nt:
                        # it's first appearance
                        nt[bList[j]] = 1
                    else:
                        # Add 1 using the bList[j] as a key
                        nt[bList[j]] += 1
        # End of for

        ntKeys=(list)(nt.keys())
        ntVals=(list)(nt.values())

        # Weight adjustment
        for i in range(0, len(nt)):
            if ntKeys[i] in weightA:
                weightA[ntKeys[i]] = -(float)(ntVals[i]) / gap + (float)(weightA[ntKeys[i]])
            else:
                weightA[ntKeys[i]] = -(float)(ntVals[i]) / gap

            if weightA[ntKeys[i]]==0:
                del weightA[ntKeys[i]]


        print(" P-Gess:" + str(pfSum * 100 / len(indivA)) + "% N-Gess:" + str(ntSum * 100 / len(indivB)) + "%")
        # 100% correct
        if pfSum == 0 and ntSum==0:
            break
    # End of learning

    # Sort
    weightAList = sorted(weightA.items(), key=lambda x: x[1], reverse=True)

    # Print Learning module(weight)
    import FileRW
    outPath = FileRW.makePathStr(listA, 'module.txt')
    FileRW.writeFileByList(outPath, np.array(weightAList))

    
    # Weight by id dictionary
    prDic = {}
    sum = 0

    # In positive list
    for i in range(0, len(indivA)):
        tmp = (list)(indivA.values())[i]

        weight = 0
        for j in range(0, len(tmp)):
            if tmp[j] in weightA:
                weight += weightA[tmp[j]]
        prDic[(list)(indivA.keys())[i]] = weight
        if weight > 0:
            sum+=1

    printList = sorted(prDic.items(), key=lambda x: x[1], reverse=True)
    print(str(sum / len(indivA) * 100) + "% 정확도")

    # Make Histogram positive prediction(weight)
    if hst:
        makeHistogram(np.array(printList))

    return 0
# End of learningModule


# Make Individual data with txt
# Return Dictionary
def makeIndiv(path):
    """path:input path"""
    # Open file
    try:
        file = open(path, 'r', encoding='utf8')
    except:
        print("Wrong Path.")
        return {}
    
    # Read file
    line = file.readline()

    # Dictionary
    indiv = {}

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
                indiv[id] = np.array(data)
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
        ptr = line.rfind(' ')

        # Add dictionary
        weight[line[:ptr]] = (float)(line[ptr + 1:])
    # End of while

    # Close file
    file.close

    return weight
# End of makeModule



#                               #
# Lagacy codes in old version   #
#                               #

# !!  Legacy code !!
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
    outPath = path[:path.rfind('.')] + "output.txt"

    # Open output file
    output = open(outPath, 'w', encoding='utf8')
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

# !!  Legacy code !!
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
        ptr = line.rfind(' ')

        # Remove low values
        if (int)(line[ptr + 1:]) < ignore:
            break

        # Add dictionary
        labels[line[:ptr]] = (int)(line[ptr + 1:])
    # End of while

    # Close file
    file.close

    # Make name of graph
    title = path
    while title.find('\\') != -1:
        title = title[title.find('\\') + 1:]
    title = title[:len(title) - 10]
  
    #hst.fontSettings()

    # Making Histogram...
    # Font setting
    plt.rc('font', family="Malgun Gothic")
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
    plt.ylim(ignore - 2, y[0] + 2)
    plt.show()
# End of makeHistogramByTxt

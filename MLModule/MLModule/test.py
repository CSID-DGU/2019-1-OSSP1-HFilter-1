# This is Test code
# Do not set this as a startup file
import MLModule
import FileRW
import numpy as np

def testcode1():

    wDic = MLModule.makeModule("C:\\Users\\hacel\\source\\repos\\HFilter\\SampleData\\남자module.txt")

    hList = ["동국대학교", "동국대학교 대나무숲", "인사이트 패션", "오늘 뭐 먹지?", "편한식사-Esiksa", "서울 갈데없다고 누가 그랬냐"]

    w = MLModule.dtrHuman(hList, wDic)

    print("남자일 확률 : " + (str)(w))

    wDic = MLModule.makeModule("C:\\Users\\hacel\\source\\repos\\HFilter\\SampleData\\여자module.txt")

    w = MLModule.dtrHuman(hList, wDic)

    print("여자일 확률 : " + (str)(w))

def testcode2():

    path = input("Enter the path : ")

    import FileRW
    outfile = open(FileRW.makePathStr(path,"data.txt"), 'w', encoding='utf8')

    # Error
    if outfile is None:
        print("Invalid path")
        return

    for i in range(0,20):
        for j in range(0,2):
            if i < 10:
                fstr = "0" + str(i)
            else:
                fstr = str(i)

            infile = open(FileRW.makePathStr(path, fstr + str(j) + "0021.txt"), 'r', encoding='utf8')

            outfile.write(infile.read())


def testcode3():
     path = input("Enter the path : ")
     MLModule.makeLabelWrite(path)


def testcode4(path, n):
    label = MLModule.makeLabel(path)

    indiv = MLModule.makeIndiv(path)

    indivA, indivB = {}, {}

    print("make half")
    for i in range(0, len(indiv)):
        if label[n][0] in list(indiv.values())[i]:
            indivA[list(indiv.keys())[i]] = list(indiv.values())[i]
        else:
            indivB[list(indiv.keys())[i]] = list(indiv.values())[i]

    labelA, labelB = {}, {}

    print("calcul A")
    for i in range(0, len(indivA)):
        for j in range(0, len(list(indivA.values())[i])):
            if list(indivA.values())[i][j] in labelA:
                labelA[list(indivA.values())[i][j]] +=1
            else:
                labelA[list(indivA.values())[i][j]] = 1

    print("calcul B")
    for i in range(0, len(indivB)):
        for j in range(0, len(list(indivB.values())[i])):
            if list(indivB.values())[i][j] in labelB:
                labelB[list(indivB.values())[i][j]] +=1
            else:
                labelB[list(indivB.values())[i][j]] = 1

    print("sorting")
    sortA = sorted(labelA.items(), key=lambda x: x[1], reverse=True)
    sortB = sorted(labelB.items(), key=lambda x: x[1], reverse=True)

    # Make txt
    import re
    name=re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]',"",label[n][0])
    FileRW.writeFileByList(FileRW.makePathStr(path), label)
    FileRW.writeFileByList(FileRW.makePathStr(path,name+"A.txt"), sortA)
    FileRW.writeFileByList(FileRW.makePathStr(path,name+"B.txt"), sortB)
    return FileRW.makePathStr(path, name)


def testcode5(path, length=7253, ignore=10):
    # Dictionary
    sortA, sortB = {}, {}

    # Open file
    try:
        file = open(path + "A.txt", 'r', encoding='utf8')
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
        sortA[line[:ptr]] = (int)(line[ptr + 1:])
    # End of while

    # Close file
    file.close

        # Open file
    try:
        file = open(path + "B.txt", 'r', encoding='utf8')
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
        sortB[line[:ptr]] = (int)(line[ptr + 1:])
    # End of while

    # Close file
    file.close

    #print("slicing")
    ## Slice
    #for i in range(0, len(sortA)):
    #    if((int)(sortA[i][1]) < ignore): break
    #slicedA = np.array(sortA[:i])

    #for i in range(0, len(sortB)):
    #    if((int)(sortB[i][1]) < ignore): break
    #slicedB = np.array(sortB[:i])

    print("differ")
    onlyA = {}
    valA=list(sortA.values())
    keyA=list(sortA.keys())
    for i in range(1,len(sortA)):
        if valA[i]>ignore:
            if keyA[i] in sortB:
                if valA[i]/valA[0]/2 > sortB[keyA[i]]/(length-valA[0]):
                    onlyA[keyA[i]] = valA[i]
            else:
                onlyA[keyA[i]] = valA[i]
        else: break

    #diffB = np.array(np.setdiff1d(slicedB[:,0],slicedA[:,0]))
    #onlyB = {}
    #for i in range(0, diffB.size):
    #    for s in slicedB:
    #        if diffB[i] in s:
    #            onlyB[diffB[i]] = int(s[1])

    A = sorted(onlyA.items(), key=lambda x: x[1], reverse=True)
    #B = sorted(onlyB.items(), key=lambda x: x[1], reverse=True)

    #MLModule.makeHistogram(np.array(A))
    FileRW.writeFileByList(path+"dif.txt", np.array(A))
    #MLModule.makeHistogram(np.array(B))


for i in range(0, 100):
    print(str(i)+"번째")
    path=testcode4("C:\\Users\\hacel\\source\\repos\\HFilter\\Data\\tmp\\data.txt", i)
    testcode5(path, 10)
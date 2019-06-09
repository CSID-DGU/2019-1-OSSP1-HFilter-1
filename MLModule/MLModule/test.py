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

def testcode6(rawPath, ignore, clust):
    # dictionary
    label={}

    ## Open label file
    ## same meaning as below(raw data)
    ##label = MLModule.makeLabel(path)
    #try:
    #    file = open(path, encoding='utf8')
    #except:
    #    print("Invalid path")
    #    return {}
    
    ## Read file
    #while True:
    #    line = file.readline()
    #    if not line:
    #        break

    #    # Remove Newline character
    #    line = line.replace(" \n", "")

    #    # Parsing
    #    ptr = line.rfind(' ')

    #    if (int)(line[ptr + 1:])<ignore:
    #        break

    #    # Add dictionary
    #    label[line[:ptr]] = (int)(line[ptr + 1:])
    ## End of while

    ## Close file
    #file.close

    # merge raw and save
    label = MLModule.makeLabel(rawPath, ignore)
    FileRW.writeFileByList(FileRW.makePathStr(rawPath), label)

    labels = label[:,0]

    indiv = MLModule.makeIndiv(rawPath)
    
    indivKey = list(indiv.keys())
    indivVal = list(indiv.values())

    # list
    indivVec = [[0] * labels.size for _ in range(len(indivVal))]

    # make individual vector
    for i in range(0, len(indivVal)):
        for j in range(0, labels.size):
            if labels[j] in indivVal[i]:
                indivVec[i][j] = 1

    import scipy.cluster.hierarchy as hac
    import matplotlib.pyplot as plt

    a = np.array(indivVec)

    z = hac.linkage(a, method='complete')
    knee = np.diff(z[::-1, 2], 2)
    # 
    #knee[knee.argmax()] = 0
    numClust = clust
    if numClust < 2:
        numClust = 2

    fig, axes11=plt.subplots(1,1)
    axes11.plot(range(1, len(z)+1), z[::-1, 2])
    axes11.plot(range(2, len(z)), knee)
    axes11.text(knee.argmax(), z[::-1, 2][knee.argmax()-1], 'possible\n<- knee point')
    m = '\n(method: {})'.format('complete')
    plt.setp(axes11, title='Screeplot{}'.format(m), xlabel='partition',
                ylabel='{}\ncluster distance'.format(m))
    plt.show()

    part = hac.fcluster(z, numClust, 'maxclust')
    
    output={}
    for i in range(1, numClust+1):
        output[i]=open(FileRW.makePathStr(rawPath, str(i)+".txt"), 'w', encoding='utf8')

    for i in range(0, len(part)):
        output[part[i]].write(indivKey[i]+" likes\n")
        for j in range(0, len(indivVal[i])):
            output[part[i]].write(indivVal[i][j]+"\n")

    for i in range(1, numClust+1):
        output[i].close

    return numClust

    # hieriachy
    #fig, axes23 = plt.subplots(2, 3)

    #for method, axes in zip(['single', 'complete'], axes23):
    #    z = hac.linkage(a, method=method)

    #    # Plotting
    #    axes[0].plot(range(1, len(z)+1), z[::-1, 2])
    #    knee = np.diff(z[::-1, 2], 2)
    #    axes[0].plot(range(2, len(z)), knee)

    #    num_clust1 = knee.argmax() + 2
    #    knee[knee.argmax()] = 0
    #    num_clust2 = knee.argmax() + 2

    #    axes[0].text(num_clust1, z[::-1, 2][num_clust1-1], 'possible\n<- knee point')

    #    part1 = hac.fcluster(z, num_clust1, 'maxclust')
    #    part2 = hac.fcluster(z, num_clust2, 'maxclust')

    #    clr = ['#2200CC' ,'#D9007E' ,'#FF6600' ,'#FFCC00' ,'#ACE600' ,'#0099CC' ,
    #    '#8900CC' ,'#FF0000' ,'#FF9900' ,'#FFFF00' ,'#00CC01' ,'#0055CC']

    #    for part, ax in zip([part1, part2], axes[1:]):
    #        for cluster in set(part):
                
    #            if cluster>len(clr)-1:
    #                clrtmp='#0055CC'
    #            else:
    #                clrtmp=clr[cluster]

    #            ax.scatter(a[part == cluster, 0], a[part == cluster, 1], 
    #                       color=clrtmp)

    #    m = '\n(method: {})'.format(method)
    #    plt.setp(axes[0], title='Screeplot{}'.format(m), xlabel='partition',
    #             ylabel='{}\ncluster distance'.format(m))
    #    plt.setp(axes[1], title='{} Clusters'.format(num_clust1))
    #    plt.setp(axes[2], title='{} Clusters'.format(num_clust2))

    #plt.tight_layout()
    #plt.show()


    # kmeans
    #whitened = whiten(indivVec)

    ## Find 2 clusters in the data
    #codebook, distortion = kmeans(whitened, 2)
    ## Plot whitened data and cluster centers in red
    #plt.scatter(whitened[:, 0], whitened[:, 1])
    #plt.scatter(codebook[:, 0], codebook[:, 1], c='r')
    #plt.show()

def hash(text):
    import hashlib
    sha512=hashlib.sha512()
    sha512.update(text.encode('utf-8'))
    out=sha512.hexdigest()
    print(out)

def testcode7():
    path = input("Enter the file name or path : ")

    # Open file
    file = open(path, 'r', encoding='utf8')
    if file is None:
        print("잘못된 경로입니다.")
        return None
    
    # Dictionary
    labels = {}

    # Near List
    NList = []

    # Read file
    while True:
        line = file.readline()
        if not line:
            break

        # Remove Newline character
        line = line.replace(" \n", "")

        # Parsing
        ptr = line.rfind(' ')

        ## Remove low values
        #if (int)(line[ptr + 1:]) < ignore:
        #    break

        # Add dictionary
        labels[line[:ptr]] = []
    # End of while

    # Close file
    file.close


    cnt=0
    #compare0
    for i in range(0,2):
        path = input("Enter male/female path : ")
        # Open file
        try:
            file = open(path, 'r', encoding='utf8')
        except:
            continue
        if file is None:
            file.close
            continue

        cnt+=1
        Ncnt=0
        NSList=[]
        # Read file
        while True:
            line = file.readline()
            if not line:
                break

            # Remove Newline character
            line = line.replace(" \n", "")

            # Parsing
            ptr = line.rfind(' ')

            ## Remove low values
            #if (int)(line[ptr + 1:]) < ignore:
            #    break

            # Add dictionary
            if line[:ptr] not in labels:
                labels[line[:ptr]]=[]
                for j in range(0,cnt):
                    labels[line[:ptr]].append(0)
            labels[line[:ptr]].append(float(line[ptr + 1:]))

            if float(line[ptr + 1:])>0 and Ncnt<11:
                Ncnt+=1
                NSList.append(line[:ptr])
        # End of while

        NList.append(NSList)
        keys=list(labels.keys())
        for i in range(0, len(keys)):
            if len(labels[keys[i]])!=cnt+1:
                labels[keys[i]].append(0)

        # Close file
        file.close
    # End of for
    
    # compare 1
    path = input("Enter the file path : ")
    for i in range(1, 27):
        # Open file
        try:
            file = open(path+str(i)+"module.txt", 'r', encoding='utf8')
        except:
            continue
        if file is None:
            file.close
            continue

        cnt+=1
        Ncnt=0
        NSList=[]
        # Read file
        while True:
            line = file.readline()
            if not line:
                break

            # Remove Newline character
            line = line.replace(" \n", "")

            # Parsing
            ptr = line.rfind(' ')

            ## Remove low values
            #if (int)(line[ptr + 1:]) < ignore:
            #    break

            # Add dictionary
            if line[:ptr] not in labels:
                labels[line[:ptr]]=[]
                for j in range(0,cnt):
                    labels[line[:ptr]].append(0)
            labels[line[:ptr]].append(float(line[ptr + 1:]))

            if float(line[ptr + 1:])>0 and Ncnt<11:
                Ncnt+=1
                NSList.append(line[:ptr])
        # End of while

        NList.append(NSList)
        keys=list(labels.keys())
        for i in range(0, len(keys)):
            if len(labels[keys[i]])!=cnt+1:
                labels[keys[i]].append(0)

        # Close file
        file.close
    # End of for

    # compare2
    path = input("Enter the file path : ")
    for i in range(0, 22):
        # Open file
        try:
            file = open(path+str(i)+"module.txt", 'r', encoding='utf8')
        except:
            continue
        if file is None:
            file.close
            continue

        cnt+=1
        Ncnt=0
        NSList=[]
        # Read file
        while True:
            line = file.readline()
            if not line:
                break

            # Remove Newline character
            line = line.replace(" \n", "")

            # Parsing
            ptr = line.rfind(' ')

            ## Remove low values
            #if (int)(line[ptr + 1:]) < ignore:
            #    break

            # Add dictionary
            if line[:ptr] not in labels:
                labels[line[:ptr]]=[]
                for j in range(0,cnt):
                    labels[line[:ptr]].append(0)

            labels[line[:ptr]].append(float(line[ptr + 1:]))

            if float(line[ptr + 1:])>0 and Ncnt<11:
                Ncnt+=1
                NSList.append(line[:ptr])
        # End of while

        NList.append(NSList)
        keys=list(labels.keys())
        for i in range(0, len(keys)):
            if len(labels[keys[i]])!=cnt+1:
                labels[keys[i]].append(0)

        # Close file
        file.close
    # End of for

    # save
    path = input("Enter the out path : ")
    # Open output file
    output = open(path, 'w', encoding='utf8')
    # Error
    if output is None:
        print("Invalid path")
        return 1

    import hashlib
    sha256=hashlib.sha256()
    keys=list(labels.keys())
    # Write
    for i in range(0, len(keys)):
        key=keys[i]
        sha256.update(key.encode('utf-8'))
        output.write(key+":")
        for j in range(0, len(labels[keys[i]])):
            tmp=f"{labels[keys[i]][j]:3.1f}"
            output.write(tmp + " ")
        output.write("\n")

    output.close

    # save 2
    path = input("Enter the out path")
    # Open output file
    output = open(path, 'w', encoding='utf8')
    # Error
    if output is None:
        print("Invalid path")
        return 1

    for i in range(0, len(NList)):
        for j in range(0, len(NList[i])):
            output.write(NList[i][j]+">")
        output.write("\n")
    output.close

def testcode8():
    path = input("Enter the file path : ")
    file = open(path, 'r', encoding='utf8')
    out = open(FileRW.makePathStr(path), 'w', encoding='utf8')

    while True:
        line = file.readline()
        if not line:
            break

        # Parsing
        ptr = line.rfind(":")

        ## Remove low values
        #if (int)(line[ptr + 1:]) < ignore:
        #    break

        out.write(line[:ptr]+"\n")
    # End of while

    file.close()
    out.close()

if __name__ == '__main__':
    #testcode8()
    testcode7()

    #import numpy as np
    #from scipy.cluster.vq import vq, kmeans, whiten
    #import matplotlib.pyplot as plt
    #path="C:\\Users\\hacel\\source\\repos\\HFilter\\Data\\test\\k26\\data"

    #num=testcode6(path+".txt", 6)

    #for i in range(1,26+1):
    #    label = MLModule.makeLabel(path+str(i)+".txt")
    #    FileRW.writeFileByList(path+str(i)+"output.txt", label)

    #path = []
    #path.append(input("Insert Base Path : "))
    #path.append(input("Insert Compare Path : "))

    ## Learning
    #for i in range(1,25):
    #    err=MLModule.learningModule(path[0], path[1]+str(i)+".txt", 10, 100, 0, False)
    #    if err==-1:
    #        print(path[1]+str(i)+".txt Error")

    #path = input("Enter the file name or path : ")
    #label = MLModule.makeLabel(path, 0)
    #import FileRW as file
    #file.writeFileByList(file.makePathStr(path), label)

    #hash("test string")

#!!! test codes !!!#
#for i in range(0, 100):
#    print(str(i)+"번째")
#    path=testcode4("C:\\Users\\hacel\\source\\repos\\HFilter\\Data\\tmp\\data.txt", i)
#    testcode5(path, 10)

#Copyright 2019.  Jeongwon Her.  All rights reserved.
#This document was written by Jeongwon Her

#!!! 다변량 정규분포에 대한 수학적 설명 !!!#
# 다변량 정규분포를 랜덤으로 만든다

#mean = [0, 0]
# n차원의 벡터 (2)개의 평균

#cov = [[1, 0], [0, 1]]
# n차원의 벡터 (2)개의 공분산 (2)^2개
# sxy=1N∑i=1N(xi−x¯)(yi−y¯)을 설정해줌

#x = np.random.multivariate_normal(mean, cov, 2)
# 주어진 평균과 공분산으로 랜덤한 n차원 벡터(2)개 생성
#print(x)

#print(np.cov(x[0,:],x[1,:]))
# 공분산을 확인해 볼 수 있다

#list((x[0,0,:] - mean) < 0.6)
#[True, True]
# 표준편차는 대략 0.6의 두배이다

# 예제
#a = np.random.multivariate_normal([0, 0, 0], [[4, 1, 2], [1, 5, 3], [2, 3, 7]], 3)
#print(a)
# 공분산은 0보다 큰 양수임을 유의하자
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.multivariate_normal.html

#!!! 표준 편차로 나누어 단위 분산 계산 !!!#
# 머신 러닝을 할때 이상값에 의한 신경망 조정이 크게 일어나지 않도록
# whitening을 해 주는 것(평균 0 분산 1로 재조정)
# https://en.wikipedia.org/wiki/Whitening_transformation

# 예제
#features  = np.array([[1.9, 2.3, 1.7],
#                      [1.5, 2.5, 2.2],
#                      [0.8, 0.6, 1.7,]])
#whiten(features)
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.whiten.html#scipy.cluster.vq.whiten

#import numpy as np
#import scipy.cluster.hierarchy as hac
#import matplotlib.pyplot as plt

#a = np.array([[0.1,   2.5],
#              [1.5,   .4 ],
#              [0.3,   1  ],
#              [1  ,   .8 ],
#              [0.5,   0  ],
#              [0  ,   0.5],
#              [0.5,   0.5],
#              [2.7,   2  ],
#              [2.2,   3.1],
#              [3  ,   2  ],
#              [3.2,   1.3]])

#fig, axes23 = plt.subplots(2, 3)
## 2*3그래프

#for method, axes in zip(['single', 'complete'], axes23):
#    z = hac.linkage(a, method=method)
    ## i번째 원소와 비교해서 거리를 구함 i*4 행렬
    ## i,0과 i,1을 비교, 거리를 i,2에 i,3은 원래 관측횟수
    ## 이전값을 반복해서 구함
    ## linkage method single or complete
    ## single은 nearest point algorithm
    ## complete는 farthest
    ## average, weighted centroid median ward...
    ## https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage

#    # Plotting
#    axes[0].plot(range(1, len(z)+1), z[::-1, 2])
#    knee = np.diff(z[::-1, 2], 2)
#    axes[0].plot(range(2, len(z)), knee)

#    num_clust1 = knee.argmax() + 2
#    knee[knee.argmax()] = 0
#    num_clust2 = knee.argmax() + 2
    ## get posible max and next max clust

#    axes[0].text(num_clust1, z[::-1, 2][num_clust1-1], 'possible\n<- knee point')

#    part1 = hac.fcluster(z, num_clust1, 'maxclust')
#    part2 = hac.fcluster(z, num_clust2, 'maxclust')
    ## hieriarchy find

#    clr = ['#2200CC' ,'#D9007E' ,'#FF6600' ,'#FFCC00' ,'#ACE600' ,'#0099CC' ,
#    '#8900CC' ,'#FF0000' ,'#FF9900' ,'#FFFF00' ,'#00CC01' ,'#0055CC']

#    for part, ax in zip([part1, part2], axes[1:]):
#        for cluster in set(part):
#            ax.scatter(a[part == cluster, 0], a[part == cluster, 1], 
#                       color=clr[cluster])

#    m = '\n(method: {})'.format(method)
#    plt.setp(axes[0], title='Screeplot{}'.format(m), xlabel='partition',
#             ylabel='{}\ncluster distance'.format(m))
#    plt.setp(axes[1], title='{} Clusters'.format(num_clust1))
#    plt.setp(axes[2], title='{} Clusters'.format(num_clust2))

#plt.tight_layout()
#plt.show()
## https://stackoverflow.com/questions/21638130/tutorial-for-scipy-cluster-hierarchy
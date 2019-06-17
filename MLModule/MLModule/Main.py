#Copyright 2019.  Jeongwon Her.  All rights reserved.
import MLModule
import FileRW as file

# ReleaseState .  Week Month Date
VERSION = 0.090606
# Threshold
ignore = 10
# Machine Learning Histogram
MLHst = False
# Machine Learning Count
MLCnt = 100
# Compression rate
Cmp = 0

def sltUtil():
    print(">Util")
    select = input("Histogram[1] MakeLabel[2] Return[0] :")

    if select=="0":
        return

    elif select=="1":
        path = input("Enter the raw path : ")

        # Get sorted labels
        labels = MLModule.makeLabel(path, ignore)
        if labels.size == 0:
            print("Path Error!")
            return

        outPath = file.makePathStr(path)

        # File write and Error detect
        if file.writeFileByList(outPath, labels) != 0:
            print("Write Error!")
            return
    
        # Make Histogram
        MLModule.makeHistogram(labels, ["그래프", path[path.rfind('\\') + 1:path.rfind('.')], "좋아요 수", ignore])

    elif select=="2":
        path = input("Enter the file name or path : ")
        rng = int(input("Enter the number(0 to path) : "))

        if rng<0:
            print("Wrong Input")
            return
        elif rng==0:
            label = MLModule.makeLabel(path, ignore)
            file.writeFileByList(file.makePathStr(path), label)
        else:
            for i in range(1,rng+1):
                label = MLModule.makeLabel(path+str(i)+".txt")
                file.writeFileByList(path+str(i)+"output.txt", label)

    else:
        print("Wrong Input")
        return

    return
# End of sltHistogram;

def sltMLLearning():
    print(">Machine Learning")
    select = input("Make Module[1] Filter[2] Hierarchy[3] Return[0] :")

    if select == "0":
        return

    elif select == "1":
        # Get path
        path = []
        path.append(input("Insert Base Path : "))
        path.append(input("Insert Compare Path : "))

        # Learning
        err = MLModule.learningModule(path[0], path[1], ignore, MLCnt, Cmp, MLHst)

        if err==-1:
            print("Path Error")

    elif select == "2":
        # Get module path
        path = input("Enter the module path : ")
        wDic = MLModule.makeModule(path)
        if len(wDic) == 0:
            print("Wrong Input")
            return

        # Get human path
        path = input("Enter a human to filter : ")
        tmp = MLModule.makeIndiv(path)
        hList = (list)(tmp.values())
        if len(hList) == 0:
            print("Nothing to filter")
            return

        w = MLModule.dtrHuman(hList, wDic)
        print("해당될 확률 : " + (str)(w))

    elif select == "3":
        # Get raw path
        path = input("Enter the raw path : ")
        clust = int(input("Enter the number of clust : "))
        MLModule.makeClust(path, ignore, clust, MLHst)

    else:
        print("Wrong Input")
        return

    return
# End of sltMLLearning

def sltSetting():
    print(">Settings")
    select = input("Threshold[1] MLHistogram[2] MLCount[3] Compression[4] Return[0] :")
        
    if select == "0":
        return

    elif select == "1":
        global ignore
        newinput = (int)(input("Insert Threshold(" + str(ignore) + ") : "))
        if newinput < 1:
            print("Threashold must bigger than 1")
            return
        ignore = newinput

    elif select == "2":
        global MLHst
        MLHstStr = input("Make ML Hisogram?(" + str(MLHst) + ") [T/F] :")
        if MLHstStr == "T":
            MLHst = True
        elif MLHstStr == "F":
            MLHst = False
        else:
            print("Wrong Input")
            return

    elif select == "3":
        global MLCnt
        newinput = (int)(input("Insert Machine Learning Frequency(" + str(MLCnt) + ") : "))
        if newinput < 1:
            print("Wrong Input")
            return
        MLCnt = newinput

    elif select == "4":
        global Cmp
        newinput = (float)(input("Insert Compression rate(" + str(Cmp) +") : "))
        Cmp = newinput

    else:
        print("Wrong Input")
        return

    return
# End of sltSetting

# main
if __name__ == '__main__':
    print("#Copyright 2019. Jeongwon Her. All rights reserved.")
    print("VERSION : " + (str)(VERSION))
    while True:
        select = input("Util[1] MachineLearning[2] Settings[3] Exit[0] :")

        # Exit
        if select == "0":
            print(">Exit")
            break

        # Histogram
        elif select == "1":
            sltUtil()

        # Machine Learning
        elif select == "2":
            sltMLLearning()

        # Settings
        elif select == "3":
            sltSetting()

        # Error
        else:
            print("Wrong Input")

        print()
    # End of while
# End of main
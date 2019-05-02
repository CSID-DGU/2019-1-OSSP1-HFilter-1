#Copyright 2019.  Jeongwon Her.  All rights reserved.
import MLModule
import FileRW as file

# ReleaseState .  Week Month Date
VERSION = 0.040420
# Threshold
ignore = 10
# Machine Learning Histogram
MLHst = False
# Machine Learning Count
MLCnt = 10

# main
def main():
    print("#Copyright 2019. Jeongwon Her. All rights reserved.")
    print("VERSION : " + (str)(VERSION))
    while True:
        select = input("Histogram[1] Machine Learning[2] Settings[3] Exit[0] :")

        # Exit
        if select == "0":
            print(">Exit")
            break

        # Histogram
        elif select == "1":
            sltHistogram()

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
def sltHistogram():
    print(">Histogram")
    path = input("Enter the path : ")

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
# End of sltHistogram;
def sltMLLearning():
    print(">Machine Learning")
    select = input("Make Module[1] Filter[2] Return[0] :")

    if select == "0":
        return
    elif select == "1":
        # Get path
        path = []
        path.append(input("Insert Base Path : "))
        path.append(input("Insert Compare Path : "))

        # Learning
        MLModule.learningModule(path[0], path[1], ignore, MLCnt, MLHst)
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
    else:
        print("Wrong Input")
        return

# End of sltMLLearning
def sltSetting():
    print(">Settings")
    select = input("Threshold[1] MLHistogram[2] MLCount[3] Return[0] :")
        
    if select == "0":
        return

    elif select == "1":
        newinput = (int)(input("Insert Threshold : "))
        if newinput < 1:
            print("Threashold must bigger than 1")
            return
        global ignore
        ignore = newinput

    elif select == "2":
        MLHstStr = input("Make ML Hisogram? [T/F] :")
        global MLHst
        if MLHstStr == "T":
            MLHst = True
        elif MLHstStr == "F":
            MLHst = False
        else:
            print("Wrong Input")
            return

    elif select == "3":
        newinput = (int)(input("Insert Machine Learning Frequency : "))
        if newinput < 1:
            print("Wrong Input")
            return
        global MLCnt
        MLCnt = newinput

    else:
        print("Wrong Input")
        return
# End of sltSetting
main()
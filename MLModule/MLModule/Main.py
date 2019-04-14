#Copyright 2019. Jeongwon Her. All rights reserved.

import MLModule
import FileRW as file

# Main

# ReleaseState . Week Month Date
VERSION = 0.030414
# Threshold
ignore = 10
# Machine Learning Histogram
MLHst = False
# Machine Learning Count
MLCnt = 10

print("#Copyright 2019. Jeongwon Her. All rights reserved.")
print("VERSION : " + (str)(VERSION))
while True:
    select = input("Histogram[1] Machine Learning[2] Settings[3] Exit[0] :")

    # Exit
    if select=="0":
        print(">Exit")
        break

    # Histogram
    elif select=="1":
        print(">Histogram")
        path = input("Enter the path : ")

        # Get sorted labels
        labels = MLModule.makeLabel(path, ignore)
        if labels.size == 0:
            print("Path Error!")
            continue

        outPath = file.makePathStr(path)

        # File write and Error detect
        if file.writeFileByList(outPath, labels) != 0:
            print("Write Error!")
            continue

        # Make Histogram
        MLModule.makeHistogram(labels, ["그래프", "남자", "좋아요 수", ignore])

    # Machine Learning
    elif select=="2":
        print(">Machine Learning")
        path=[]
        path.append(input("Insert Base Path : "))
        path.append(input("Insert Compare Path : "))
        MLModule.learningModule(path[0], path[1], ignore, MLCnt, MLHst)

    # Settings
    elif select=="3":
        print(">Settings")
        select=input("Threshold[1] MLHistogram[2] MLCount[3] Return[0] :")
        
        if select == "0":
            continue
        elif select == "1":
            ignore = input("Insert Threshold : ")
        elif select == "2":
            MLHstStr = input("Make ML Hisogram? [T/F] :")
            if MLHstStr == "T":
                MLHst=True
            elif MLHstStr == "F":
                MLHst=False
            else:
                print("Wrong Input")
                continue
        elif select == "3":
            MLCount=input("Insert Machine Learning Frequency : ")
        else:
            print("Wrong Input")
            continue

    # Error
    else:
        print("Wrong Input")
#End of while

input("Press any key to continue...")

# End of Main
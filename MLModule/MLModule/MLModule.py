#Copyright 2019. Jeongwon Her. All rights reserved.

# Read txt in path and sort intersection in descending order
# Return output path
def makeLabelByTxt(path):
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
#End of makeLabelByTxt

import matplotlib.pyplot as plt #그래프 그려줌
import NamGyunSWTeam as hst

def makeHistogram(path, xLabel="items", yLabel="nums", ignore=10):
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
        line = line.replace("\n", "")

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

    hst.fontSettings()

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    x = (list)(labels.keys())
    y = (list)(labels.values())
    plt.bar(x, y)
    plt.ylim(ignore-2, y[0]+2)
    plt.show()
# End of makeHistogram


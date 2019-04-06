#Copyright 2019. Jeongwon Her. All rights reserved.

def makeLabelByTxt(path):
    Labels = {}
    # Open file
    file = open(path, 'r', encoding='utf8')
    if file is None:
        print("잘못된 경로입니다.")
        return None
    
    # Read file
    while True:
        line = file.readline()
        line = line.replace("\n", "")

        if not line:
            break
        if "검색 결과" in line or "Likes" in line:
            continue

        if line not in Labels:
            Labels[line] = 1
        else:
            Labels[line] += 1

    # Make output path
    name=path
    while name.find('\\') != -1:
        name = name[name.find('\\')+1:]
    name=name[:name.find('.')]
    #print(name)
    output = open( path[:path.find(name)] + name + "output.txt", 'w', encoding='utf8')

    # Sort
    if output is None:
        print("결과 없음.")
        return None
    sortLabels = sorted(Labels.items(), key=lambda x: x[1], reverse=True)

    # Write
    for i in range(0, len(sortLabels)):
        output.write(str(sortLabels[i]) + "\n")
#End of makeLabelByTxt

path = input("경로를 입력하세요 : ")

makeLabelByTxt(path)


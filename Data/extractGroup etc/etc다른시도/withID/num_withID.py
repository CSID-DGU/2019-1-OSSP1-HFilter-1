
# coding: utf-8

# In[ ]:


##Copyright 2019. All rights reserved.
#OSSP in Dongguk University
#2019-1-OSSP1-HFilter-1

get_ipython().run_line_magic('matplotlib', 'inline')
import sys
from matplotlib import pyplot as plt 
from matplotlib import font_manager, rc

# Draw barChart
# 명 뺴고, ID 빼고
def barChart_except_IDkorean(path):
    # Open file
    file = open(path, 'r', encoding='utf8')
    if file is None:
        print("잘못된 경로입니다.")
        return None
    
    # Dictionary
    label = {}
    
    index = 0
    # Read file
    while True:
        line = file.readline()
        if not line:
            break

        # ID는 무시
        if "  ID" in line:
            continue
        
        # "명"은 뺴야함
        line = line.replace("명", "")
        
        # enter 위치
        ptr_enter = line.find('\n')

        # 뒤에서 부터 찾는 빈칸, key와 value값으로 나눌 것이다.
        ptr_division=line.rfind(' ')
        
        # 오늘은 뭐먹지? 38명 있으면 "오늘은 뭐먹지?"만 추출한다.
        nameOfKey = line[:ptr_division]

        # 오늘은 뭐먹지? 38명 있으면 38만 추출한다.
        numOfKey = int(line[ptr_division+1:ptr_enter])
        
        # 내림차순이므로 10미만이면 끝낸다.
        # 후에 그래프에 너무 작은 수까지 포함하면 양이 너무 많아 오류가 생긴다.
        if numOfKey < 10:
            break
        
        # ex) {0: [오늘은 뭐먹지?, 38], 1: [하이마트, 17], ...}
        label[index] = [nameOfKey, numOfKey]
        index += 1
    # End of while

    # Close file
    file.close

    # ex) C:\Users\현상엽\Downloads\동국대학교\3학년 1학기\공개sw프로젝트\머신러닝_프로젝트\남자.txt
    title=path
    while title.find('\\') != -1:
        title = title[title.find('\\')+1:] # 남자.txt
    title = title[:title.find('.')] # 남자
    title = title + "_historgram"

    # Making Histogram
    # 한글이 깨지기에 폰트를 바꾸어준다.
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    plt.rc('font', family=font_name)
    # Histogram title
    plt.title(title)
    # x, y label name
    plt.xlabel("Page_index")
    plt.ylabel("Num")
    # x축 이름과 y축 이름 설정
    x_index = list(label.keys()) #Page_index
    # Page_name은 각 label[index][0]에 존재한다.
    x_name = []
    y_num = []
    for i in range(0, index):
        y_num.append(label[i][1])
        x_name.append(label[i][0])
        
    for i in range(0, index):
        print(str(x_index[i]) + ": " + x_name[i])

    # bar차트를 그린다 (pie(), hist() 등 여러 차트가 있다.)
    plt.bar(x_index, y_num, width=0.7, color="blue")
    #y축 최소값과 최대값을 정해주자.
    #위에서 10미만은 체크하지 않았고 내림차순이므로 최대값이 y[0]
    #보기 좋게 y의 limit값을 정해주자 (범위)
    plt.ylim([5, y_num[0]+5])
    plt.show()
    return None
# End



# path가 남자고 path2가 여자임
def merge_file_union(path, path2):
    
    # ex) C:\Users\현상엽\Downloads\동국대학교\3학년 1학기\공개sw프로젝트\머신러닝_프로젝트\남자.txt
    name=path
    while name.find('\\') != -1:
        name = name[name.find('\\')+1:] # 남자.txt
    name=name[:name.find('.')] # 남자
    
    # ex) C:\Users\현상엽\Downloads\동국대학교\3학년 1학기\공개sw프로젝트\머신러닝_프로젝트\여자.txt
    name2=path2
    while name2.find('\\') != -1:
        name2 = name2[name2.find('\\')+1:] # 여자.txt
    name2=name2[:name2.find('.')] # 여자
    
    # C:\Users\현상엽\Downloads\동국대학교\3학년 1학기\공개sw프로젝트\머신러닝_프로젝트\남자_여자_merge.txt
    outPath = path[:path.find(name)] + name + "_" + name2 + "_union.txt"
    
    # Open output file
    output = open( outPath, 'w', encoding='utf8')
    if output is None:
        print("경로 생성 실패.")
        return None
    
    #남녀 파일 합칠거야
    try:
        file_1 = open(path, 'r', encoding='utf8')
        file_2 = open(path2, 'r', encoding='utf8')
    except:
        print("잘못된 경로입니다.")
        return None
    
    output.write("남자목록차례_OSSP\n")
    while True:
        line = file_1.readline()
        if not line:
            break
        output.write(line)
    
    output.write("\n\n성별바뀜\n\n")
    output.write("여자목록차례_OSSP\n")
    
    while True:
        line = file_2.readline()
        if not line:
            break
        output.write(line)
    
    file_1.close
    file_2.close
    output.close
    return outPath
# End of merge_file_union


# ID 추가
# Read txt in path and sort intersection in descending order
# Return output path
def makeLabelByTxt_withID(path):
        
    # Dictionary
    labels = {}

    # Open file
    try:
        file = open(path, 'r', encoding='utf8')
    except:
        print("잘못된 경로입니다.")
        return None
    
    personID = ""
    personSex = ""
    # Read file
    while True:
        line = file.readline()
        if not line:
            break
        
       # Remove Newline character
        line = line.replace("\n", "")
        
        if "남자목록차례_OSSP" in line:
            personSex = "남자"
            continue
        
        if "여자목록차례_OSSP" in line:
            personSex = "여자"
            continue

        # Jump name and id
        if "검색 결과" in line:
            continue
        
        if "Likes" in line:
            personID = line[:line.find('의')]
            continue

        if line not in labels:
            # it's first appearance
            labels[line] = [1, personSex, personID]
        else:
            # Add 1 using the line as a key
            # ex) { "page" : [2, ID_1, ID_2]}
            labels[line][0] += 1
            labels[line].append(personSex)
            labels[line].append(personID)
    # End of while
    

    # Make output path
    
    # ex) C:\Users\현상엽\Downloads\동국대학교\3학년 1학기\공개sw프로젝트\머신러닝_프로젝트\남자.txt
    name=path
    while name.find('\\') != -1:
        name = name[name.find('\\')+1:] # 남자.txt
    name=name[:name.find('.')] # 남자
    # C:\Users\현상엽\Downloads\동국대학교\3학년 1학기\공개sw프로젝트\머신러닝_프로젝트\남자output.txt
    outPath = path[:path.find(name)] + name + "output_withID.txt"

    # Open output file
    output = open( outPath, 'w', encoding='utf8')
    if output is None:
        print("경로 생성 실패.")
        return None

    # Sort
    # ex) labels.items() = [(key, value), (key, value), ...]
    sortLabels = sorted(labels.items(), key=lambda x: x[1][0], reverse=True)

    # Write
    for i in range(0, len(sortLabels)):
        output.write(str(sortLabels[i][0]) + " " + str(sortLabels[i][1][0]) + "명\n")
        # 사람수 성별 Id 성별 Id .... 무조건 홀수개
        for j in range(1, int((len(sortLabels[i][1])+1)/2)):
            output.write("  ID "+ str(j) + ": " + str(sortLabels[i][1][2*j-1]) + " " + str(sortLabels[i][1][2*j]) + "\n")

    file.close
    output.close
    return outPath
# 끝


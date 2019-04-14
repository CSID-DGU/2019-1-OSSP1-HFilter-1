##Copyright 2019. All rights reserved.
#OSSP in Dongguk University
#2019-1-OSSP1-HFilter-1

# coding: utf-8

# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
import sys

# Draw Histogram with sorted txt
def makeHistogram_sub_IDkorean(path, xLabel="items", yLabel="nums", ignore=10):
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
        line = line.replace("\n", "")
        
      ######  
        # ID는 무시
        if "  ID" in line:
            continue
            
        # "명"은 뺴야함
        line = line.replace("명", "")
      ######  
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
# End of makeHistogram



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
# End of makeLabelByTxt




# Main
path_men = input("남자파일 경로 입력하세요 : ")
path_women = input("여자파일 경로 입력하세요 : ")
path_union = merge_file_union(path_men, path_women)

# ID와 함께 구합니다.
path_men = makeLabelByTxt_withID(path_men)
path_women = makeLabelByTxt_withID(path_women)
path_union =makeLabelByTxt_withID(path_union)

# Error
if path_men == None or path_women == None or path_union == None:
    sys.exit(1)

select = input("히스토그램을 그립니까?(Yes/No) ")

if select=="예" or select=="Yes" or select=="yes"    or select=="1" or select=="o" or select=="ok":
    makeHistogram_sub_IDkorean(path_men, "페이지", "좋아요")
    makeHistogram_sub_IDkorean(path_women, "페이지", "좋아요")
    makeHistogram_sub_IDkorean(path_union, "페이지", "좋아요")

# End of Main



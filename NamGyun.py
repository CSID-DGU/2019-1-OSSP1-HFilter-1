import matplotlib.pyplot as plt #그래프 그려줌
import matplotlib.font_manager as fm
import numpy as np #수학 함수
#남자 좋아요 수를 넣을 딕셔너리
menLikesCnt ={} 
#남자 딕셔너리 키 저장할 리스트
menKeysList=[]   
#남자 딕셔너리 벨류값을 저장할 리스트
menValuesList=[] 
#남자 히스토그램 키
menHistKeys=[]
#남자 히스토그램 값
menHistValues=[]

#히스토그램 한글 깨짐방지  전역설정,맑은글씨체
path = 'C:/Windows/Fonts/malgun.ttf'

font_name = fm.FontProperties(fname=path, size=50).get_name()

plt.rc('font', family=font_name)


print('폰트 사이즈size : ',plt.rcParams['font.size'] )
 

print('폰트 글꼴(family) : ', plt.rcParams['font.family'])







#여자 좋아요 수를 넣을 딕셔너리
womenLikesCnt ={} 
#히스토그램 2명이상만 띄우기 위한 변수
histCnt=0
#print("남자 좋아요 불러올 경로 입력 :")
#route = input()  #경로 입력
#print("남자 좋아요 저장할 경로 입력 :")
#route2 = input() #저장항 경로
#cp949 코덱으로 인코딩 된 파일 UTF8로 인코딩
f = open("C:\여자.txt",'r',encoding='UTF8') 
#cp949 코덱으로 인코딩 된 파일 UTF8로 인코딩
f2 =open("C:\\Users\\hacel\\OneDrive\\Desktop\\변환2.txt",'w',encoding='UTF8')
#파일을 읽어 딕셔너리에 키와 값을 저장
while True :
    line = f.readline()
    line=line.replace("\n","") ##줄바꿈 제거
    if not line : break
    #사람의 이름 건너뜀(좋아요한 페이지만을 넣기위해)
    if "검색 결과" in line :  
        continue
    #유저 id 건너뜀 (좋아요한 페이지만을 넣기우해)
    elif "Likes" in line :    
        continue
    #처음 나오는좋아요 페이지라면
    if line not in menLikesCnt : 
        #좋아요페이지를 키로하며 1을값으로 갖는 딕셔너리 쌍 추가
        menLikesCnt[line] =1  
        menKeysList.append(line)
        #menLikesCnt의 벨류값을 menKeyList에 추가 어차피1이기때문에 1을 넣음
        menValuesList.append(1)
    else :
        #앞에서 나왔던 좋아요 페이지라면 그 좋아요 페이지를 키값으로하여 값을 1 증가
        menLikesCnt[line]+=1
        
for i in range(0,len(menKeysList)) :
#menValuesList에 딕셔너리에 들어가있던 값들을 순차적으로 저장
    menValuesList[i] = menLikesCnt[menKeysList[i]]
#명수가 많은순서대로정렬
for k in range(0,len(menKeysList)-1) :
    for j in range(0,len(menKeysList) -1 ) :
        #내림차순 정렬
        if menValuesList[j] < menValuesList[j+1] :
            #menKeysList(좋아요 페이지의이름을 내림차순 정렬)
            tmp = menKeysList[j]
            menKeysList[j] = menKeysList[j+1]
            menKeysList[j+1] = tmp
            #menValuesList(좋아요 페이지를 몇명이 했는지 명수를 저장한 리스트 내림차순정렬)
            tmp = menValuesList[j]
            menValuesList[j] = menValuesList[j+1]
            menValuesList[j+1] = tmp
            
for i in range(0,len(menKeysList)) : 
    #리스트의 길이만큼 반복
    #딕셔너리의 키값과 벨류값을 파일에 씀 키와 벨류값사이 띄어쓰기 3번
    #딕셔너리의 키값들을 리스트에 넣고 리스트를 순차적으로 호출하면서 리스트의값을 키로하여
    #딕셔너리의 값들을 호출해 결과적으로 딕셔너리의 키와 벨류값을 메모장에 저장
    f2.write(str(menKeysList[i]) +"   " + str(menValuesList[i]) + "명\n") 

    
#히스토그램 영역

#내림차순이므로 menValuesList가 1이 나오면 종료
for i in range(0,len(menValuesList)) :
    if menValuesList[i] ==10 :
        histCnt = i-1
        break

#2이상의 값만 따로 옮겨줌
for i in range(0,histCnt+1) :
    menHistKeys.append(menKeysList[i])
    menHistValues.append(menValuesList[i])
    
    
    
    
    
print(menKeysList)
print(menValuesList)

#히스토그램 제목
plt.title("남자")
#히스토그램 x축
plt.xlabel("좋아요 페이지")
#히스토그램 y축
plt.ylabel("좋아요 수")
#0부터 10까지 4개로
#x축 0.8간격 가운데 정렬
plt.bar(menHistKeys,menHistValues,width = 0.8,align = 'center')
#y축의 길이를 좋아요수가 가장높은것으로 설정
plt.ylim([0,menValuesList[0]])
plt.show()
    
f.close()
f2.close()
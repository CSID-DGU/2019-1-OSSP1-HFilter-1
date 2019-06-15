# 동국대학교 OSSP 2019-1학기 1조 HFilter

group = {}
group["연예"] = ["AgeofStar", "Music", "아이돌", "댄스", "Mnet", "노래", "MOIM"]
group["친구"] = ["Friend", "친구"]
group["성별"] = ["여자", "남자", "언니", "남녀", "오빠"]
group["소셜"] = ["인스타그램", "그램"]
group["음식"] = ["맛집", "디저트", "EAT", "Cookat", "먹방", "Food", "푸드", "치킨",
               "petitzel", "HAITAI", "우유", "레시피"]
group["라이프"] = ["다이어트", "오늘", "라이프", "PLAY", "스타일", "내일", "카페"]
group["뷰티"] = ["뷰티", "성형", "진혹거", "화장", "Beauty", "Vely", "powderroom",
               "오즈", "존예", "pieu", "렌즈", "Wusinsa", "Estee"]
group["패션"] = ["Givenchy", "패션"]
group["쇼핑"] = ["Department", "Store", "Hi-mart", "SHOP", "쇼핑",
               "백화점", "포인트", "이마트", "페이", "G마켓", "인터파크"]
group["편의점"] = ["GS25", "Ministop"]
group["커뮤니티"] = ["직장인", "대학생", "청년", "나무숲", "Univ", "instiz", "그룹"]
group["학업"] = ["서비스", "대학교", "학과", "학교", "PPT", "캠퍼스", "YBM"]
group["취업"] = ["취업", "공모전", "활동", "대외", "외국어"]
group["대기업"] = ["삼성", "SK", "LG", "KT"]
group["학교"] = ["외대", "순천향대", "school", "고등학교"]
group["항공"] = ["항공", "운항", "승무원", "Air"]
group["가정"] = ["육아"]
group["연애"] = ["데이트", "연애", "사랑", "커플", "Enjoycouple"]
group["지역"] = ["서울", "부산", "대전", "전주", "세종", "둔산동", "Dae-jeon",
               "인천", "SEOUL", "Seoul", "울산", "청주", "광주", "대구", "수원"]
group["우리나라"] = ["Korea", "대한민국", "전국", "코리아"]
group["취미"] = ["덕후", "Military", "월드", "lotteworld", "UFC", "동물"]
group["여행"] = ["Plaeat", "여행", "트래블", "Travel", "N서울타워"]
group["브랜드"] = ["LOTTE", "GS", "Nike", "DADA", "다다", "Lotte", "monami"]
group["영화"] = ["CGV", "영화", "CINEMA", "Megabox", "명장"]
group["유머"] = ["베스트", "모음", "vonvon.me", "일반인", "lululala", "동영상"]
group["글"] = ["리뷰", "이야기", "STORY", "글귀", "후기", "꿀팁"]
group["뉴스"] = ["뉴스", "NewsBang", "NTD"]
group["미디어"] = ["딩고", "인사이트", "Wikitree", "BJ", "tvn", "페이지", "위키트리",
                "레전드", "PICKiS", "BaD-Mouth"]
group["감성"] = ["감성", "공간"]

# 위에 group 쓴거랑 같은데 파일입출력해서 불러온 것
catagory = {}
f = open("./datalist/data_group.txt", "r")
while True:
    line = f.readline()
    if not line: break

    n = line.find(":")
    key = line[:n]

    comma = line.find(',')
    while line[comma:].find(',') != -1:
        line = line.replace(",", "")
        comma = line[comma:].find(',')
        if comma == -1: break

    # default는 빈칸 기준으로 나누는 것
    # ex) 연예: ㅇㅇ 이므로 n+2부터 시작
    value = line[n+2:].split()
    catagory[key] = value

print(catagory.items())
f.close()

# '연예': ['A', 'B]이었다면
# 'A': '연예', 'B': '연예'로 바꾼다.
# group말고 category로 해도 똑같다.
case = {}
for key, value in group.items():
    for v in range (0, len(value)):
        case[value[v]] = key

# 1부터 26은 data1~data26
# data14는 data141~data1424 세부사항 별개로 존재
# 27부터 50은 data141부터 data1424를 위한 것
# group별로 가장 많은 순서로 저장한다.
for i in range (1, 51):
    readPath = "./datalist/extract/data" + str(i) + "extract.txt"
    if i>=27:
        ii = i - 26
        readPath = "./datalist/extract/data14/data14" + str(ii) + "extract.txt"

    f = open(readPath, "r", encoding='UTF-8')

    writePath = "./datalist/group/data" + str(i) + "group.txt"
    if i>=27:
        ii = i - 26
        writePath = "./datalist/group/data14/data14" + str(ii) + "group.txt"

    f2 = open(writePath, "w", encoding='UTF-8')

    # "소셜" : [10, "인스타그램", 7, "그램", 3]
    # 이런 형태로 기록될 것임
    record = {}

    while True:
        lines = f.readline()
        if not lines: break

        n = lines.find(' ')
        name = lines[:n]
        num = int(lines[n + 1:])

        if name in case:
            # case[name]이 record의 key에 있을 시
            if case[name] in record:
                record[case[name]][0] = record[case[name]][0] + num
                record[case[name]].append(name)
                record[case[name]].append(num)
            else:
                record[case[name]] = [num, name, num]

    f.close()

    # 개수에 따라 내림차순으로 정렬
    sort = sorted(record.items(), key=lambda t: t[1][0], reverse=True)
    print(sort)

    # [('성별', [416, '여자', 200, '남자', 216]), ...] 이런 형태로 되어있음
    for k in sort:
        f2.write(k[0] + " " + str(k[1][0]) + " : ")
        for k2 in range (1, len(k[1])):
            f2.write(str(k[1][k2]) + " ")
        f2.write("\n")

    f2.close()

# group 전체 요약 저장
groupWrite = {}
for i in range (1, 51):
    readPath = "./datalist/group/data" + str(i) + "group.txt"
    if i>=27:
        ii = i - 26
        readPath = "./datalist/group/data14/data14" + str(ii) + "group.txt"

    f = open(readPath, "r", encoding='UTF-8')

    for j in range (0, 3):
        line = f.readline()
        index = line.find(' ')
        name = line[:index]
        if j == 0:
            groupWrite[i] = [name]
        else:
            groupWrite[i].append(name)

    f.close()

# 1: 성별 라이프 소셜
# 2: 글 성별 음식
# 이런식으로 저장된다.
#groupPath = "./datalist/group/datagroup.txt"
groupPath = "./datalist/group/datagroup_+14.txt"
f = open(groupPath, "w", encoding="UTF-8")
for key, value in groupWrite.items():
    # data141~data1424는 따로 구분
    if key == 27:
        f.write("----------\n")
    if key >= 27:
        f.write(str(14) + str(key-26) + ":")
    else:
        f.write(str(key) + ":")

    for num in range (0, len(value)):
        f.write(" " + value[num])
    f.write("\n")
f.close()



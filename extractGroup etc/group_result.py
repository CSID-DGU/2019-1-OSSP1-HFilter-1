# 동국대학교 OSSP 2019-1학기 1조 HFilter

# 각 그룹별 선호 extract nouns를 가져온다.
# ex) 1: 음식 지역 성별
readPath = "./datalist/group/datagroup.txt"
f = open(readPath, "r", encoding='utf-8-sig')
# \ufeff 문제를 해결한다.
# 애초에 파일을 읽어들일 때 제거하는 것이다.

# ex) result[1] = [음식, 지역, 성별]
result = {}

# 1부터 26 (27은 포함 X)
# 각 그룹별 성향 저장하기
for i in range (1, 27):
    line = f.readline()

    # ex) 1: 성별 라이프 소셜
    n = line.find(":")
    # ex) 1
    key = line[:n]
    key = int(key)

    # ex) result[1] = ["성별", "라이프", "소셜"]
    subline = line[n+2:]
    next = subline.find("\n")
    blank1 = subline.find(" ")
    blank2 = subline.rfind(" ")
    result[key] = []
    result[key].append(subline[:blank1])
    result[key].append(subline[blank1 + 1 : blank2])
    result[key].append(subline[blank2 + 1 : next])

# end for문
f.close()

# 각 성향에 대한 설명
readPath = "./datalist/group_explain.txt"
f = open(readPath, "r")

# ex) explain["친구"] = "친구 머시기 blah blah"
explain = {}

# 각 성향별 explain 저장하기 (key:성향, value:text)
while True:
    line = f.readline()
    if not line: break

    # ex) 연예: 당신은 blah blah
    n = line.find(":")
    key = line[:n]

    # ex) 당신은 blah blah 부분만 저장
    explain[key] = line[n+2:]

# end while문
f.close()

# 1부터 26 (27은 포함 X)
# 각 그룹별 성향에 따라 성향과 explain 출력
for i in range (1, 27):
    # 각 그룹별 성향 explain 최종
    writePath = "./datalist/explain/data" + str(i) + "explain.txt"
    f = open(writePath, "w", encoding='UTF-8')

    # 당신은 "연애" "성별" "대한민국" 이 3가지에 관심(성향)이 많습니다.
    f.write("당신은")
    for j in range (0, 3):
        f.write(" \"" + result[i][j] + "\"")
    f.write(" 이 3가지에 관심(성향)이 많습니다.\n\n")

    # 각 성향 별 flavor text를 출력한다.
    for j in range (0, 3):
        f.write(result[i][j] + " flavor text\n:")
        f.write(" " + explain[result[i][j]] + "\n\n")

    f.close()
# end for문


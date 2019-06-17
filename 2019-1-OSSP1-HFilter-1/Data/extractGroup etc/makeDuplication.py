# 동국대학교 OSSP 2019-1학기 1조 HFilter

# 1부터 26은 data1~data26
# data14는 data141~data1424 세부사항 별개로 존재
# 27부터 50은 data141부터 data1424를 위한 것
# 각 문자열 개수만큼 문자열 중복 생성
for i in range (1, 51):
    readPath = "./datalist/data" + str(i) + "output.txt"
    modifyPath = "./datalist/modify/data" + str(i) + "modify.txt"

    # 27~50은 data141~data1424
    if i >= 27:
        ii = i - 26
        readPath = "./datalist/data14output/data14" + str(ii) + "output.txt"
        modifyPath = "./datalist/modify/data14/data14" + str(ii) + "modify.txt"

    f = open(readPath, "r", encoding='UTF-8')
    f2 = open(modifyPath, "w", encoding='UTF-8')
    while True:
        # ex) 고민 들어주는 여자 19
        line = f.readline()
        if not line: break

        # 맨 뒤 enter(\n) 제거
        line = line.replace("\n", "")
        # 맨 오른쪽 공백 삭제
        line = line.rstrip()

        # 뒤에서 빈칸 찾기
        n = line.rfind(' ')
        # ex) "고민 들어주는 여자 19"에서 19만 추출
        num = int(line[n + 1:])
        # 숫자만큼 반복하여 저장 (단어 빈도수 구하기 위해)
        for j in range(0, num):
            f2.write(line[:n] + "\n")

    f.close()
    f2.close()



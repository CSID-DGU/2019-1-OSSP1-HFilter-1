# 동국대학교 OSSP 2019-1학기 1조 HFilter

# 1부터 26은 data1~data26
# data14는 data141~data1424 세부사항 별개로 존재
# 27부터 50은 data141부터 data1424를 위한 것
# 추출한 명사들을 한 군데에 모아서 중복없이 저장한다.
dic = {}
for i in range (1, 27):
    readPath = "./datalist/extract/data" + str(i) + "extract.txt"
    f = open(readPath, "r", encoding='UTF-8')

    while True:
        line = f.readline()
        if not line: break

        # 빈칸 위치 찾고 빈칸 전 단어만 확인
        # ex) 사랑 100 있으면 '사랑'만 확인
        d = line.find(' ')
        line = line[:d]

        # 딕셔너리 key에 있는지 확인
        if(line in dic):
            continue
        # 없으면 key 생성
        else:
            dic[line] = 'exist'

Path = "./datalist/extract/kindOfNouns(sorted).txt"
Path2 = "./datalist/extract/kindOfNouns.txt"

kindOfNouns_sorted = open(Path, "w", encoding='UTF-8')
kindOfNouns = open(Path2, "w", encoding='UTF-8')

# 중복없이 저장한 단어(key)들을 write
# 정렬 순
for k in sorted(dic.keys()):
    kindOfNouns_sorted.write(k + "\n")

# 비 정렬 순
for k in dic.keys():
    kindOfNouns.write(k + "\n")

kindOfNouns_sorted.close()
kindOfNouns.close()

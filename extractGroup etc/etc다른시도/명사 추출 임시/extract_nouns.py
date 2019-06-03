# 동국대학교 OSSP 2019-1학기 1조 HFilter
# 명사 빈도수 추출해보기

f = open("data01output.txt", "r")
f2 = open("data01modify.txt", "w")
while True:
    # ex) 고민 들어주는 여자 19
    line = f.readline()
    if not line: break
    # 파일이 숫자 뒤에 빈칸있고 \n이 있다...
    line = line.replace(" \n", "")
    # 뒤에서 빈칸 찾기
    n = line.rfind(' ')
    # ex) "고민 들어주는 여자 19"에서 19만 추출
    num = int(line[n+1:])
    # 숫자만큼 반복하여 저장 (단어 빈도수 구하기 위해)
    for i in range(0, num):
        f2.write(line[:n]+"\n")
f.close()
f2.close()

f = open("data01modify.txt", "r")
lines = f.read()

# 자연어처리 KoNLPy 파이썬 패키지 이용
# okt(Open Korea Text) 형태소 분석기 사용
from konlpy.tag import Okt
nlpy = Okt()
# nouns: 명사 추출
nouns = nlpy.nouns(lines)
f.close()

# Counter 모듈로 리스트에 있는 각 항목을 셀 수 있다.
from collections import Counter
cnt = Counter(nouns)

keySet = [] # key와 빈도수 dictionary set
keySort = [] # key만 저장

# most_common은 리스트 안에 tuple들이 나타나는데
# tuple의 첫번째 요소는 추출한 명사고
# tuple의 두번째 요소는 해당 명사 빈도 수
# 상위 100개만 추출해보자
for k, n in cnt.most_common(100):
    keyDic = {'key': k, 'num': n}
    # 추출결과 중 유효한 단어만 뽑기 위해 2글자 이상만 저장
    if len(keyDic['key']) >= 2:
        keySet.append(keyDic)
        keySort.append(keyDic['key'])

f = open("data01most.txt", "w")
for set in keySet:
    f.write(set['key']+" "+str(set['num'])+"\n")
f.close()


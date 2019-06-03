# 동국대학교 OSSP 2019-1학기 1조 HFilter

# 자연어처리 KoNLPy 파이썬 패키지 이용
# okt(Open Korea Text) 형태소 분석기 사용
from konlpy.tag import Okt
nlpy = Okt()
# Counter 모듈로 리스트에 있는 각 항목을 셀 수 있다.
from collections import Counter
# 영어 단어 추출할 자연어처리 패키지
import nltk

# Emoji가 있으면 konlpy을 사용할 때
# 랜덤한 지점에서 kernel died 등의 오류가 발생
# '이모지'에 해당하는 범위의 캐릭터들을 모두 제거하자
import re
def strip_e(st):
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return RE_EMOJI.sub(r'', st)

# 1부터 26 (27은 포함 X)
# 중복생성된 문자열들 가지고 명사 추출
for i in range (1, 27):
    readPath = "./datalist/modify/data" + str(i) + "modify.txt"
    f3 = open(readPath, "r", encoding='UTF-8')
    # 파일 전체를 읽는다.
    lines = f3.read()

    # Emoji때문에 9번이랑 24번 데이터에서 오류뜬다
    # Process finished with exit code -1073740940 (0xC0000374)
    if i == 9 or i == 24:
        lines = strip_e(lines)

    # nouns: 명사 추출
    nouns = nlpy.nouns(lines)
    f3.close()

    # list에 있는 각 항목을 count한다.
    cnt = Counter(nouns)

    keySet = []  # key와 빈도수 dictionary set

    # most_common은 리스트 안에 tuple들이 나타나는데
    # tuple의 첫번째 요소는 추출한 명사고
    # tuple의 두번째 요소는 해당 명사 빈도 수
    # 상위 30개만 추출해보자
    for k, n in cnt.most_common(30):
        keyDic = {'key': k, 'num': n}
        # 추출결과 중 유효한 단어만 뽑기 위해 2글자 이상만 저장
        if len(keyDic['key']) >= 2:
            keySet.append(keyDic)

    # nltk를 쓰지 않을 때 사용, the 같은 관사도 체크함
    '''
    # 이제 영어 추출
    frequency = {}
    text_string = lines.lower()
    match_pattern = re.findall(r'\b[a-z]{2,20}\b', text_string)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    # 개수에 따라 내림차순으로 정렬
    eng = sorted(frequency.items(), key=lambda t : t[1], reverse=True)

    for k in range(0, len(eng)):
        keyDic = {'key': eng[k][0], 'num': eng[k][1]}
        if(k >= 30): break
        keySet.append(keyDic)
    '''

    # 명사인지 아닌지 test하는 함수
    is_noun = lambda pos: pos[:2] == 'NN'
    nouns = []

    tokenized = nltk.word_tokenize(lines, language="english")
    for (word, pos) in nltk.pos_tag(tokenized):
        if is_noun(pos):
            nouns.append(word)

    engDic = {}
    for word in nouns:
        # 2자리 이상, amp는 단어가 아닌데 불러올 때 잘못 변환
        if (len(word) < 2 or word == "amp"): continue
        # nltk가 한글도 인식해서 영어로 시작할 경우메나 체크
        if ord('a') <= ord(word[0].lower()) <= ord('z'):
            if (word in engDic):
                engDic[word] = engDic[word] + 1
            else:
                engDic[word] = 1

    # 개수에 따라 내림차순으로 정렬
    eng = sorted(engDic.items(), key=lambda t: t[1], reverse=True)

    check = 1
    for k in eng:
        keyDic = {'key': k[0], 'num': k[1]}
        # 한글 최대 30개, 영어 최대 10개
        if (check >= 10): break
        keySet.append(keyDic)
        check = check + 1

    extractPath = "./datalist/extract/data" + str(i) + "extract.txt"
    f4 = open(extractPath, "w", encoding='UTF-8')
    for set in keySet:
        f4.write(set['key'] + " " + str(set['num']) + "\n")
    f4.close()
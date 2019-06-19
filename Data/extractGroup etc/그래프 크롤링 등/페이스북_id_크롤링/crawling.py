##Copyright 2019. All rights reserved.
# OSSP in Dongguk University
# 2019-1-OSSP1-HFilter-1
import requests
import bs4

# -*- coding:utf-8 -*-

f = open("성_목록.txt", 'w')
f.close()
f = open("성_목록.txt", 'a')

url = "https://ko.wikipedia.org/w/index.php?title=한국의_성씨"  # url을 변수로 저장함.
html_result = requests.get(url)  # html을 가져옴.
print(html_result)  # 상태코드
# print(html_result.text) #html 정보
# html_result.encoding = 'UTF-8'
# print(html_result.encoding) # = 'euc-kr'
# print(sys.stdout.encoding)
# html_result.encode('cp949')
a = html_result.text

# soup = BeautifulSoup(a, 'html.parser')
# soup.find_all("a", class_="_2ial")

next = 0

# 성 100개 저장
# <a href="/wiki/%EC%B5%9C_(%EC%84%B1%EC%94%A8)" title="최 (성씨)">최</a>
# 이런 식으로 되어있음
for i in range(1, 100):
    b = a.find("(성씨)", next)
    c = a.find(">", b)
    # if(b < 0):
    #     break
    d = a.find("<", b)
    next = a.find("a", d)
    str = a[c + 1:d]
    f.write(str + "\n")

f.close()
print("finish! 성 목록 저장")

names = []
f = open("성_목록.txt", 'r')
lines = f.readlines()
for line in lines:
    # 메모장에 저장할 때 보기 편하려고 \n 추가해줬음
    first_name = line.replace("\n", "")
    names.append(first_name)

f.close()

print(names)

f = open("numID.txt", 'w')
f.close()
f = open("numID.txt", 'a')

for name in names:
    url = "https://www.facebook.com/public/" + name  # url을 변수로 저장함.
    html_result = requests.get(url)  # html을 가져옴.
    # print(html_result) #상태코드
    # print(html_result.text) #html 정보
    # print(html_result.encoding)
    # html_result.encoding = 'euc-kr'
    a = html_result.text

    # soup = BeautifulSoup(a, 'html.parser')
    # soup.find_all("a", class_="_2ial")

    # 무슨 성으로 검색했는지 확인하려고
    print(name + "\n")
    f.write(name + "\n")
    b3 = 0

    # <a class="_2ial" href="https://www.facebook.com/people/김채은/100027964147512">
    # 이런 식으로 되어 있음
    for i in range(1, 100):
        b = a.find("_2ial", b3)
        b1 = a.find("com/", b)
        b2 = a.find(">", b)
        b3 = a.find("a", b)
        str = a[b1:b2]
        if (len(str) < 1):
            f.write("\n")
            break
        ans = str[4:]
        if (ans.find("people") > -1):
            slash1 = ans.find("/")
            slash2 = ans.find("/", slash1 + 1)
            f.write(ans[slash2 + 1:len(ans) - 1] + "\n")
            # print(ans[slash2+1:len(ans)-1])
        else:
            f.write(ans[:len(ans) - 1] + "\n")
            # print(ans[:len(ans)-1])

f.close()
print("finish!")
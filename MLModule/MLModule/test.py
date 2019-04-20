# This is Test code
# Do not set this as a startup file

import MLModule

wDic = MLModule.makeModule("C:\\Users\\hacel\\source\\repos\\HFilter\\SampleData\\남자module.txt")

hList = ["동국대학교", "동국대학교 대나무숲", "인사이트 패션", "오늘 뭐 먹지?", "편한식사-Esiksa", "서울 갈데없다고 누가 그랬냐"]

w=MLModule.dtrHuman(hList, wDic)

print("남자일 확률 : " + (str)(w))

wDic = MLModule.makeModule("C:\\Users\\hacel\\source\\repos\\HFilter\\SampleData\\여자module.txt")

w=MLModule.dtrHuman(hList, wDic)

print("여자일 확률 : " + (str)(w))
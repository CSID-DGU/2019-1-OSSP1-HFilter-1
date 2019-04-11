#Copyright 2019. Jeongwon Her. All rights reserved.

import sys
import MLModule

path = input("경로를 입력하세요 : ")

path = MLModule.makeLabelByTxt(path)

if path == None:
    sys.exit(1)

select = input("히스토그램을 그립니까?(Yes/No) ")

if select=="예" or select=="Yes" or select=="yes"\
    or select=="1" or select=="o" or select=="ok":
    MLModule.makeHistogram(path, "페이지", "좋아요")

# End of Main
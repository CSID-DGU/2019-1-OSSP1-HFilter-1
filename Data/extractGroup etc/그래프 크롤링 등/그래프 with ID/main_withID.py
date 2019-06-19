
# coding: utf-8

# In[1]:


##Copyright 2019. All rights reserved.
#OSSP in Dongguk University
#2019-1-OSSP1-HFilter-1

#%matplotlib inline
import sys
get_ipython().run_line_magic('matplotlib', 'inline')
import num_withID

# Main
path_men = input("남자파일 경로 입력하세요 : ")
path_women = input("여자파일 경로 입력하세요 : ")
path_union = num_withID.merge_file_union(path_men, path_women)

# ID와 함께 구합니다.
path_men = num_withID.makeLabelByTxt_withID(path_men)
path_women = num_withID.makeLabelByTxt_withID(path_women)
path_union = num_withID.makeLabelByTxt_withID(path_union)

# Error
if path_men == None or path_women == None or path_union == None:
    sys.exit(1)

select = input("히스토그램을 그립니까?(Yes/No) ")

if select=="예" or select=="Yes" or select=="yes"    or select=="1" or select=="o" or select=="ok":
    num_withID.barChart_except_IDkorean(path_men)
    num_withID.barChart_except_IDkorean(path_women)
    num_withID.barChart_except_IDkorean(path_union)

# End of Main


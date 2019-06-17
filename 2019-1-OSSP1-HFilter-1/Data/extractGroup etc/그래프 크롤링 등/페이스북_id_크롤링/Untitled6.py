
# coding: utf-8

# In[1]:


import requests

url = "http://www.naver.com" #url을 변수로 저장함.
html_result=requests.get(url) #html을 가져옴.
print(html_result) #상태코드
print(html_result.text) #html 정보


# In[2]:


import requests

url = "https://www.facebook.com/public/%EA%B9%80%EB%8F%99%EC%9A%B1" #url을 변수로 저장함.
html_result=requests.get(url) #html을 가져옴.
print(html_result) #상태코드
print(html_result.text) #html 정보


# In[3]:


import requests

url = "https://www.facebook.com/public/김동욱" #url을 변수로 저장함.
html_result=requests.get(url) #html을 가져옴.
print(html_result) #상태코드
print(html_result.text) #html 정보


# In[4]:


import requests

url = "https://www.facebook.com/public/김동욱" #url을 변수로 저장함.
html_result=requests.get(url) #html을 가져옴.
print(html_result) #상태코드
print(html_result.text) #html 정보

with open("c:\\naver_html.html","w") as naver_html:
    naver_html.write(html_result.text)
    print("파일입출력 완료")



# In[5]:


import requests

url = "https://www.facebook.com/public/김동욱" #url을 변수로 저장함.
html_result=requests.get(url) #html을 가져옴.
print(html_result) #상태코드
print(html_result.text) #html 정보

with open("find_html.html","w") as find_html:
    find_html.write(html_result.text)
    print("파일입출력 완료")



# In[6]:


import requests

url = "https://www.facebook.com/public/김동욱" #url을 변수로 저장함.
html_result=requests.get(url) #html을 가져옴.
print(html_result) #상태코드
#print(html_result.text) #html 정보

with open("find_html.html","w") as find_html:
    find_html.write(html_result.text)
    print("파일입출력 완료")



# In[7]:


import requests

url = "https://www.facebook.com/public/김동욱" #url을 변수로 저장함.
html_result=requests.get(url) #html을 가져옴.
print(html_result) #상태코드
#print(html_result.text) #html 정보

with open("find_html.html","w", encoding="utf-8") as find_html:
    find_html.write(html_result.text)
    print("파일입출력 완료")



# In[8]:


import requests

url = "https://www.facebook.com/public/김동욱" #url을 변수로 저장함.
html_result=requests.get(url) #html을 가져옴.
print(html_result) #상태코드
#print(html_result.text) #html 정보

with open("find_html.html","w", encoding="utf-8") as find_html:
    find_html.write(html_result.text)
    print("파일입출력 완료")



# In[9]:


import requests

url = "https://www.facebook.com/public/김동욱" #url을 변수로 저장함.
html_result=requests.get(url) #html을 가져옴.
print(html_result) #상태코드
#print(html_result.text) #html 정보

with open("find_html.txt","w", encoding="utf-8") as find_html:
    find_html.write(html_result.text)
    print("파일입출력 완료")



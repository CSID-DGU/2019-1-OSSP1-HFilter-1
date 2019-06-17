
# coding: utf-8

# In[1]:


import sys
import urllib.request
import json

if __name__ == '__main__':
    # [CODE 1]

    page_name = "jtbcnews"
	# 내가 만든 개발자 모드 id, secret code
    app_id = "308819746676543"
    app_secret = "d122d0649cee41e53e628540f749810f"
    access_token = app_id + "|" + app_secret

    # [CODE 2]

    # https://graph.facebook.com/v2.8/[page_id]/?access+token=[App_ID]|[Secret_Key]

    # 형식의 문자열을 만들어 낸다


    base = "https://graph.facebook.com/v3.2" # v2.8
    node = "/" + page_name
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters
    
    print(url)

    # [CODE 3]

    req = urllib.request.Request(url)

    # [CODE 4]

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            data = json.loads(response.read().decode('utf-8'))
            page_id = data['id']
            print ("%s Facebook Numeric ID : %s" % (page_name, page_id))
    except Exception as e:
        print (e)
    # 앱 검수를 받아야 한다.
	# https://graph.facebook.com/v3.2/jtbcnews/?access_token=308819746676543|d122d0649cee41e53e628540f749810f
    # "error": {
    #  "message": "(#10) To use 'Page Public Content Access', your use of this endpoint must be reviewed and approved by Facebook. To submit this 'Page Public Content Access' feature for review please read our documentation on reviewable features: https://developers.facebook.com/docs/apps/review.",
    #  "type": "OAuthException",
    #  "code": 10,
    #  "fbtrace_id": "Ay5jgEr9W7z"
    #}


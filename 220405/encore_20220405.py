#!/usr/bin/env python
# coding: utf-8

# In[151]:


import requests


# In[152]:


url= 'https://www.starbucks.co.kr/store/getStore.do?r=804IUG79N7'
payload = {
    'in_biz_cds' : '0',
    'in_scodes' : '0',
    'ins_lat' : '37.5627128',
    'ins_lng' : '126.93279869999999',
    'search_text' : '',
    'p_sido_cd' : '01',
    'p_gugun_cd' : '',
    'in_distance' : '0',
    'in_biz_cd' : '',
    'isError' : 'true',
    'searchType' : 'C',
    'set_date' : '',
    'all_store' : '0',
    'T03' : '0',
    'T01' : '0',
    'T12' : '0',
    'T09' : '0',
    'T30' : '0',
    'T05' : '0',
    'T22' : '0',
    'T21' : '0',
    'T10' : '0',
    'T36' : '0',
    'P10' : '0',
    'P50' : '0',
    'P20' : '0',
    'P60' : '0',
    'P30' : '0',
    'P70' : '0',
    'P40' : '0',
    'P80' : '0',
    'whcroad_yn' : '0',
    'P90' : '0',
    'new_bool' : '0',
    'iend' : '1000',
    'rndCod' : 'V8UNZFKU44',}


# In[153]:


r = requests.post(url, data=payload)


# In[154]:


r.text


# In[155]:


rt_dict = r.json()


# In[156]:


type(rt_dict)


# In[157]:


rt_dict.keys()


# In[158]:


rt_dict['list']


# In[159]:


len(rt_dict['list'])


# In[160]:


for x, y in rt_dict['list'][0].items():
    print(x, " -> " ,y)


# In[161]:


a = dict()


# In[162]:


a = {}


# In[163]:


a['encore'] = 100
a


# In[164]:


a['서초'] = 200
a # 없는 키값 설정하면 만들어짐


# In[165]:


a['encore'] = 1000
a # 키값 중복 허용 안해서 덮어쓰기 됨.


# In[166]:


print('서초2' in a)
'encore' in a # in으로 존재여부 확인 가능


# In[167]:


if 'encore' in a:
    a['encore'] += 1
a


# In[220]:


gu = dict()
for x in rt_dict['list']:
    #print(x['gugun_name'], end = ", ")
    if x['gugun_name'] in gu:     
        gu[x['gugun_name']] += 1
    else:
        gu[x['gugun_name']] = 1
    print(gu.values())


# In[169]:


head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"}


# In[170]:


r = requests.get("https://www.melon.com/song/detail.htm?songId=34845949", headers=head)


# In[171]:


r.status_code


# In[172]:


from bs4 import BeautifulSoup


# In[173]:


bs = BeautifulSoup(r.text)
print(type(bs))
bs


# In[174]:


bs.find("div", id="d_video_summary") # id로 찾기


# In[175]:


bs.find("div")


# In[176]:


text = BeautifulSoup(str(bs.find("div", id="d_video_summary")).replace("<br/>", "\n")).text
# replace . str에 있는 메소드 전자를 후자로 바꿔줌


# In[177]:


text1 = text.strip() # 양 끝에 있는 공백이나 개행문자들 삭제


# In[45]:


text1


# In[46]:


print(text1) # print는 \t \n \r 등등을 해석해서 출력함.


# In[47]:


dir(text1)


# In[150]:


print(len(text1.split())) # 221개의 글자
text1.split('\n') # 파라미터값 기준으로 잘라줌 
# 리턴값 list -> 순환가능


# ## 요청 : 각 단어의 카운트

# In[49]:


text1.split()
"La".lower()
"la".upper()
dir('la')
help('la'.lower)


# In[50]:


yo = dict()
for x in text1.split():
    if len(x) > 1:     
        if x in yo:
            yo[x] += 1
        else:
            yo[x] = 1
yo


# ## 튜플

# In[51]:


tupleA = (1,2,3)


# In[52]:


listA = [1,2,3]


# In[53]:


tupleA[0] = 100 # 파이썬에서 튜플은 한번 만들어지면 변경 불가능


# ## 사용자 함수

# In[54]:


def myfunc():
    return 1
myfunc()


# In[55]:


def myfunc2(a):
    return a ** 2, a ** 3
myfunc2(10)  # 10 말고 (10)은 튜플.


# ## unpacking

# In[56]:


a1 = myfunc2(100)
a1


# In[57]:


a, b = myfunc2(100)   # ???
a, b


# In[58]:


a1, a2, a3 = (1,2,3)
a1


# In[224]:


def myfunc(a, c, b=20): # 기본값 설정할땐 끝부터 채우기.
    return a + b
myfunc(10,10) # ??


# In[60]:


print(rt_dict['list'][0]['addr'])
rt_dict['list'][0]['addr'].find('역삼') # 역삼이 10번째 index부터 있음.


# In[61]:


def find_starbuck(addr):
    rt = []
    for x in rt_dict['list']:
        if x['addr'].find(addr) > 0:
            rt.append(x['addr'])
    return rt
rt = find_starbuck("서초")
rt


# In[62]:


for x in rt_dict['list']:
    print(x['s_name'])


# In[63]:


def find_starbucks2(type_):
    if type_ == 'dt':
        for x in rt_dict['list']:
            if x['s_name'][-2:] == "DT":
                rt.append(x['addr'])
    elif type_ == 'r':
        for x in rt_dict['list']:
            if x['s_name'][-1:] == "R":
                rt.append(x['addr'])
    else:
        return -1
    return rt
find_starbucks2('r')


# In[64]:


"""
type_ = 'dt'
return dt 매장 주소만 리턴
type_ = 'r'
return 리저브 매장 주소만 리턴 
type_ 2가지 이외의 데이터 입력할 경우 return -1
"""
find_starbucks2(1)


# ### 질문 : 가장 최근에 만들어진 매장?

# In[65]:


open_star = {}
for x in rt_dict['list']:
    open_star[x['s_name']] = x['open_dt']
sorted(open_star.items(), key=lambda x : x[1], reverse=True) # 내림차순 True 오 F


# In[66]:


help(sorted)


# In[67]:


sorted([34, 234, 23, 4234])


# In[68]:


def tmp(x):
    return x[1]
sorted(open_star.items(), key=tmp)


# In[69]:


sorted(open_star.items(), key=lambda x : x[1])


# In[90]:


try:
    1 / 0
except:
    # 코드 ~~
    print("오류나떠")
finally:
    print("무조건 실행")
print("~~~")


# In[96]:





# In[101]:


a = [1,2,3]
try:
    a[5]
    1 / 0
except IndexError:
    print("인덱스 벗어남")
except ZeroDivisionError:
    print("0으로 나눴다")
except Exception as e:  # 에러사항 보기
    # 코드 ~~
    print(e)
# 옵션
finally:
    print("무조건 실행")
print("~~~")


# In[3]:


a = 10 # 전역변수
def tmp():
    a = 20 #지역변수
    print (a)
tmp()


# In[10]:


def tmp2():
    a10 = "test"
    print(a10)
tmp2()


# In[7]:


def tmp2():
    global a10
    a10 = "test"
    print(a10)
tmp2()


# In[8]:


a10


# In[14]:


def tmp3(a, *b):
    print(a, b)
tmp3(1,2,3,4,5,6) 
# 파라미터에 몇개를 넣을지 모를때 *를 넣으면 나머지는 튜플로 만들어준다


# In[17]:


a = 10
while a < 20:
    print("x", end=".")
    a += 1


# - continue, break

# In[16]:


while True:
    data = input("데이터 입력 : ")
    if data == "Q":
        break
    print (int(data) + 100)


# ## 파일

# ## 상대경로 : ./ -> 현재폴더
# ## 절대경로 : 

# In[27]:


# 첫번째 -> 파일경로, 두번째 -> 쓸지? 읽을지?, 세번째 -> 인코딩
f = open("./bigbang.txt", "w", encoding='cp949')


# In[19]:


import requests
from bs4 import BeautifulSoup
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"}
r = requests.get("https://www.melon.com/song/detail.htm?songId=34845949",headers=head)
bs = BeautifulSoup(r.text)
text = BeautifulSoup(str(bs.find("div", id="d_video_summary")).replace("<br/>", "\n")).text
text = text.strip()


# In[30]:


f.write(text)


# In[225]:


f.close() # close 해야 저장됨


# ### 읽기

# In[32]:


f1 = open("./bigbang.txt", 'r', encoding='cp949')


# In[33]:


f1.read()


# In[35]:


f1.read() 
# read함수는 포인터를 가지고 있음.항상 첫번째를 가리키고 
# read를 사용하면 맨끝으로 포인터를 이동해서 다시 read하면 읽을것이 없음


# In[39]:


f1.tell() # 포인터 어디있어?


# In[36]:


f1.seek(0) # 0으로 가


# In[37]:


f1.tell()


# In[38]:


f1.read() # 다시 읽힘


# In[40]:


f1.read()


# In[41]:


import os


# In[43]:


os.getcwd() # 현재 작업하는 python의 경로


# In[44]:


#os.chdir(변경할 디렉토리) # 변경


# In[50]:


if os.path.isdir("./melon") == False: # 없으면
    os.mkdir("./melon")                # melon 폴더 만들어


# In[51]:


os.path.isdir("./apple")


# In[53]:


from bs4 import BeautifulSoup


# In[54]:


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# In[55]:


BeautifulSoup(html_doc, 'lxml')


# In[57]:


bs = BeautifulSoup(html_doc, 'html.parser')


# In[66]:


bs.find("a")


# In[63]:


bs.findAll("a") # 순환 가능
bs.findAll("a")[0].text


# In[64]:


bs.findAll("a")[0]['href']


# In[67]:


bs.find("a", id="link2")


# In[70]:


bs.findAll("a", id="link2")[0] # 단수를 찾아도 []로 감싸져있어서 index지정


# In[75]:


bs.findAll(class_='sister')


# In[76]:


melon = "https://www.melon.com/chart/index.htm"


# In[77]:


head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}


# In[80]:


r = requests.get(melon, headers=head)


# In[82]:


r.text


# In[83]:


bs = BeautifulSoup(r.text, 'html.parser')


# In[84]:


bs.findAll("tr", class_="lst50")


# In[87]:


melon_100 = bs.find("table").findAll("tr")


# In[130]:


x.find("div", class_="wrap_song_info").find("a")['title'][:-3]


# In[139]:


import requests
from bs4 import BeautifulSoup
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"}
target = "https://www.melon.com/song/detail.htm?songId={}"
r = requests.get(target.format("34808759"),headers=head)
bs = BeautifulSoup(r.text)
text = BeautifulSoup(str(bs.find("div", id="d_video_summary")).replace("<br/>", "\n")).text
text = text.strip()


# ### 사용자 함수로 작성
# * Id 값을 매개변수로
# 
# def extract_lyrics(id_): <br>
#     return lyrics
# 
# ### 멜론 폴더에 노래 가사 저장 -> 가수_노래제목.txt
# ### 19세 노래는 예외처리

# In[ ]:


x.find("div", class_="wrap_song_info").find("a")['title'][:-3]


# In[145]:


for x in melon_100[1:]:
    #print(x.find("div", class_="wrap_song_info").find("a")['href'].split(","), end = " ---> ")
    print(x.find("div", class_="wrap_song_info").find("a")['href'].split(",")[-1][:-2], end = " -- ")
    print(x.find("div", class_="wrap_song_info").find("a")['title'].replace(" 재생","").strip(), end = " - ")
    print(x.find("div", class_="ellipsis rank02").find("a").text)


# In[144]:


r = requests.get("https://www.melon.com/song/detail.htm?songId=34845949", headers=head)
r.status_code
from bs4 import BeautifulSoup
bs = BeautifulSoup(r.text)
print(type(bs))
bs
bs.find("div", id="d_video_summary") # id로 찾기


# In[ ]:





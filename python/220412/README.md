# 0412 Review 📖

### Data Frame
pd.DataFrame(r.json()['OutBlock_1'])
dataFrame으로 만들어줌

### .unique()
- 데이터 중에 유일한 값(고유한 값)을 찾을 때 쓰는 함수 
동명이인 빼고싶어서, unique()만 하면 선수명 나옴 대신 중복값포함

### .duplicated()
df[df.duplicated()]
- 데이터 중에 중복값이 있는지 확인하는 코드
- 단 data frame안에서의 데이터를 처리할 때 사용함
- DataFrame.duplicated()

```
df.drop_duplicates(inplace=True)
```
중복값이 있는지 확인 후 중복값 제거


### .shape
- row와 column의 차원을 표시하는 개념
- 튜플로 (row, col)를 나타내줌
- 동명이인인 사람의 수와 column 수 표시
```
preprocessing[preprocessing['선수명'].duplicated()].shape
(40, 15)
```

### copy() 모듈을 사용하는 이유?
- 원본 데이터에서 값을 꺼내고 수정하다보면 원본 데이터가 변경 될 수 있는데 리스트를 복사함으로써 이를 방지할 수 있다
- 데이터에서 어떤 조건을 뽑을 때 사용하길 권장함


pd.DataFrame(search_starbucks(None))[['addr']]
데이터 프레임으로 여러 컬럼들을 담고 싶을 때
pd.DataFrame(search_starbucks(None))['addr']
series를 

### Data Frame 합치기 (merge, join, concat)
- merge  
pd.merge(right, left, left_on, right_on, how)
key값을 기준으로 두 개의 데이터 프레임을 합칠 때 사용하는 함수  
_on: 정렬할 기준이 될 key  
how : 병합시킬 위치  

```
imort pandas as pd

pd.set_option('preprocessing', 10)
pd.set_option('original_extract', 20)

pd.merge(preprocessing, original_extract, left_on=['선수명', '등번호'], right_on=['선수명', '등번호'], how='left')
```
왼쪽 dataframe을 기준으로 병합되기 때문에 10개의 행이 만들어진다. 

- join  
merge와 거의 큰 차이가 없이 비슷한 병합 함수이다
```
df1.join(df2. how='left')
```
df1에 df2를 결합하는 것
on값에 따라 결합 위치가 변경된다

- concat  
pd.concat([데이터프레임], [데이터프레임])  
단어 그대로 데이터 프레임을 이어붙이는 것  
dataframe의 결합으로 dataframe들을 합치는 것  
append는 index와 column이 없어도 사용 가능하지만 concat은 그럴 수 없다  

```
stock1
	날짜	종가	전일비	시가	고가	저가	거래량	종목코드
1	2022.04.12	280000.0	5500.0	277000.0	284500.0	275000.0	39222.0	128940
2	2022.04.11	274500.0	500.0	273000.0	275500.0	270000.0	18325.0	128940
3	2022.04.08	274000.0	10000.0	265000.0	275000.0	265000.0	29675.0	128940

stock2
날짜	종가	전일비	시가	고가	저가	거래량
1	2022.03.29	277000.0	2500.0	280500.0	280500.0	276500.0	15224.0
2	2022.03.28	279500.0	0.0	277500.0	280000.0	275500.0	14122.0

pd.concat([stock1, stock2])

날짜	종가	전일비	시가	고가	저가	거래량	종목코드
1	2022.04.12	280000.0	5500.0	277000.0	284500.0	275000.0	39222.0	128940
2	2022.04.11	274500.0	500.0	273000.0	275500.0	270000.0	18325.0	128940
3	2022.04.08	274000.0	10000.0	265000.0	275000.0	265000.0	29675.0	128940
1	2022.03.29	277000.0	2500.0	280500.0	280500.0	276500.0	15224.0	NaN
2	2022.03.28	279500.0	0.0	277500.0	280000.0	275500.0	14122.0	NaN
```
일치하지 않는 부분은 Nan으로 null값으로 결측치가 표시된다

+ 위의 정렬을 역방향으로 하기
```
pd.concat([stock1, stock2]).iloc[::-1]
```

### 결측치
데이터에 null값, 데이터가 없는 것

- 결측값 찾기
df.isnull().sum()
결측값(true, false)중에서 true의 수를 세어서 총 합으로 나타내줌

df[‘입단년도’] = df.입단년도


### .contains()
```
df[df[‘Team’].str.contains(‘고양’)]
```
Team이름이 고양인 선수의 목록을 나타냄


df.loc[df[‘Team’].str.contains(‘고양’), ‘Team’]=’ 키움 히어로즈’
loc[]를 사용해서 Team이름이 고양인 선수들의 team명을 키움 히어로즈로 변경시킨다=키움 히어로즈로 바뀌게 된다 합친다

### .set_options()
pd.set_option(‘display.max_rows’, None)
데이터 전체를 화면에 출력하고 싶을 때 사용하는 변수


### groupby method를 이용한 집계
- count()
요소의 갯수를 구하는 것
```
df.groupby(['Team'])[['용병']].count()

	용병
Team	
KIA 타이거즈	84
KT 위즈	83
LG 트윈스	89
```

- sum()
요소의 갯수를 구하는 것
```
df.groupby(['Team'])[['용병']].sum()

	용병
Team	
KIA 타이거즈	3
KT 위즈	3
LG 트윈스	3
```
각 Team의 용병이라는 목록의 갯수를 구함


### .dropna()
결측치(null인 값)을 제거해주는 코드
```
stock1 =pd.read_html(r.text)[0].dropna()
```

### 
```
def get_naver_stock(code, page=11):
    """
        code : 종목정보 
        page : 해당 페이지 정보 추출 
    """
    url = "https://finance.naver.com/item/sise_day.naver?code={}&page={}"
    head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36"}
    total = list()
    for x in range(1, page):
        r = requests.get(url.format(code, x), headers=head)
        total.append(pd.read_html(r.text)[0].dropna())
    total_df = pd.concat(total)
    total_df['종목코드'] = code
    return total_df.iloc[::-1]
```

### 인덱스 설정 해제
df.reset_index(drop=True, inplace=True)
인덱스 값을 삭제시키고 싶을 때 reset_index(drop=True)를 적용

### 논리 연산자
- and -> &
- or -> |
- not -> ~

### .first() .nth()
df.groupby(['Team']).first()
groupby에 의해 Team내에서 가장 기준이 높은 대상을 추출함

df.groupby(['Team']).nth(0) #1위 2위 3위 ...
1st 2nd 3th 4th 의 nth로 


### 🔍 예제
```
df.groupby([‘Team’, ‘포지션’], as_index=False)[[‘연봉(만원)’]].mean()
```
Team과 포지션을 dataframe으로 만들고 인덱스 해제 후, 연봉은 평균 값으로 계산
Team과 포지션이 동일한 선수들을 묶어서 column에 맞는 각각의 수를 표시

```
df.loc[df['연봉'].notnull(), '용병'] = df.loc[df['연봉'].notnull(), '연봉'].apply(lambda x:x[-2:] == '달러')
```
‘달러’로 연봉이 끝나는 선수는 용병으로 정의하고 그 중 연봉의 값이 null 이 아닌 선수만 dataframe으로 정리
```

### 🔍 예제 - map 표시하기
```
import folium
seoul_map = folium.Map(location=[37.55,126.98], zoom_start=12)
```
지도를 로딩하는 코드

# 0413 Review 📖

### .iter()
iterrable? 반복가능하다  
for문처럼 작동하며 반복되는 데이터를 처리하는 기능을 하는 함수

- 사용법
```
import xml.etree.ElementTree as ET

root = ET.fromstring(r.text)
items = root.iter(tag='item')
```
대신 items[0] 처럼 인덱싱으로 호출이 불가능하다 -> for문으로만 가능

### .set 집합
```
set([1,2,3,3,3,3])
{1, 2, 3}
```
이렇게 중복값 제거 가능

- 차집합
차이를 알고싶으니 차집합
set(set_b) - set(set_a)

.astype(int) 
형변환 해주는 함수

.diff(-1)
현재위치에서 어느위치(-1)를 뺄건지
-1이니까 현재의 바로 뒤에 걸 빼는 것

.shift(1)
row를 한 열 밑으로 내리는 함수


### Python array[::] 용법
arr[a:b:c]의 형태로 되어있는데, index a 부터 b까지 c의 간격으로 배열이 만들어 지는 것
c가 none이면 한칸 간격으로 

```
tmp[::-1]
```
전체 배열을 -1의 간격(역순)으로 배열을 만든 것

### .concat
index를 기준으로 column이 옆으로 붙게된다 (column만 이동하게 됨)


### ORM
- 예시
```
import sqlalchemy
pip install mysqlclient
engine = sqlalchemy.create_engine("mysql+mysqldb://root:" + "1234" + "@127.0.0.1/stock", encoding='utf-8')
conn = engine.connect()
covid2.to_sql(name='covid2', con = engine, if_exists = 'replace', index=False)
```

- if_exists
'replace' 는 같은 이름의 테이블이 있으면 이 결과로 대체됨
‘append’는 같은 이름의 테이블이 있으면 밑에 추가됨
‘fail’는 error처리함

pd.read_sql_query("select * from covid", conn)
쿼리문으로 테이블에 담긴 모든 데이터 출력

```
tmp3.to_sql(name='tmp', con = engine, if_exists = 'append', index=False, 
           dtype = {
               'createDt' : sqlalchemy.types.VARCHAR(100),
               'deathCnt' : sqlalchemy.types.INTEGER(),
               'decideCnt' : sqlalchemy.types.INTEGER()
           })
```

### 중복값
.duplicates -> drop할 때
.duplicated -> 중복값을 확인할 때

### column 
- column 이름 바꾸는 법
tmp.columns = ['주소', '운영시간', '매장이름']   
column에 원하는 이름의 리스트를 대입해서 작성하면 된다
단, column의 개수와 list의 내의 요소의 개수가 같아야함

- column 순서 변경
ediya_df = ediya_df[['매장이름', '주소', '운영시간']]
data frame안에 []의 형식으로 원하는 순서대로 리스트를 작성하면 된다

### 원하는 column을 기준으로 정렬하기
ediya_df.sort_values(by=['마감'])



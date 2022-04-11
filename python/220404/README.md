# 0404 Review 📖

<br>

### 1.list[-1] 는 마지막 index

### 2. list[타입]
- python에선 list에 value는 어떤 타입을 넣어도 된다.
- 타입 혼용 가능

### 3. for x in y :

- java의 for(x : y)와 같다.
- x에 y의 값들을 넣는다.

### 4. "{} x {} = {}".format(a, b, a*b)
- {} x {} = {} 라는 형태에 a, b, a*b 를 맵핑하여
a x b = a*b 를 수행

### 5. list comprehension
- for문 간소화
``` 
- 예)
[x for x in range(1,10) if x % 2 == 0]
1~9의 범위와 2로 나눈 나머지가 0인값을 x에 대입하고 그 x들을 배열화
```

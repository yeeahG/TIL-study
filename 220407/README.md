# 0407 Review 📖

<br>

## 1. enumerate  
```
for ~~~ in **enumerate**():
```
- data의 실행순서를 index화 해준다
- for 문을 돌릴때 어디까지 되었는지 확인가능
- 데이터의 진행순서를 알려줌


## 2. unpacking
```
In :
for x in ~~~:
 a, b = x.text.split(":")
        player_dict[a] = b.strip()
a, b

out :
{'선수명': '강정현'}
```

## 3. sorted(~~.items())
sorted(tmp)를 했더니 value값은 나오지 않고 key값만 나왔는데 
tmp.items()를 했더니 value값까지 잘 출력되었다.
```
In:
sorted(tmp.items(), key=lambda x : x[1], reverse=True)

out:
[('한기원', 39.24646781789639)]
```

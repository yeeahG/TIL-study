# playdata-java-study

## 1. 제어의 역전이란?
- 기존 제어 흐름
MainApplication → BankStatementAnalyzer → BankStatementParser

            ↘   BankStatementAnalyzer → BankStatementProcessor


기존에 Main에게 BankStatementAnalyzer 객체의 생성 요청하던 일을
BankStatementFactory를 생성후 BankStatementProcessor와 BankStatementTSVParser에게 전달하여 
원래 받던 BankStatementAnalyzer에게 전달하여 순서가 역전 된 것을 의미한다.

- 바뀐 제어 흐름
MainApplication → BankStatementFactory → BankStatementParser(+ interface)   →  BankStatementAnalyzer

                                        ↘        BankStatementProcessor    ↗

## 2. 인터페이스와 다형성이 뭘까요?
- 인터페이스
한 클래스에 있어서 메서드 생성 가이드라인 또는 규격

- 다형성
A.java → B.java → C.java 형태와 같이 하나의 객체가 여러 타입(형태)을 가질 수 있는 것을 의미한다.


## 3. 구현된 클래스에 메소드를 추가, 삭제 어떻게 될까요?
직접 추가 삭제를 해본 결과
![오류1](https://user-images.githubusercontent.com/95362504/158567422-d2bf7a66-2b46-4a75-9847-ccc7ed718b08.png)

![오류2](https://user-images.githubusercontent.com/95362504/158567461-36181c38-3241-43b6-b612-216eb0060f5c.png)

위와 같이 인터페이스에 어기게 되면 해당 인터페이스의 규격에 맞게 생성 또는 삭제하라는 오류메시지를 출력한다.

# 0317 Review

### 1. Bean의 역할은 무엇일까요?
- Answer
ApplicationContext.getBean()으로 얻어질 수 있는 객체는 빈이다.
즉, Spring에서의 빈은 ApplicationContext가 알고있는 객체, 즉 ApplicationContext가 만들어서 그 안에 담고있는 객체를 의미한다.

### 2. @Component, @ComponentScan, @Autowired, @Service, @Controller는 무엇일까요?
- @Component
: 개발자가 직접 작성한 Class 를 Bean 으로 만드는 것이다.
: 즉, 패키지 스캔 안에 이 어노테이션은 "이 클래스를 정의했으니 빈으로 등록하라" 는 뜻이 된다.

- @ComponentScan
: Component 어노테이션이 붙은 클래스들을 검색한다.

- @Autowired
: 생성자, setter, 필드의 경우를 Autowired에 등록 할 수 있다.
: 각 상황의 타입에 맞는 IoC컨테이너 안에 존재하는 Bean을 자동으로 주입 한다.

- @Service
: Component의 하위 애노테이션으로 DAO가 DB에서 받아온 데이터를 가공하는것이다.

- @Controller
: @Controller어노테이션은 MVC패턴에서 Controller클래스에 선언, @Component어노테이션을 써도 상관없다. 하지만 @Controller 어노테이션을 사용함으로 @RequestMapping 등의 추가 어노테이션을 사용 가능


### 3. spring_mvc_tutorial의 전반적인 흐름은 어떻게 될까요?
         MainController.java init() -> index.jsp -> MainController.java modelAndView() or getBook() -> result.jsp 

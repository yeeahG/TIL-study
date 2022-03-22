# 0322 Review 📖




### 📌 영속성이 무엇인가요?
1. 영속성 컨텍스트(Persistence Context)란 Entity를 영구히 저장하는 환경을 의미함 <br>
2. EntityManager로 Entity를 CRUD 처리하며, 이렇게 처리된 Entity는 DB에 곧바로 반영되는 것이 아니고, 영속성 컨텍스트에 보관, 관리됨 <br>
3. 영속성 컨텍스트는 EntityManager 생성 시 만들어지기 때문에 EntityManager를 통해 영속성 컨텍스트에 접근, 관리가 가능함.


### 📌 find()<br>
 - em.find()가 호출되면 1차 캐시에서 Entity를 찾고, 찾고자 하는 Entity가 1차 캐시에 없을 경우 DB에서 조회하게 됨
(1차 캐시에서 우선 검색)
    ```commandline
    예) find(Student.class, 1L)

    결과 : SQL의 Student table의 첫번째 Entity를 반환
    ```
 

### 📌 EntityTransaction
 - 작업을 한 단위로 묶음.
 - em이 가지고 있는 method. (EntityManager.getTransaction())
 - begin으로 시작하고 commit으로 모아둔 쿼리를 DB에 저장


 
### 📌 remove()
 - 엔티티를 삭제할때 사용된다
 - 영속성 context에서 삭제되고 commit이 되기 전까진 반영되지 않는다.
 - 삭제한 엔티티는 재사용되지 않고 JVM에 의해 Garbage Collection 되도록 한다.<br>

    ```
    예) Major major = em.find(Major.class, 1L); 
    em.remove(major);
        
    결과 : major 삭제.
    ```

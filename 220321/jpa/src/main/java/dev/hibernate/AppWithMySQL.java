package dev.hibernate;

import java.util.Date;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;

import dev.hibernate.model.Book;

/**
 * MYSQL 명령어
 * 모든 DB 조회 : show databases;
 * DB생성 : create database DB이름;
 * 현재 사용중인 DB 조회 : select database();
 * 사용할 DB로 변경 : use DB이름;
 * 현재 사용중인 DB가 가지고 있는 Table 조회 : show tables;
 * Table 정보 조회 : desc table이름;
 * Table 데이터 조회 : select * from table 이름
 * 
 *
 */
public class AppWithMySQL {
    public static void main(String[] args) {

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("jpa");

        // EntityManagerFactory를 통해서 EntityManager 생성
        EntityManager em = emf.createEntityManager();

        // 트랜잭션 만들기
        EntityTransaction tx = em.getTransaction();

        try {
            // 트랜잭션은 트랜잭션 사이에서 해야한다.
            // 트랜잭션 시작한다.
            tx.begin();
            Book book = new Book();
            book.setBookName("The little prince");
            book.setPubDate(new Date());

            // book data DB Insert
            // em.persist(entity)
            em.persist(book);

            // 트랜잭션 끝났다.

            // 수정 em.update() 같은 별도의 수정 메서드가 존재하지 않음.
            // 어떤 엔티티가 변경되었는지만 JPA가 추적함.

            // UPDATE MEMBER SET BOOK_NAME = "다큰왕자", where id = "book1";
            book.setBookName("어른 왕자");

            // 한 행 조회 : em.find(조회할 엔티티의 타입, @Id로 매핑한 필드 값)
            Book findBook = em.find(Book.class, "1L");
            System.out.println(findBook.getBookName());

            // 엔티티 삭제 : em.remove(삭제할 entity);
            // DELETE FROM BOOK WHERE id = "book1";
            // em.remove(findBook);
            tx.commit();
        } catch (Exception e) { // 매개변수의 다형성
            em.close();
            emf.close();
        }
    }
}

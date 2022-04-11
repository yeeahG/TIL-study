package dev.hibernate.model;

import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

/**
 * Entity 어노테이션 : '객체와 테이블을 매핑(Mapping)'
 * : 해당 class를 JPA가 관리하는 Entity로 인식하게함
 * 별도의 Table Annotation(@Table)을 지정하지 않으면 해당 클래스의 이름(BOOK)으로 테이블이 생성됨
 * -> 'BOOK' Table
 * 
 * Entity Annotation 적용시 주의할 점
 * 1. 기본생성자(Default Constructor) 필수(JPA가 엔티티 객체를 생성하라 할 때 기본 생성자를 활용하기 때문이다.)
 * 2. 값을 저장할 필드에 final을 사용하면 안됨.
 */

@Entity
// default 값이 BOOK이고 다른 값 을 집어넣으면 해당이름으로 변경된 테이블 생성
@Table(name = "BOOK")
public class Book {

    /**
     * JPA의 기본키 생성 전략(크게 2가지)
     * 1. 직접할당 : 기본키를 애플리케이션에서 직접 할당
     * 2. 자동생성 : 대리키 활용(strategy = generationType 1) 2) 3)
     * 
     * 1) IDENTITY : 기본키 생성을 DB한테 위임(MYSQL의 auto_invrement)
     * 2) SEQUENCE : DB의 시퀀스 기능을 활용(Oracle에서 지원, MySQL은 미지원)
     * 3) TABLE : 키 생성 테이블을 사용(키를 생성해주는 별도의 테이블을 만들고, 시퀀스처럼 사용, 모든 DB에서 사용가능)
     * 
     * 직접 할당 방식을 사용하기 위해서는 @Id만 쓰면됨
     * 예)
     * Book book = new Book();
     * book.setId("book1");
     * 
     * 
     * 자동 생성 방식을 사용하기 위해서는 @Id + GeneratedValue를 추가, 원하는 키 생성 전략 선택.
     */
    @Id // primary key(기본키) 매핑 설정
    // private String id;

    // MYSQL에서 사용하기 위함
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 자동 키 생성
    private Long id;

    /**
     * @column annotation : 필드와 컬럼 매핑
     */

    @Column(name = "book_name", nullable = false) // 컬럼이름을 해당 처럼 바꾸어서 만들고 null값은 불가능하다.(Not Null)
    private String bookName; // camelCase(JAVA) / snake_case(book_name)\

    @Column(name = "book_author")
    private String author;

    // private String publishing : 이런게 추가되었을때 일이 늘어난다.

    @Temporal(TemporalType.TIMESTAMP) // java.util.date, util.Calendar 매핑할때 사용
    // TemporalType.DATE : 날짜, DB date 타입과 매핑(ex. 2022-03-03)
    // TemporalType.TIME : 시간, DB time 타입과 매핑(ex. 09:30:23)
    // TemporalType.TIMESTAMP : 날짜와 시간, DB의 timestamap 타입과 매핑(ex.2022-12-23
    // 09:50:24)

    @Column(name = "pub_date")
    private Date pubDate;

    public Book() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getBookName() {
        return bookName;
    }

    public void setBookName(String bookName) {
        this.bookName = bookName;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public Date getPubDate() {
        return pubDate;
    }

    public void setPubDate(Date pubDate) {
        this.pubDate = pubDate;
    }

}

package dev.book.bookorder.model.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Entity

@Getter
@Setter

@ToString

@Table(name = "ORDERS")
public class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ORDER_ID")
    private Long id;

    private String userName;
    private String address;
    private int totalPrice;

    @ManyToOne // 다 : 1 관계
    @JoinColumn(name = "BOOK_ID") // 외래키 하는 방법(Book.java id값)
    private Book book; // order(다) : book(1)
}

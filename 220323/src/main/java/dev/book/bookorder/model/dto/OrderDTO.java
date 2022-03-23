package dev.book.bookorder.model.dto;

import dev.book.bookorder.model.entity.Book;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@ToString
@Getter
@Setter

// 여러가지의 값을 한번에 받아오기 위해 생성
public class OrderDTO {
    // Orders Table과 맞출 필요는 없다. (DB와 관련되지 않았음.)

    // cart.jsx의 body부분을 감싸줄
    public OrderDTO(String userName, String address, String bookTitle, int totalPrice) {
        this.userName = userName;
        this.address = address;
        this.bookTitle = bookTitle;
        this.totalPrice = totalPrice;
    }

    private String userName;
    private String address;
    private String bookTitle;
    private String bookAuthor;
    private int totalPrice;

    private Book book; // 연관관계 반대로 설정했기 때문에

}

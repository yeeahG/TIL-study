package dev.book.bookorder.model.dto;

import dev.book.bookorder.model.entity.Book;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter

public class BookDTO {
    private Long id;
    private String name;
    private String description;
    private String author;
    private int price;
    private int amount;

    public BookDTO(Book book) {
        // Book Entity had value
        this.id = book.getId();
        this.name = book.getName();
        this.description = book.getDescription();
        this.author = book.getAuthor();
        this.price = book.getPrice();
    }
}

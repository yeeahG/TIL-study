package dev.book.bookorder.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import dev.book.bookorder.model.entity.Book;

// JpaRepository<내가 사용하는 엔티티 타입, 기본키 타입> 인터페이스를 상속 
public interface BookRepository extends JpaRepository<Book, Long> {
    // Book의 String name에 접근한다.(단, 규칙에 맞게 작성해야 함)
    Book findByName(String name);
}

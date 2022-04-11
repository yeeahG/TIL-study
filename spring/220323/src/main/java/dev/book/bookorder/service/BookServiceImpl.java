package dev.book.bookorder.service;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import dev.book.bookorder.model.dto.BookDTO;
import dev.book.bookorder.model.entity.Book;
import dev.book.bookorder.repository.BookRepository;

@Service // 서비스 클래스 임을 나타냄
public class BookServiceImpl implements BookService {

    @Autowired // 컴포넌트로 등록
    private BookRepository bookRepository; // 구현체 인스턴스 주입

    @Override
    public List<BookDTO> findAllBooks() {
        List<Book> list = bookRepository.findAll(); // findAll() : JPA Repository에 있는 메서드

        // 형 변환 (이 값을 모았다가 list로 바꿔)
        List<BookDTO> result = list.stream().map(r -> new BookDTO(r)).collect(Collectors.toList());
        return result;

        // Book controller로 날아감
    }

}
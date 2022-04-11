package dev.book.bookorder.controller;

import java.util.List;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import dev.book.bookorder.model.dto.BookDTO;
import dev.book.bookorder.service.BookService;

// 책에 대한 정보 조회
// 컴포넌트로 등록(어플리케이션 실행시 다 빈으로 등록)
// @Controller(@Componenet가 각 클래스의 이름에 맞게 직관적인 명칭으로 변환된 것) + @ResponseBody

@CrossOrigin(origins = "*") // 차후 배포를 위해서는 수정이 필요
@RestController
@RequestMapping("/api/v1/books") // how to take front request, GET : localhost:8090/api/v1/books~
public class BookController {

    private final BookService bookService;

    // 생성자
    // BookServiceImpl.java의 값이 bookService로 들어옴
    public BookController(BookService bookService) {
        this.bookService = bookService;
    }

    @GetMapping() // GET : /api/v1/books
    // controller -> service -> repository -> DB 순으로 데이터 전달
    public List<BookDTO> findAllBooks() {
        // 전체 책 데이터 조회
        // 그대로 List<BookDTO>줌

        return bookService.findAllBooks();

    }
}

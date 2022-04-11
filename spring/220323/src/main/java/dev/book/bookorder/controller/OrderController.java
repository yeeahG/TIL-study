package dev.book.bookorder.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import dev.book.bookorder.model.dto.OrderDTO;
import dev.book.bookorder.service.OrderService;

// 주문관련
@CrossOrigin(origins = "*") // 차후 배포를 위해서는 수정이 필요
@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {

    private final OrderService orderService;

    public OrderController(OrderService orderService) {
        this.orderService = orderService;
    }

    @PostMapping() // POST : ~/api/v1/orders // 무언가 올린다~
    public void insertOrder(@RequestBody OrderDTO orderDTO) {
        // System.out.println(orderDTO);

        orderService.insertOrder(orderDTO);

    }
}

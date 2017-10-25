package main

import "fmt"

func CountBits(num int) int {
    counter := 0
    for num > 0 {
        counter = counter + num & 1
        num = num >> 1
    }
    return counter
}

func main() {
    fmt.Println(CountBits(15333333333442434))
    fmt.Println(CountBits(0))
    fmt.Println(CountBits(-10))
}

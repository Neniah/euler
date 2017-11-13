package main
import "fmt"


func Fibonacci(n int)  int{
  if n < 2 {
    return n
  } else {
    return Fibonacci(n-2) + Fibonacci(n-1)
  }
}

func main(){
  sum := 0
  fibo := 0
  for i:= 0; fibo <= 4000000; i++ {
    fibo = Fibonacci(i)
    if fibo % 2 == 0 {
      sum += fibo
    }
  }
  fmt.Println(sum)
}

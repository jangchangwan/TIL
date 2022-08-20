function add(a: number, b: number): number {
  return a + b;
}
// 반환값도 타입 결정 가능
// 정해놓은 타입이 아닌 경우 코드상에서 error 발생
// 코드 자동완성 기능이 잘 되어있다.
var result2 = add(10, 20)

result2.toLocaleString();
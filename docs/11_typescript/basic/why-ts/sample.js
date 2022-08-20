function sum(a, b) {
  return a + b;
}

var result = sum(10, '20'); // 1020 자바스크립트 특성상 문자로 합해진다

result.toLocalString();

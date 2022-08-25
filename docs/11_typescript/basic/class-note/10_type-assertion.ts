// 타입 단언(type assertion)

var a;
a = 20
a = 'a'
var b = a as string;  // 추론한 타입이 다를 경우 개발자가 선언해주는 경우

//  DOM API 조작
var div = document.querySelector('div');
if (div) {
  div?.innerText
}

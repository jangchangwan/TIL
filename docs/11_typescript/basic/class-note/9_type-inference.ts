// 타입 추론

// 타입 추론 기본 1
// var a = 'abc';

// 기본값 설정 값을 넘기지 않을 경우 10이라는 값을 넘긴다.
// 숫자와 문자를 더할경우 문자가 된다.
function getB(b = 10) {
  var c = 'hi'
  return b + c;
}

// 타입 추론 기본 2

interface Dropdown1<T> {
  value: T;
  title: string;
}

var shoppingItem: Dropdown1<string> = {
  value: "쇼핑",
  title: "물건이름",
}

// 타입 추론 기본 3
interface Dropdown2<T> {
  value: T;
  title: string;
}

interface DetailDropdown<K> extends Dropdown2<K>{
  description: string;
  tag: K;
}

var detailItem: DetailDropdown<string> = {
  title: 'abc',
  description: 'ab',
  value: 'ab',
  tag: '영화'
}


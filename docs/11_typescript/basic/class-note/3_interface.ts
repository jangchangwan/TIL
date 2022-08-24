interface User {
  age: number;
  name: string;
}


// 변수에 인터페이스 활용
var seho: User = {
  age: 33,
  name: '세호'
}
const capt = {
  name: '캡틴',
  age: 100,
}
// 함수에 인터페이스 활용
function getUser(user: User) {
  console.log(user)
}

getUser(capt);

// 함수의 스펙(구조)에 인터페이스를 활용

interface SumFuction {
  // 인자와 반환값을 정할 수 있다
  (a: number, b: number):number
}

let sum: SumFuction
sum = function(a:number, b:number):number {
  return a + b
}

// 인덱싱
interface StringArray {
  [index: number]: string;
}

var arr_1: StringArray = ['a', 'b', 'c']
// 문자열만 저장되므로 숫자는 저장 X
// arr_1[0] = 10
arr_1[1] = 'a'

var arr = ['a','b','c'];
console.log(arr[0]); // 'a'


// 딕셔너리 패턴
// RegExp 정규표현식
interface StringRegexDictionary {
  [key: string]: RegExp
}

var obj:StringRegexDictionary = {
  sth: /abc/,
  // css 확장자로 끝나는 파일들
  cssFile: /\.css$/,
  // js 확장자로 끝나는 파일들
  jsFile: /\.js$/,
}

Object.keys(obj).forEach(function(value){
  console.log(value)
})

// 인터페이스 상속 

interface Person {
  name: string;
  age: number;
}

// 상속받을 경우 Person에 있는 타입들도 정의를 받아야한다.
interface Developer extends Person{
  language: string;
}

var captain: Developer = {
  language : 'ts',
  age : 100,
  name : 'captain'
}
// 연산자를 이용한 타입정하기

// 문자열 또는 숫자를 받아쓴다.
// 타입 가드 : 특정 타입으로 타입의 범위를 좁혀나가는 과정
function logMessage(value: string | number):void{
  console.log(value)
  if (typeof value === "number"){
    // 속성에 따른 메소드를 불러와준다
    value.toLocaleString();
  }
  else if (typeof value === "string"){
    value.toString();
  }
  else {
    throw new TypeError('value must be string or number')
  }
} 

logMessage('hello')
logMessage(100)


interface Developer_1 {
  name: string;
  skill: string;
}

interface Person {
  name: string;
  age: number;
}

// 인터페이스의 경우 교집합만 가능하다, 혼돈하지 말 것
function askSomeone (someone: Developer_1 | Person) {
  someone.name
  // someone.skill
  // someone.age
}
askSomeone({name: '디펠로퍼', skill: '웹 개발'})
askSomeone({name:'캡틴', age: 100})


// & 인터섹션 타입 소개
// 3가지를 만족하는 타입은 존재할 수 없으므로 never라고 뜨게 된다
var temp: string & number & boolean;

// 합집합?
function askSomeone1 (someone: Developer_1 & Person) {
  someone.name
  someone.skill
  someone.age
}

askSomeone1({name:'캡틴', age: 100, skill:'웹 기술'})
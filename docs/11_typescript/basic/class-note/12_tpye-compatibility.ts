// 인터페이스

interface Developer {
  name: string;
  skill: string;
}

interface Person {
  name: string
}

var developer: Developer;
var person: Person;

// 구조적을 더 큰 인터페이스가 호환가능하다 
// developer = person
// person = developer


var add = function(a: number) {
  // ...
}
var sum = function(a: number, b: number) {
  // ...
}

sum = add;
// add = sum;
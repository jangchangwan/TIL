// function logText(text) {
//   console.log(text);
//   return text;
// } 


// function logText<T>(text: T): T {
//   console.log(text);
//   return text;
// }
// logText<string>('하이')


// function logText(text:string) {
//   console.log(text);
//   text.split('').reverse().join('');
//   return text;
// } 

// function logNumber(num:number) {
//   console.log(num);
//   return num;
// } 

// logText('abc');
// logText(10);
// logText(true);

//  제너릭을 통해 타입2가지이상를 사용하기
function logText<T>(text:T):T {
  console.log(text);
  return text;
} 

const str = logText<string>('문자열')
str.split('')
logText<number>(123)
// const a = logText('a');
// logText(10);


// 인터페이스에 제네릭을 선언하는 방법

interface Dropdown<T> {
  value : T;
  selected: boolean;
}

const obj : Dropdown<string> = {value: 'abc', selected: false}


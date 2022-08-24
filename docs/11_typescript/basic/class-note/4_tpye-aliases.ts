// 타입 별칭
interface Person_1 {
  name: string;
  age: number;
}


type Person_2 = {
  name: string;
  age: number;
}

// 인터페이스
var seho: Person_1 = {
  name : '세호',
  age : 30
}

// 타입 별칭 마우스를 가져 다 댈경우 필요한 타입이 뜨게 된다
var changwan: Person_2 = {
  name : "changwan",
  age: 30,
}

type Todo = {id: number, title:string, done:boolean}
function getTodo(todo: Todo){
  console.log(todo);
  
}
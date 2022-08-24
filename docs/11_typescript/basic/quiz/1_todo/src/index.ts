// type Todo = {
//   id: number;
//   title: string;
//   done: boolean;
// };
// 인터페이스 활용으로 중복코드 줄이기
interface Todo {
  id: number;
  title: string;
  done: boolean;
}


let todoItems: Todo[];



// api
function fetchTodoItems(): Todo[] {
  const todos = [
    { id: 1, title: '안녕', done: false },
    { id: 2, title: '타입', done: false },
    { id: 3, title: '스크립트', done: false },
  ];
  return todos;
}

// crud methods
function fetchTodos(): object[] {
  const todos = fetchTodoItems();
  return todos;
}
// 아무것도 지정하지 않은 경우 any로 타입이 지정된다
// 함수에 반환값이 없을 경우 void로 지정해줘야 한다.
function addTodo(todo: Todo): void {
  todoItems.push(todo);
}

function deleteTodo(index: number): void {
  todoItems.splice(index, 1);
}

function completeTodo(index: number, todo: Todo): void {
  todo.done = true;
  todoItems.splice(index, 1, todo);
}

// business logic
function logFirstTodo(): object {
  return todoItems[0];
}

function showCompleted(): object[] {
  return todoItems.filter(item => item.done);
}

// TODO: 아래 함수의 내용을 채워보세요. 아래 함수는 `addTodo()` 함수를 이용하여 2개의 새 할 일을 추가하는 함수입니다.
function addTwoTodoItems():void {
  let todo_1 = { id: 4, title: '너무', done: false }
  let todo_2 = { id: 5, title: '어려워', done: false }
  addTodo(todo_1)
  addTodo(todo_2)
  // addTodo() 함수를 두 번 호출하여 todoItems에 새 할 일이 2개 추가되어야 합니다.
}

// NOTE: 유틸 함수
function log(): void {
  console.log(todoItems);
}

todoItems = fetchTodoItems();
addTwoTodoItems();
log();

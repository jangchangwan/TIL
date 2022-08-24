// 두가지 데이터를 동시에 사용
interface Email {
  value: string;
  selected: boolean;
}
interface Productnumber {
  value: number;
  selected: boolean;
}
// 제너릭을 통해 원하는 데이터타입을 정해서 사용
interface value<T> {
  value: T;
  selected: boolean;
}

const emails: value<string>[] = [
  { value: 'naver.com', selected: true },
  { value: 'gmail.com', selected: false },
  { value: 'hanmail.net', selected: false },
];



const numberOfProducts: value<number>[] = [
  { value: 1, selected: true },
  { value: 2, selected: false },
  { value: 3, selected: false },
];

function createDropdownItem(item: value<string> | value<number>) {
  const option = document.createElement('option');
  option.value = item.value.toString();
  option.innerText = item.value.toString();
  option.selected = item.selected;
  return option;
}

// NOTE: 이메일 드롭 다운 아이템 추가
emails.forEach(function (email) {
  const item = createDropdownItem(email);
  const selectTag = document.querySelector('#email-dropdown');
  selectTag.appendChild(item);
});

numberOfProducts.forEach(function (product) {
  const item = createDropdownItem(product);
  const selectTag = document.querySelector('#product-dropdown');
  selectTag.appendChild(item);
});
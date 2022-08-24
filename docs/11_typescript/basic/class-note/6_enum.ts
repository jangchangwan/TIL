//  이넘

// 별도의 값을 넣지않는 경우 0으로 출력
enum Shoes {
  Nike,
  Adidas ="아디다스",
}

var myShoes = Shoes.Adidas;
console.log(myShoes); // 0

enum Answer {
  Yes = 'Y',
  No = 'N'
}

// 예제
function askQuestion(answer: Answer) {
  if (answer === Answer.Yes) {
    console.log('정답입니다.')
  }
  else if (answer === Answer.No) {
    console.log('오답입니다.');
  }
}

askQuestion(Answer.Yes)
// askQuestion('예스')
// askQuestion('y')
// askQuestion('yes')
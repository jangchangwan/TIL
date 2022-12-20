// 소수 체크
function isPrimeNumber(number) {
  if (number <= 1) {
      return false;
  }
  for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i === 0) {
          return false;
      }
  }
  return true;
}

function solution(n, k) {
  let count = 0;
  // 진수변환
  let num = n.toString(k); 
  let numArr = num.split("0");

  for (let i = 0; i < numArr.length; i++) {
      if (isPrimeNumber(Number(numArr[i]))) {
          count++;
      }
  }
  return count;
}
function solution(word) {
  const stack = [];

  for (let i = 0; i < word.length; i++) {
    if (!stack.length || stack[stack.length - 1] !== word[i])
      stack.push(word[i]);
    else stack.pop();
  }
  if (stack.length) {
    return 0;
  }
  return 1;
}

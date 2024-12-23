const fs = require('fs');
const input = fs
  .readFileSync('input.txt', 'utf-8')
  .toString()
  .trim()
  .split('\n');

function solution() {
  // 중복 제거
  const removeRepeatNumber = [...new Set(input.slice(1, input.length))];

  // 스펠링 순으로 정렬
  const sortingWords = removeRepeatNumber.sort((a, b) => a.localeCompare(b));

  // 글자 순으로 한번 더 정렬
  const sortingWords2 = sortingWords.sort((a, b) => a.length - b.length);

  return sortingWords2.join('\n');
}

console.log(solution());

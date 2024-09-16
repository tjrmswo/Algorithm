const fs = require('fs');
const input = fs.readFileSync('input.txt', 'utf-8').toString().trim();

function solution(word) {
  let smallest = null;

  // 첫 번째 컷: 0부터 i까지
  for (let i = 1; i < word.length - 1; i++) {
    // 두 번째 컷: i+1부터 j까지
    for (let j = i + 1; j < word.length; j++) {
      // 각 절단별로 세 부분을 나누고 각각 뒤집기
      const part1 = word.substring(0, i).split('').reverse().join('');
      const part2 = word.substring(i, j).split('').reverse().join('');
      const part3 = word.substring(j).split('').reverse().join('');

      // 합쳐서 새로운 단어 생성
      const newWord = part1 + part2 + part3;

      // 가장 작은 단어 찾기
      if (smallest === null || newWord < smallest) {
        smallest = newWord;
      }
    }
  }
  return smallest;
}

console.log(solution(input));

const filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split('\n');

function solution() {
  // 단어를 나누는 기준 띄어쓰기 또는 <>로 나눈다
  let answer = input[0];
  const regExp = /<[a-z\s]+>|[a-z0-9]+/g;

  answer = answer.replace(regExp, (word) => {
    return word.startsWith('<') ? word : word.split('').reverse().join('');
  });

  console.log(answer);
}

solution();

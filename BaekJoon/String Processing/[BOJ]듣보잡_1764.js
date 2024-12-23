const filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split('\n');

function solution() {
  const [N, M] = input.shift().split(' ').map(Number);

  const Nset = new Set();
  const Mset = new Set();
  const answer = [];

  input.forEach((el, idx) => {
    if (idx < N) {
      Nset.add(el);
    } else {
      Mset.add(el);
    }
  });

  Nset.forEach((el) => {
    if (Mset.has(el)) answer.push(el);
  });

  answer.sort();
  console.log(answer.length + '\n' + answer.join('\n'));
}

solution();

const fs = require('fs');
const input = fs
  .readFileSync('input.txt', 'utf-8')
  .toString()
  .trim()
  .split('\n');

function solution() {
  const reverse = input[0].split('').reverse().join('');
  console.log(reverse);
}

solution();

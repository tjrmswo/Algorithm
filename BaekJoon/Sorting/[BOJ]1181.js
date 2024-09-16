const fs = require('fs');
const input = fs
  .readFileSync('input.txt', 'utf-8')
  .toString()
  .trim()
  .split('\n');

function solution() {
  input.shift();

  s_arr = [...new Set(input)];

  s_arr = s_arr
    .sort((a, b) => a.length - b.length || a.localeCompare(b))
    .join('\n');

  return s_arr;
}

console.log(solution(input));

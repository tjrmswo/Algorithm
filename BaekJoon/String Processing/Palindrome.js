const fs = require('fs');
const input = fs
  .readFileSync('input.txt', 'utf-8')
  .toString()
  .trim()
  .split('\n');
const reg = /[`~!@#$%^&*()_|+\-=?;:'",.<>\{\}\[\]\\\/ ]/gim;

function solution() {
  const w = input[0].replace(reg, '').split('').join('').toLowerCase();
  const s = input[0]
    .replace(reg, '')
    .split('')
    .reverse()
    .join('')
    .toLowerCase();

  if (s !== w) {
    console.log('회문이 아닙니다.');
    return;
  }

  console.log('회문입니다.');
}

solution();

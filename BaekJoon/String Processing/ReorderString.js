const fs = require('fs');
const input = fs
  .readFileSync('input.txt', 'utf-8')
  .toString()
  .trim()
  .split('\n');

function solution() {
  const array = JSON.parse(input[0]);

  const data = array.sort(
    (a, b) => a.price - b.price || a.name.localeCompare(b.name)
  );

  console.log(data);
}

solution();

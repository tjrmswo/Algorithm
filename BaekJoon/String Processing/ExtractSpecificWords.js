const fs = require('fs');
const input = fs
  .readFileSync('input.txt', 'utf-8')
  .toString()
  .trim()
  .split('\n');

function solution() {
  const word = input[0].toLowerCase().replace(/[,.]/g, '').split(' ');
  const excludeWord = 'love';

  const wordCount = {};
  let maxCount = 0;
  const resultWord = [];

  word.forEach((w) => {
    if (w !== excludeWord) {
      wordCount[w] = (wordCount[w] || 0) + 1;

      if (wordCount[w] >= maxCount) {
        maxCount = wordCount[w];
        resultWord.push(w);
      }
    }
  });

  const asc = [...new Set(resultWord)].sort((a, b) => a.localeCompare(b));

  // console.log(asc[0]);

  return asc[0];
}

solution();

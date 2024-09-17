const fs = require('fs');

const input = fs
  .readFileSync('input.txt', 'utf-8')
  .toString()
  .trim()
  .split('\n');

const vow = ['a', 'e', 'i', 'o', 'u'];
const allowedStr = ['ee', 'oo'];

function solution(words) {
  for (let i = 0; i < words.length; i++) {
    const word = words[i];
    if (word === 'end') {
      break;
    }

    let vowelCount = 0;
    let consonantCount = 0;
    let isAcceptable = true;

    if (!vow.some((element) => word.includes(element))) {
      console.log(`<${word}> is not acceptable.`);
      continue;
    }

    for (let j = 0; j < word.length; j++) {
      const currentChar = word[j];
      const nextChar = word[j + 1];

      if (
        currentChar === nextChar &&
        !allowedStr.includes(currentChar + nextChar)
      ) {
        console.log(`<${word}> is not acceptable.`);
        isAcceptable = false;
        break;
      }

      if (vow.includes(currentChar)) {
        consonantCount = 0;
        vowelCount++;
        if (vowelCount >= 3) {
          console.log(`<${word}> is not acceptable.`);
          isAcceptable = false;
          break;
        }
      } else {
        vowelCount = 0;
        consonantCount++;
        if (consonantCount >= 3) {
          console.log(`<${word}> is not acceptable.`);
          isAcceptable = false;
          break;
        }
      }
    }

    if (isAcceptable) {
      console.log(`<${word}> is acceptable.`);
    }
  }
}

solution(input);

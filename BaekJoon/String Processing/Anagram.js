const fs = require('fs');
const input = fs
  .readFileSync('input.txt', 'utf-8')
  .toString()
  .trim()
  .split('\n');

function solution() {
  const words = JSON.parse(input[0]);

  const Anagram = {};

  // 애너그램 그룹화
  words.forEach((word) => {
    const key = word.split('').sort().join('');

    if (!Anagram[key]) {
      Anagram[key] = [];
    }

    Anagram[key].push(word);
  });

  // 그룹을 키의 정렬된 순서에 따라 정렬
  const sortedKeys = Object.keys(Anagram).sort();

  // 정렬된 키 순서로 최종 결과 배열 구성
  const result = sortedKeys.map((key) =>
    Anagram[key].sort((a, b) => a.localeCompare(b))
  );

  console.log(result); // 최종 결과 출력
}

solution();

const filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split('\n');

function solution() {
  const [N, M] = input[0].split(' ');
  const graph = input.slice(1);

  const visited = [];
  const needVisit = [];

  // 사용되는 그래프의 인접 리스트 형태로 변환
  const adjacencyList = {};

  graph.forEach((connection) => {
    const [node1, node2] = connection.split(' ');
    if (!adjacencyList[node1]) adjacencyList[node1] = [];
    if (!adjacencyList[node2]) adjacencyList[node2] = [];
    adjacencyList[node1].push(node2);
    adjacencyList[node2].push(node1);
    console.log(adjacencyList);
  });

  needVisit.push('1');

  while (needVisit.length !== 0) {
    const node = needVisit.pop(); // 스택 구조 사용 (LIFO)

    if (!visited.includes(node)) {
      visited.push(node);
      const neighbors = adjacencyList[node] || [];

      neighbors.forEach((neighbor) => {
        if (!visited.includes(neighbor)) {
          needVisit.push(neighbor);
        }
      });
    }
  }

  console.log('Visited Nodes:', visited);
}

solution();

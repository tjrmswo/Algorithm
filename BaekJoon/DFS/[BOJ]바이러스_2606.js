const filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
const input = require('fs')
  .readFileSync(filePath, 'utf-8')
  .toString()
  .trim()
  .split('\n');

// 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
// 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성
function solution() {
  const graph = input.slice(2);

  // 1을 방문한 노드 카운트
  let cnt = 0;

  // 방문했던 노드
  const visited = new Set();
  // 방문할 노드
  const needVisit = ['1'];
  // 노드 관계성
  const List = {};

  graph.forEach((g) => {
    const [node1, node2] = g.split(' ');

    if (!List[node1]) List[node1] = [];
    if (!List[node2]) List[node2] = [];

    List[node1].push(node2);
    List[node2].push(node1);
  });

  while (needVisit.length !== 0) {
    const node = needVisit.pop();
    if (!visited.has(node)) {
      visited.add(node);
      if (node !== '1') {
        cnt++;
      }

      const neighbors = List[node] || []; // 이웃 노드가 없으면 빈 배열 반환

      neighbors.forEach((neighbor) => {
        if (!visited.has(neighbor)) {
          needVisit.push(neighbor);
        }
      });
    }
  }

  console.log(cnt);
}

solution();

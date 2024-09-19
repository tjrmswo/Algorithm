class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.front = null;
    this.rear = null;
    this.length = 0;
  }

  enqueue(value) {
    const newNode = new Node(value);
    if (this.length === 0) {
      this.front = newNode;
      this.rear = newNode;
    } else {
      this.rear.next = newNode;
      this.rear = newNode;
    }
    this.length++;
  }

  dequeue() {
    if (this.length === 0) return -1;
    const value = this.front.value;
    this.front = this.front.next;
    this.length--;
    if (this.length === 0) {
      this.rear = null;
    }
    return value;
  }

  peekFront() {
    return this.length > 0 ? this.front.value : -1;
  }

  peekBack() {
    return this.length > 0 ? this.rear.value : -1;
  }

  isEmpty() {
    return this.length === 0 ? 1 : 0;
  }

  size() {
    return this.length;
  }
}

const fs = require('fs');
const input = fs.readFileSync('input.txt', 'utf-8').trim().split('\n');

function solution(order) {
  const queue = new Queue();
  const results = [];
  const orders = order.slice(1);

  for (let i = 0; i < orders.length; i++) {
    const command = orders[i];
    if (command.startsWith('push')) {
      const value = parseInt(command.split(' ')[1], 10);
      queue.enqueue(value);
    } else if (command === 'front') {
      results.push(queue.peekFront());
    } else if (command === 'back') {
      results.push(queue.peekBack());
    } else if (command === 'size') {
      results.push(queue.size());
    } else if (command === 'empty') {
      results.push(queue.isEmpty());
    } else if (command === 'pop') {
      results.push(queue.dequeue());
    }
  }

  process.stdout.write(results.join('\n') + '\n');
}

solution(input);

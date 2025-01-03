const input = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("\n")

let num = input[0];
let tower = input[1].split(" ");
tower = tower.map((v) => +v);
let stack = [];
let result = [];


for (let i = 0; i < num; i++) {
  if (stack.length == 0) {
    stack.push([i+1, tower[i]]);
  } else if (stack[stack.length - 1][1] < tower[i]) {
    while (stack.length > 0 && stack[stack.length - 1][1] < tower[i]) {
      stack.pop();
    }
    stack.push([i+1, tower[i]]);
  } else {
    stack.push([i+1, tower[i]]);
  }

  if (stack.length == 1) result.push(0);
  else result.push(stack[stack.length - 2][0]);
}

console.log(result.join(" "));
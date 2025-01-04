const [first, ...input] = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("\n");

let N = Number(first.trim().split(" "));
const rope = input.map(Number);
let ans = [];

const solution = () => { 
    rope.sort((a, b) => a - b);
    
    for (x of rope) {
        ans.push(x * N);
        N -= 1;
    }

    console.log(Math.max(...ans));
}

solution();
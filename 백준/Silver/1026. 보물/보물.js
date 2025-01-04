const [first, ...input] = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("\n");

const N = Number(first);
const arr = input.map((line) => line.trim().split(" ").map(Number));
let sum = 0;

const solution = () => { 
    arr[0].sort((a, b) => b - a);
    arr[1].sort((a, b) => a - b);

    for (let i = 0; i < N; i++){
        sum += arr[0][i] * arr[1][i];
    }

    console.log(sum);
}

solution();
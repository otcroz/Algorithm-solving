const [first, input] = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("\n");

const N = Number(first);
const arr = input.split(" ").map(Number);
let res = [];

const solution = () => {
    let sum = 0;
    arr.sort((a, b) => a - b);

    for (let i = 0; i < N; i++){
        sum += arr[i];
        res.push(sum);
    }

    let minTime = res.reduce((acc, cur) => acc + cur, 0);
    console.log(minTime);
    
}

solution();
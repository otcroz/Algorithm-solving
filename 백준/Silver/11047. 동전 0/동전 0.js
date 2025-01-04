const [first, ...input] = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("\n");

let [N, target] = first.trim().split(" ");
const value = input.map(Number);
let cnt = 0;

const solution = () => { 
    for (let i = N - 1; i >= 0; i--){
        cnt += Math.floor(target / value[i]);
        target %= value[i];
    }

    console.log(cnt);
}

solution();
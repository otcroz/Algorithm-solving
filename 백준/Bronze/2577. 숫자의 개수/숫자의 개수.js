const input = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("\n").map(Number);

const solution = () => {
    const calc = input.reduce((acc, cur) => 
        acc * Number(cur)
    , 1).toString();
    //const calc = (input[0] * input[1] * input[2]).toString();
    const arr = Array(10).fill(0);

    for (num of calc) { 
        arr[Number(num)]++;
    }
    
    console.log(arr.join("\n"));
}

solution()
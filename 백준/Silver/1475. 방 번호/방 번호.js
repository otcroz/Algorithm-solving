const input = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("").map(Number);

const solution = () => {
    const arr = Array(10).fill(0);

    for (num of input) {
        if (num == 6 || num == 9) {
            if (arr[6] > arr[9]) { arr[9]++; }
            else { arr[6]++; }
        } else {
            arr[num]++;
        }
    }
    console.log(Math.max(...arr));
    
}

solution()
const input = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("\n")

const length = Number(input[0]);
const arr = input[1].split(" ").map(Number).sort((a,b) => a-b); // 오름차순 정렬렬
const x = Number(input[2]);

const solution = () => {
    let count = 0;
    let left = 0;
    let right = length - 1;

    while (left < right) {
        let sum = arr[left] + arr[right];
        
        if (sum == x) {
            count++;
            left++;
        } else if (sum < x) {
            left++;
        } else {
            right--;
        }
    }
    console.log(count);
}

solution();
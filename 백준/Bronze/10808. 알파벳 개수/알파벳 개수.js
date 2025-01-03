const input = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim();

const solution = () => { 
    let array = Array(26).fill(0); // 0이 26개 들어간 배열
    for (let i = 0; i < input.length; i++) { 
        const cur = input.charCodeAt(i);
        array[cur - 97]++;
    }

    console.log(array.join(" "));
}

solution()
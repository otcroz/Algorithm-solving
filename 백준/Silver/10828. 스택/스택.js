const input = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("\n")

const solution = () => {
    const n = Number(input[0]);
    let stack = [];
    let answer = [];

    for (let i = 1; i < n+1; i++) {
        const command = input[i].split(" ");
        

        switch (command[0].trim()) {
            case "push": stack.push(Number(command[1])); break;
            case "pop": stack.length != 0 ? answer.push(stack.pop()) : answer.push(-1); break;
            case "size": answer.push(stack.length); break;
            case "empty": stack.length == 0 ? answer.push(1) : answer.push(0); break;
            case "top": stack.length == 0 ? answer.push(-1) : answer.push(stack[stack.length - 1]); break;
        }
    }

    console.log(answer.join("\n"));
}

solution();
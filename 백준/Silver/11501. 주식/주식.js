const [first, ...input] = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("\n");

const T = Number(first);

const solution = () => {
    for (let i = 0; i < T * 2; i+=2){
        const N = Number(input[i]);
        const stock = input[i + 1].split(" ").map(Number);
        let profit = 0;
        let maxProfit = 0;

        // 역순
        for (let i = N - 1; i >= 0; i--){
            if (maxProfit < stock[i]) maxProfit = stock[i];
            else if (maxProfit > stock[i]) profit += maxProfit - stock[i];
        }

        console.log(profit);
    }
}

solution();
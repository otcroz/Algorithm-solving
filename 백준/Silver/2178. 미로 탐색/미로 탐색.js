const [first, ...input] = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("\n")

const [m, n] = first.trim().split(" ").map(Number);
const graph = input.map((line) => line.trim().split("").map(Number));

let queue = [];
dx = [-1, 1, 0, 0];
dy = [0, 0, -1, 1];

const bfs = (i, j) => {
    queue.push([i, j]);

    while (queue.length) {
        let [x, y] = queue.shift();

        for (let k = 0; k < 4; k++){
            let nx = x + dx[k];
            let ny = y + dy[k];
            
            if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                if (graph[nx][ny] === 1) {
                    graph[nx][ny] = graph[x][y] + 1;
                    queue.push([nx, ny]);
                }
            }
        }
    }
};

const solution = () => { 
    bfs(0, 0);
    console.log(graph[m-1][n-1]);
}

solution();
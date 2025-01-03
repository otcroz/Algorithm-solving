const [first, ...input] = require('fs').readFileSync(process.platform == 'win32' ? "./input.txt" : '/dev/stdin').toString().trim().split("\n")

const [m, n] = first.split(" ").map(Number);
const graph = input.map((line) => {
    return line.trim().split(" ").map(Number);
})
//console.log(JSON.stringify(graph))
const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];
const res = [];
const arr = [];
const visited = Array(m).fill(null).map(() => Array(n).fill(0));

const solution = () => {
    const dfs = (j, k) => {
        let cnt = 1;
        arr.push([j, k]);

        while (arr.length > 0) {
            const [nx, ny] = arr.pop();
            for (let i = 0; i < 4; i++){
                if (0 <= dx[i] + nx && nx + dx[i] < m && 0 <= ny + dy[i] && ny + dy[i] < n
                    && visited[nx + dx[i]][ny + dy[i]] === 0
                    && graph[nx + dx[i]][ny + dy[i]] === 1) {
                    cnt += 1;
                    visited[nx + dx[i]][ny + dy[i]] = 1;
                    arr.push([nx + dx[i], ny + dy[i]]);
                }
            }
        }
        res.push(cnt);
    }

    for (let i = 0; i < m; i++){
        for (let j = 0; j < n; j++){
            if (visited[i][j] === 0 && graph[i][j] === 1) { 
                visited[i][j] = 1;
                dfs(i, j);
            }
        }
    }

    console.log(res.length);
    console.log(res.length === 0 ? 0 :Math.max(...res));

}

solution();
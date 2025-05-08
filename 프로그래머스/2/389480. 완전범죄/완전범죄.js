function solution(info, n, m) {
    
    let dp = Array.from({length: info.length + 1}, () =>{
        return Array(m).fill(Infinity);
    })
    
    dp[0][0] = 0;
    
    for(let i = 1; i <= info.length; i++){
        let [a, b] = info[i-1];
        for (let j = 0; j < m; j++){
            dp[i][j] = Math.min(dp[i-1][j] + a, dp[i][j]);
            
            if (j + b < m){
                dp[i][j + b] = Math.min(dp[i-1][j], dp[i][j + b]);
            }
        }
    }
    
    let min = Infinity;
    
    dp[info.length].map((item) => {
        if(item < n){
            min = Math.min(item, min);
        }
    })
    
    return min === Infinity ? -1 : min;
}
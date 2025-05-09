function solution(players, m, k) {
    let answer = 0;
    let count = 1; // 서버 수 
    
    let servers = Array(players.length).fill(0);
    
    players.forEach((player, time) => {
        if(parseInt(player / m) > servers[time]){
            let needServer =  parseInt(player / m) - servers[time];
            
            for(i = 0; i< k; i++){
                if (time + i <= 23){
                    servers[time + i] += needServer;
                }
            }
            answer += needServer;
        }
    })
    
    return answer;
}
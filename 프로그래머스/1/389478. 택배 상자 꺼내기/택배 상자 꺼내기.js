function solution(n, w, num) {
    if (w === 1) return n - num + 1;
    
    const arr = Array.from({length: w}, () => []);
    const h = Math.trunc(n / w);
    for(let i = 1; i <= n; i++){
        const r = i % w;
        if (!r) arr[w-1].push(i);
        else arr[r-1].push(i);
        if(!r) arr.reverse();
        console.log(arr);
    }
    
    if (h%2) arr.reverse();
    
    for(let i = 0; i< w; i++){
        if (arr[i].includes(num)) return arr[i].length - arr[i].indexOf(num);
    }
}
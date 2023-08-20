

function base8(num){
    if(num == 0){
        return 0
    }
    else{
        return (num % 8) + 10 * base8(Math.floor(num / 8))
    }
}

console.log(base8(0))
console.log(base8(8))
console.log(base8(10))